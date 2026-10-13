#!/usr/bin/env python3
"""Read-only Starfield plugin structure probe.

Phase-0 goals:
- walk Bethesda GRUP/record structures
- index raw FormIDs and EDIDs
- transparently decompress compressed records
- enumerate subrecords, including XXXX extended-size subrecords
- never modify the source file

This is intentionally a narrow research tool, not an xEdit replacement.
"""

from __future__ import annotations

import argparse
import json
import mmap
import os
import struct
import sys
import zlib
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable, Iterator, Optional

MAIN_HEADER_SIZE = 24
GRUP_HEADER_SIZE = 24
COMPRESSED_FLAG = 0x00040000

_U16 = struct.Struct("<H")
_U32 = struct.Struct("<I")
_MAIN = struct.Struct("<4sIIIHH")  # sig, size, flags, formid, vc_info, form_version
_GROUP = struct.Struct("<4sI4sIHH")  # sig, size, label, group_type, stamp, unknown
_SUB = struct.Struct("<4sH")


class ProbeError(RuntimeError):
    pass


@dataclass(slots=True)
class RecordHeader:
    signature: str
    data_size: int
    flags: int
    form_id: int
    vc_info: int
    form_version: int
    offset: int
    group_path: tuple[str, ...]

    @property
    def compressed(self) -> bool:
        return bool(self.flags & COMPRESSED_FLAG)


@dataclass(slots=True)
class Subrecord:
    signature: str
    size: int
    offset: int
    data: bytes


@dataclass(slots=True)
class RecordIndexEntry:
    signature: str
    form_id: int
    flags: int
    offset: int
    data_size: int
    compressed: bool
    edid: Optional[str]
    group_path: tuple[str, ...]


class PluginReader:
    def __init__(self, path: Path):
        self.path = path
        self._fh = None
        self._mm: mmap.mmap | None = None

    def __enter__(self) -> "PluginReader":
        self._fh = self.path.open("rb")
        self._mm = mmap.mmap(self._fh.fileno(), 0, access=mmap.ACCESS_READ)
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        if self._mm is not None:
            self._mm.close()
            self._mm = None
        if self._fh is not None:
            self._fh.close()
            self._fh = None

    @property
    def data(self) -> mmap.mmap:
        if self._mm is None:
            raise ProbeError("reader is not open")
        return self._mm

    def walk_records(self) -> Iterator[RecordHeader]:
        yield from self._walk_range(0, len(self.data), ())

    def _walk_range(
        self,
        start: int,
        end: int,
        group_path: tuple[str, ...],
    ) -> Iterator[RecordHeader]:
        pos = start
        data = self.data

        while pos < end:
            if end - pos < 4:
                raise ProbeError(
                    f"trailing {end - pos} byte(s) at 0x{pos:X} inside {group_path}"
                )

            sig_raw = data[pos : pos + 4]
            try:
                sig = sig_raw.decode("ascii")
            except UnicodeDecodeError as exc:
                raise ProbeError(f"non-ASCII signature at 0x{pos:X}: {sig_raw!r}") from exc

            if sig == "GRUP":
                if end - pos < GRUP_HEADER_SIZE:
                    raise ProbeError(f"truncated GRUP header at 0x{pos:X}")
                raw = data[pos : pos + GRUP_HEADER_SIZE]
                _, group_size, label_raw, group_type, stamp, unknown = _GROUP.unpack(raw)
                if group_size < GRUP_HEADER_SIZE:
                    raise ProbeError(
                        f"invalid GRUP size {group_size} at 0x{pos:X}; smaller than header"
                    )
                group_end = pos + group_size
                if group_end > end:
                    raise ProbeError(
                        f"GRUP at 0x{pos:X} extends to 0x{group_end:X}, container ends 0x{end:X}"
                    )
                label = self._format_group_label(label_raw, group_type)
                desc = f"type={group_type}:{label}"
                yield from self._walk_range(
                    pos + GRUP_HEADER_SIZE,
                    group_end,
                    group_path + (desc,),
                )
                pos = group_end
                continue

            if end - pos < MAIN_HEADER_SIZE:
                raise ProbeError(f"truncated record header at 0x{pos:X}")

            raw = data[pos : pos + MAIN_HEADER_SIZE]
            sig_raw, size, flags, form_id, vc_info, form_version = _MAIN.unpack(raw)
            signature = sig_raw.decode("ascii", errors="replace")
            payload_end = pos + MAIN_HEADER_SIZE + size
            if payload_end > end:
                raise ProbeError(
                    f"record {signature} {form_id:08X} at 0x{pos:X} extends to "
                    f"0x{payload_end:X}, container ends 0x{end:X}"
                )

            yield RecordHeader(
                signature=signature,
                data_size=size,
                flags=flags,
                form_id=form_id,
                vc_info=vc_info,
                form_version=form_version,
                offset=pos,
                group_path=group_path,
            )
            pos = payload_end

    @staticmethod
    def _format_group_label(label_raw: bytes, group_type: int) -> str:
        if group_type == 0:
            return label_raw.decode("ascii", errors="replace")
        return f"0x{int.from_bytes(label_raw, 'little'):08X}"

    def raw_payload(self, header: RecordHeader) -> bytes:
        start = header.offset + MAIN_HEADER_SIZE
        end = start + header.data_size
        return bytes(self.data[start:end])

    def payload(self, header: RecordHeader) -> bytes:
        raw = self.raw_payload(header)
        if not header.compressed:
            return raw
        if len(raw) < 4:
            raise ProbeError(
                f"compressed record {header.signature} {header.form_id:08X} has no size prefix"
            )
        expected_size = _U32.unpack_from(raw, 0)[0]
        try:
            inflated = zlib.decompress(raw[4:])
        except zlib.error as exc:
            raise ProbeError(
                f"zlib failure for {header.signature} {header.form_id:08X}: {exc}"
            ) from exc
        if len(inflated) != expected_size:
            raise ProbeError(
                f"decompressed-size mismatch for {header.signature} {header.form_id:08X}: "
                f"expected {expected_size}, got {len(inflated)}"
            )
        return inflated

    def subrecords(self, header: RecordHeader) -> Iterator[Subrecord]:
        payload = self.payload(header)
        pos = 0
        extended_size: Optional[int] = None

        while pos < len(payload):
            if len(payload) - pos < _SUB.size:
                raise ProbeError(
                    f"truncated subrecord header in {header.signature} {header.form_id:08X} "
                    f"at payload +0x{pos:X}"
                )
            sig_raw, short_size = _SUB.unpack_from(payload, pos)
            sig = sig_raw.decode("ascii", errors="replace")
            header_pos = pos
            pos += _SUB.size

            if sig == "XXXX":
                if short_size != 4 or len(payload) - pos < 4:
                    raise ProbeError(
                        f"invalid XXXX in {header.signature} {header.form_id:08X} "
                        f"at payload +0x{header_pos:X}"
                    )
                extended_size = _U32.unpack_from(payload, pos)[0]
                pos += 4
                continue

            size = extended_size if extended_size is not None else short_size
            extended_size = None
            end = pos + size
            if end > len(payload):
                raise ProbeError(
                    f"subrecord {sig} in {header.signature} {header.form_id:08X} "
                    f"requests {size} bytes at payload +0x{header_pos:X}, "
                    f"only {len(payload) - pos} remain"
                )
            yield Subrecord(signature=sig, size=size, offset=header_pos, data=payload[pos:end])
            pos = end

        if extended_size is not None:
            raise ProbeError(
                f"dangling XXXX at end of {header.signature} {header.form_id:08X}"
            )

    def edid(self, header: RecordHeader) -> Optional[str]:
        try:
            for sub in self.subrecords(header):
                if sub.signature == "EDID":
                    return sub.data.split(b"\x00", 1)[0].decode("utf-8", errors="replace")
        except ProbeError:
            raise
        return None

    def find_form_id(self, form_id: int) -> Optional[RecordHeader]:
        for header in self.walk_records():
            if header.form_id == form_id:
                return header
        return None


def parse_form_id(text: str) -> int:
    value = text.strip().lower()
    if value.startswith("0x"):
        value = value[2:]
    try:
        return int(value, 16)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"invalid hex FormID: {text}") from exc


def make_index(reader: PluginReader) -> Iterator[RecordIndexEntry]:
    for header in reader.walk_records():
        try:
            edid = reader.edid(header)
        except ProbeError:
            edid = None
        yield RecordIndexEntry(
            signature=header.signature,
            form_id=header.form_id,
            flags=header.flags,
            offset=header.offset,
            data_size=header.data_size,
            compressed=header.compressed,
            edid=edid,
            group_path=header.group_path,
        )


def command_scan(args: argparse.Namespace) -> int:
    path = Path(args.plugin)
    counts: dict[str, int] = {}
    total = 0
    with PluginReader(path) as reader:
        for header in reader.walk_records():
            total += 1
            counts[header.signature] = counts.get(header.signature, 0) + 1
    result = {
        "plugin": str(path),
        "size": path.stat().st_size,
        "records": total,
        "signatures": dict(sorted(counts.items())),
    }
    print(json.dumps(result, indent=2))
    return 0


def command_record(args: argparse.Namespace) -> int:
    path = Path(args.plugin)
    with PluginReader(path) as reader:
        header = reader.find_form_id(args.form_id)
        if header is None:
            print(f"FormID {args.form_id:08X} not found", file=sys.stderr)
            return 2
        subs = list(reader.subrecords(header))
        result = {
            "plugin": str(path),
            "record": {
                "signature": header.signature,
                "form_id": f"{header.form_id:08X}",
                "flags": f"0x{header.flags:08X}",
                "compressed": header.compressed,
                "offset": f"0x{header.offset:X}",
                "data_size": header.data_size,
                "form_version": header.form_version,
                "vc_info": header.vc_info,
                "group_path": list(header.group_path),
                "edid": reader.edid(header),
                "subrecords": [
                    {
                        "signature": sub.signature,
                        "size": sub.size,
                        "offset": f"0x{sub.offset:X}",
                    }
                    for sub in subs
                ],
            },
        }
        print(json.dumps(result, indent=2))
    return 0


def command_search_edid(args: argparse.Namespace) -> int:
    path = Path(args.plugin)
    needle = args.text.casefold()
    matches: list[dict[str, object]] = []
    with PluginReader(path) as reader:
        for entry in make_index(reader):
            if entry.edid and needle in entry.edid.casefold():
                matches.append(
                    {
                        "signature": entry.signature,
                        "form_id": f"{entry.form_id:08X}",
                        "edid": entry.edid,
                        "offset": f"0x{entry.offset:X}",
                    }
                )
    print(json.dumps({"plugin": str(path), "matches": matches}, indent=2))
    return 0


def command_dump_subrecords(args: argparse.Namespace) -> int:
    path = Path(args.plugin)
    with PluginReader(path) as reader:
        header = reader.find_form_id(args.form_id)
        if header is None:
            print(f"FormID {args.form_id:08X} not found", file=sys.stderr)
            return 2
        rows = []
        for sub in reader.subrecords(header):
            row: dict[str, object] = {
                "signature": sub.signature,
                "size": sub.size,
                "offset": f"0x{sub.offset:X}",
            }
            if args.hex:
                row["hex"] = sub.data.hex()
            rows.append(row)
        print(
            json.dumps(
                {
                    "record": f"{header.signature}:{header.form_id:08X}",
                    "edid": reader.edid(header),
                    "subrecords": rows,
                },
                indent=2,
            )
        )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="sfprobe",
        description="Read-only structural probe for Starfield ESM/ESP plugins",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_scan = sub.add_parser("scan", help="walk the plugin and summarize record signatures")
    p_scan.add_argument("plugin")
    p_scan.set_defaults(func=command_scan)

    p_record = sub.add_parser("record", help="inspect one raw FormID")
    p_record.add_argument("plugin")
    p_record.add_argument("form_id", type=parse_form_id)
    p_record.set_defaults(func=command_record)

    p_search = sub.add_parser("search-edid", help="case-insensitive EDID substring search")
    p_search.add_argument("plugin")
    p_search.add_argument("text")
    p_search.set_defaults(func=command_search_edid)

    p_dump = sub.add_parser("dump-subrecords", help="enumerate subrecords for one raw FormID")
    p_dump.add_argument("plugin")
    p_dump.add_argument("form_id", type=parse_form_id)
    p_dump.add_argument("--hex", action="store_true", help="include complete subrecord payload hex")
    p_dump.set_defaults(func=command_dump_subrecords)

    return parser


def main(argv: Optional[list[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return int(args.func(args))
    except (OSError, ProbeError) as exc:
        print(f"sfprobe: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
