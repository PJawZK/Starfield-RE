# sfprobe architecture derived from xEdit reference study

Status: initial design / read-only implementation target

## Purpose

`sfprobe` is a Linux-native, read-only Starfield data inspection tool for the reverse-engineering project. It is intentionally narrower than xEdit.

The goal is not to replace xEdit wholesale. The goal is to implement the smallest trustworthy subset needed for Starfield world research, beginning with Bel I-a / Khepri.

Primary initial capabilities:

- open `Starfield.esm` and other Starfield plugins directly
- walk top-level records and nested `GRUP` structures
- index records by raw FormID
- index EDIDs where available
- decompress compressed records
- enumerate subrecords, including extended-size subrecords
- inspect a selected record without modifying the source file
- export machine-readable JSON for later graphing and diffing
- add semantic decoders incrementally, beginning with `PNDT`

No write support is permitted in phase 0.

## Why xEdit is the right reference

xEdit separates a generic Bethesda plugin implementation from game-specific definitions. For Starfield, the repository contains a dedicated `Core/wbDefinitionsSF1.pas` rather than treating Starfield as Fallout 4 with renamed records.

The Starfield definition layer includes first-class Starfield signatures and explicit `PNDT` planet-data decoding. xEdit currently treats Starfield main records as 24-byte main-record structures and includes Starfield-specific archive, load-order and record-definition logic.

This makes xEdit useful in three ways:

1. format reference
2. behavior oracle for validation
3. source of known semantic field names and relationships

`sfprobe` should not reproduce xEdit's GUI, conflict-resolution engine, scripting layer or decades of compatibility logic.

## Licensing boundary

xEdit source is MPL-2.0.

For `sfprobe`:

- prefer independent implementation from documented behavior and observed file structure
- record where xEdit informed field semantics
- avoid mechanically transplanting large blocks of MPL source into unrelated files
- if code is ever directly reused, preserve MPL obligations and isolate that code clearly

The current implementation plan is independent code using xEdit as a reference specification and validation oracle.

## Relevant xEdit structure

The most useful upstream areas are:

- `Core/wbImplementation.pas` — generic element/file/record implementation
- `Core/wbInterface.pas` — common record/element interfaces and definitions
- `Core/wbDefinitionsCommon.pas` — shared Bethesda definitions and helpers
- `Core/wbDefinitionsSF1.pas` — Starfield record definitions
- `Core/wbDefinitionsSignatures.pas` — record/subrecord signatures
- `Core/wbCompression.pas` — compressed record handling
- `Core/wbLoadOrder.pas` — plugin/load-order semantics
- `Core/wbBSArchive.pas` / `BSArch*` — Starfield archive support

For Khepri, `wbDefinitionsSF1.pas` is the immediate priority.

## Confirmed Starfield PNDT structure useful to Khepri

xEdit's current Starfield definition exposes `PNDT` (`Planet`) with the following major fields.

### Identity and common data

- `EDID`
- base-form components

### Surface worldspace links

`CNAM` — Master Worldspaces, each entry containing:

- latitude
- longitude
- `WRLD` FormID

`EOVR` — Edited Worldspaces, each entry containing:

- latitude
- longitude
- `WRLD` FormID
- type: removed or added

This is directly relevant to tracing generated/edited planetary surface worldspaces.

### xEdit post-load normalization of CNAM/EOVR

`PNDT` uses xEdit's `wbPNDTAfterLoad` callback. This callback is presentation/normalization logic rather than a reinterpretation of the planet's physical fields.

Observed behavior:

- for a master record, xEdit ensures `CNAM` exists, removes `CNAM` entries whose worldspace FormID is zero, and removes `EOVR`
- for an override record, xEdit ensures `EOVR` exists, removes `EOVR` entries whose worldspace FormID is zero, and removes `CNAM`

Therefore `sfprobe` should keep two concepts separate:

1. **raw view** — exactly which subrecords and bytes are present on disk
2. **normalized view** — optional xEdit-equivalent interpretation for comparison

The raw view is authoritative for reverse engineering. Normalization must never silently erase evidence from the raw report.

### Biomes

`PPBD` entries expose:

- `BIOM` FormID
- chance
- resource-generation FormID (`RSGD` or NULL)
- fauna FormIDs
- keyword FormIDs
- flora entries
  - `FLOR` FormID
  - resource FormID
  - frequency

### Surface generation

- `FNAM` — Surface Tree (`SFTR`)
- `GNAM` — Scan Worldspace Multiplier

### Body data

A bounded `BDST` / `BDED` body structure contains:

- `ANAM` — body name
- `XEMP` — environment map
- `CNAM` — body type
  - Undefined
  - Star
  - Planet
  - Moon
  - Orbital
  - Asteroid Belt
  - Station
- `DNAM` — Space Cell
  - cell editor ID
  - unique flag
- `ENAM` — Orbital Data
  - major axis
  - minor axis
  - aphelion
  - eccentricity
  - incline
  - mean orbit
  - axial tilt
  - rotational velocity
  - start angle
  - perihelion angle
  - apply orbital velocity
  - geostationary orbit
- `FNAM` — Orbited Data
  - gravity well
  - mass in Earth masses
  - radius in km
  - surface gravity
- `GNAM` — Galaxy Data
  - star system ID
  - parent planet ID
  - planet ID
- `HNAM` — legacy/auxiliary astronomical data including year length and random seed
- `INAM` — Atmosphere Data
  - `ATMO` FormID or NULL
  - average density fraction
  - Rayleigh scattering coefficient
  - Mie scattering coefficient
- `KNAM` — Biome Noise
  - noise filename
  - biome frequency
  - terrain-height frequency
  - noise type
  - terrain-height seed
  - terrain max height in metres
- `NNAM` — player knowledge flags

### Remaining PNDT fields

- `TEMP` — temperature in C
- `DENS` — density
- `PHLA` — perihelion angle
- `RSCS` — resource-creation seed

These fields make `PNDT` the first high-value semantic decoder for `sfprobe`.

## Phase-0 parser architecture

```text
Starfield.esm
    |
    v
binary reader
    |
    +-- file/record header reader
    +-- GRUP walker
    +-- record decompressor
    +-- subrecord iterator
    |
    v
record index
    |
    +-- by FormID
    +-- by signature
    +-- by EDID
    |
    v
semantic decoders
    |
    +-- PNDT first
    +-- WRLD
    +-- LCTN
    +-- CELL
    +-- REGN
    +-- BIOM
    +-- WTHR
    +-- SFTR/RSGD as required
```

## Data model

The phase-0 core should stay deliberately simple.

### RecordHeader

- signature
- data size
- flags
- raw FormID
- revision/version control fields
- source offset
- group path

Starfield uses a 24-byte main-record structure according to xEdit's current `wbDefinitionsSF1.pas` initialization. xEdit's common `wbRecordHeader()` definition expands that as:

- signature — 4 bytes
- data size — u32
- flags — u32
- FormID — u32
- version-control info 1 — 4 bytes
- form version — u16
- version-control info 2 — 2 bytes

### Subrecord

- signature
- data size
- raw bytes / memory view
- record-relative offset

### Record

- header
- decompressed payload view
- subrecord list on demand
- EDID on demand

Avoid eagerly decoding all records. `Starfield.esm` is large and most records are irrelevant to a focused query.

## Parsing policy

### Read-only first

The parser must never modify the source plugin in phase 0.

### Strict bounds checking

Every header and payload must remain inside its containing record or group.

Malformed sizes should produce an explicit error including:

- file offset
- group path
- record signature/FormID when known
- expected size
- available bytes

### Compression

Compressed records should be transparently decompressed into an owned byte buffer before subrecord iteration.

Do not assume every record uses compression.

### Extended subrecord sizes

Support Bethesda `XXXX` extended-size subrecords before declaring the generic scanner usable.

### Unknown data preservation

Semantic decoders must not discard unknown bytes or silently reinterpret them.

A decoder should be able to report both:

- understood fields
- unknown/unconsumed regions

## First commands

Target CLI:

```bash
python -m sfprobe scan /path/to/Starfield.esm
python -m sfprobe record /path/to/Starfield.esm 0005DFB2
python -m sfprobe search-edid /path/to/Starfield.esm BelI-aPlanetData
python -m sfprobe dump-subrecords /path/to/Starfield.esm 0005DFB2
```

Later:

```bash
python -m sfprobe planet /path/to/Starfield.esm 0005DFB2 --json bel-ia.json
python -m sfprobe refs /path/to/Starfield.esm 0005DFB2
python -m sfprobe world-map /path/to/Starfield.esm 0005DFB2
```

## Validation target: Bel I-a

Known research anchor:

- raw FormID: `0005DFB2`
- EDID: `BelI-aPlanetData`

The first acceptance test is deliberately narrow:

1. locate raw FormID `0005DFB2`
2. verify record signature is `PNDT`
3. recover `EDID = BelI-aPlanetData`
4. enumerate every subrecord signature and byte length
5. compare the result with SF1Edit/xEdit
6. decode `PNDT` fields incrementally
7. verify the surface-worldspace FormIDs exposed by `CNAM`/`EOVR`

## PNDT implementation order

Do not implement the entire structure in one pass.

### P0

- EDID
- top-level subrecord enumeration
- raw `CNAM`/`EOVR` collection
- `TEMP`, `DENS`, `PHLA`, `RSCS`

### P1

- `BDST`...`BDED` body section
- body type
- space-cell editor ID
- orbital data
- mass/radius/gravity
- galaxy identifiers

### P2

- atmosphere data
- biome noise
- surface tree
- biome FormIDs

### P3

- full biome entry decoding
- resource generation
- flora/fauna/keywords

## Reference graph layer

Once generic record indexing works, build two maps:

```text
outgoing[record] -> referenced FormIDs
incoming[target] -> records that reference target
```

Start conservatively. FormID extraction should come from known semantic fields rather than treating every four-byte value as a FormID.

For Khepri this allows:

```text
BelI-aPlanetData
  -> surface WRLD records
  -> BIOM records
  -> ATMO
  -> SFTR
  -> RSGD
```

and then reverse-reference discovery for locations, quests or generation records that point back into those structures.

## Why Python first

Python is appropriate for phase 0 because:

- Linux-native
- zero proprietary toolchain requirement
- fast iteration on binary formats
- easy JSON/report output
- easy integration with later RE scripts
- performance is sufficient for indexed sequential scanning if implemented carefully

If profiling later shows that archive or full-plugin indexing is a bottleneck, the stable parser core can be migrated to Rust/C++ without changing the output schema.

## Writer policy

Do not implement plugin writing until all of these are true:

- generic scanner passes on multiple official plugins
- compressed/uncompressed records validated
- extended subrecords validated
- FormID/load-order semantics validated
- PNDT decode matches xEdit for representative planets
- round-trip semantic comparison tooling exists

The first writer should target a disposable generated test plugin, never `Starfield.esm`.

## Immediate next step

Test the generic read-only scanner against the user's current installed `Starfield.esm`.

Required first local command once the game files are available:

```bash
python tools/sfprobe/sfprobe.py record "/path/to/Starfield/Data/Starfield.esm" 0005DFB2
```

The output from that run becomes the first empirical fixture for the Bel I-a record map.
