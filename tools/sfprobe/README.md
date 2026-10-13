# sfprobe

Read-only Starfield ESM/ESP structural probe.

`sfprobe` is intentionally narrow. It exists to support the Starfield reverse-engineering/world-overhaul project without making SF1Edit/xEdit a mandatory runtime dependency.

## Current phase

Phase 0 supports:

- 24-byte main record headers
- recursive `GRUP` walking
- raw FormID lookup
- compressed records (`0x00040000`)
- subrecord enumeration
- `XXXX` extended subrecord sizes
- `EDID` extraction
- JSON output

It does **not** write plugins.

## Requirements

- Python 3.11+ recommended
- standard library only

## Usage

```bash
python tools/sfprobe/sfprobe.py scan /path/to/Starfield.esm
```

Inspect Bel I-a by the currently known raw FormID:

```bash
python tools/sfprobe/sfprobe.py record /path/to/Starfield.esm 0005DFB2
```

Search by editor ID:

```bash
python tools/sfprobe/sfprobe.py search-edid /path/to/Starfield.esm BelI-aPlanetData
```

Enumerate all subrecords in Bel I-a:

```bash
python tools/sfprobe/sfprobe.py dump-subrecords /path/to/Starfield.esm 0005DFB2
```

For byte-level research on a selected record only:

```bash
python tools/sfprobe/sfprobe.py dump-subrecords /path/to/Starfield.esm 0005DFB2 --hex
```

## Expected first validation

The first real-data acceptance check is:

- FormID `0005DFB2` is found
- signature is `PNDT`
- EDID is `BelI-aPlanetData`
- subrecord sequence can be enumerated without bounds/decompression errors

Then compare that output with SF1Edit/xEdit.

## Safety

The program opens source plugins read-only and memory-maps them with `mmap.ACCESS_READ`.

No writer exists in phase 0.

## Known assumptions awaiting real-file validation

The initial scanner intentionally makes a small number of format assumptions based on xEdit's Starfield definitions and the modern Bethesda plugin family:

- Starfield main records use 24-byte headers.
- `GRUP` headers are treated as 24 bytes.
- compressed record payloads use a 32-bit uncompressed-size prefix followed by zlib data.
- ordinary subrecords use a 4-byte signature + 16-bit payload size.
- `XXXX` carries a 32-bit extended size for the following subrecord.

The 24-byte main-record size is directly reflected in xEdit's current Starfield initialization. The remaining structural assumptions must be validated against the user's current `Starfield.esm` before being treated as locked project facts.

## Next semantic decoder

`PNDT` is first because xEdit currently exposes useful Starfield planet semantics including:

- master/edited surface worldspaces
- lat/long placement
- biome links
- surface tree
- body type
- space-cell editor ID
- orbital data
- mass/radius/gravity
- atmosphere
- biome-noise/terrain-height controls
- temperature/density/resource seed

See `docs/sfprobe-xedit-architecture.md`.
