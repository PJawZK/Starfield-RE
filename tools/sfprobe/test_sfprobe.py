#!/usr/bin/env python3

from __future__ import annotations

import importlib.util
import struct
import tempfile
import unittest
import zlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("sfprobe", HERE / "sfprobe.py")
assert SPEC and SPEC.loader
sfprobe = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sfprobe)


def sub(sig: bytes, payload: bytes) -> bytes:
    return struct.pack("<4sH", sig, len(payload)) + payload


def sub_extended(sig: bytes, payload: bytes) -> bytes:
    return (
        struct.pack("<4sH", b"XXXX", 4)
        + struct.pack("<I", len(payload))
        + struct.pack("<4sH", sig, 0)
        + payload
    )


def record(
    sig: bytes,
    form_id: int,
    payload: bytes,
    *,
    flags: int = 0,
    form_version: int = 1,
) -> bytes:
    if flags & sfprobe.COMPRESSED_FLAG:
        encoded = struct.pack("<I", len(payload)) + zlib.compress(payload)
    else:
        encoded = payload
    return (
        struct.pack(
            "<4sIIIHH",
            sig,
            len(encoded),
            flags,
            form_id,
            0,
            form_version,
        )
        + encoded
    )


def group(label: bytes, group_type: int, body: bytes) -> bytes:
    size = sfprobe.GRUP_HEADER_SIZE + len(body)
    return struct.pack("<4sI4sIHH", b"GRUP", size, label, group_type, 0, 0) + body


class SfProbeTests(unittest.TestCase):
    def write_fixture(self, data: bytes) -> Path:
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".esm")
        tmp.write(data)
        tmp.close()
        self.addCleanup(lambda: Path(tmp.name).unlink(missing_ok=True))
        return Path(tmp.name)

    def test_uncompressed_record_and_edid(self) -> None:
        payload = sub(b"EDID", b"BelI-aPlanetData\x00") + sub(b"TEMP", struct.pack("<f", 12.5))
        path = self.write_fixture(record(b"PNDT", 0x0005DFB2, payload))
        with sfprobe.PluginReader(path) as reader:
            header = reader.find_form_id(0x0005DFB2)
            self.assertIsNotNone(header)
            assert header is not None
            self.assertEqual(header.signature, "PNDT")
            self.assertEqual(reader.edid(header), "BelI-aPlanetData")
            self.assertEqual([s.signature for s in reader.subrecords(header)], ["EDID", "TEMP"])

    def test_nested_group_walk(self) -> None:
        payload = sub(b"EDID", b"InsideGroup\x00")
        inner = record(b"PNDT", 0x12345678, payload)
        path = self.write_fixture(group(b"PNDT", 0, inner))
        with sfprobe.PluginReader(path) as reader:
            rows = list(reader.walk_records())
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0].form_id, 0x12345678)
            self.assertTrue(rows[0].group_path)

    def test_compressed_record(self) -> None:
        payload = sub(b"EDID", b"CompressedPlanet\x00") + sub(b"RSCS", struct.pack("<i", 42))
        data = record(
            b"PNDT",
            0x01020304,
            payload,
            flags=sfprobe.COMPRESSED_FLAG,
        )
        path = self.write_fixture(data)
        with sfprobe.PluginReader(path) as reader:
            header = reader.find_form_id(0x01020304)
            self.assertIsNotNone(header)
            assert header is not None
            self.assertTrue(header.compressed)
            self.assertEqual(reader.edid(header), "CompressedPlanet")
            self.assertEqual([s.signature for s in reader.subrecords(header)], ["EDID", "RSCS"])

    def test_xxxx_extended_subrecord(self) -> None:
        payload_data = b"x" * 70000
        payload = sub(b"EDID", b"Extended\x00") + sub_extended(b"TEST", payload_data)
        path = self.write_fixture(record(b"PNDT", 0xAABBCCDD, payload))
        with sfprobe.PluginReader(path) as reader:
            header = reader.find_form_id(0xAABBCCDD)
            self.assertIsNotNone(header)
            assert header is not None
            rows = list(reader.subrecords(header))
            self.assertEqual(rows[1].signature, "TEST")
            self.assertEqual(rows[1].size, 70000)
            self.assertEqual(rows[1].data, payload_data)

    def test_invalid_record_bounds_fail_closed(self) -> None:
        bad = struct.pack("<4sIIIHH", b"PNDT", 1000, 0, 1, 0, 1) + b"tiny"
        path = self.write_fixture(bad)
        with sfprobe.PluginReader(path) as reader:
            with self.assertRaises(sfprobe.ProbeError):
                list(reader.walk_records())


if __name__ == "__main__":
    unittest.main()
