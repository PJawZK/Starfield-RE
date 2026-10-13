# Bel I-a / Khepri Record Probe

Status: implementation discovery baseline
Date: 2026-10-13

## Purpose

Map the concrete Starfield data/runtime chain for Bel I-a before any surface-flight patching or world overhaul work begins.

This document is intentionally narrower than `starfield-surface-flight-probe.md`. It records what is already known publicly, what must be verified against the user's local Starfield installation, and what evidence should be collected for the first runtime experiment.

## Known planetary identity

Current public data sources agree that Bel I-a is:

- a moon of Bel I in the Bel system;
- barren;
- gravity approximately 0.11 g;
- temperate;
- no atmosphere;
- no magnetosphere;
- no water;
- no flora/fauna;
- 100% crater biome in current public database data;
- approximately 59-day local day length;
- resources: Aluminum, Beryllium, Helium-3.

This remains an excellent first Khepri implementation laboratory because it has almost no ecological or weather-system baggage.

## Known record anchor

Public extracted-data references identify:

```text
FormID: 0005DFB2
EDID:   BelI-aPlanetData
Name:   Bel I-a
```

Treat this as a **public-data lead to verify locally**, not as a substitute for loading the current user's `Starfield.esm` in SF1Edit/Creation Kit.

The parent planet is reported immediately adjacent in the same public dataset:

```text
Bel I
FormID: 0005DFB1
EDID:   BelIPlanetData
```

The adjacency may be useful when inspecting the surrounding record hierarchy, but must not be assumed to imply every related surface/orbit/location record is also adjacent.

## Expected data layers

The record investigation should establish this chain with actual FormIDs/EDIDs from the installed game:

```text
Bel system
  |
  +-- Bel I planet data
        |
        +-- Bel I-a planet data (0005DFB2 / BelI-aPlanetData)
              |
              +-- general location
              +-- surface location
              +-- orbit location
              +-- worldspace / surface overlay relationship
              +-- biome list / planet BIOM map
              +-- content generation configuration
              +-- generated landing area records at runtime
```

Do not infer missing links from naming conventions. Record each link only after it is visible in current game data or runtime evidence.

## BIOM relationship

Current community tooling/research establishes that landable planets/moons rely on external `.biom` map data under Starfield's `planetdata/biomemaps` assets, while the planet data record identifies biome definitions/assignments used by the planet.

For Bel I-a, verify:

- exact BIOM file name/path;
- archive containing the vanilla file;
- biome identifiers referenced by `BelI-aPlanetData`;
- whether the 100% crater distribution is represented as a single biome mapping or a broader biome definition with one effective surface class;
- whether modifying only biome content changes dressing without changing macro terrain shape.

Important: current biome-authoring research indicates biome records primarily control terrain textures, grass/rocks/objects and flora/fauna; they do not necessarily control the large-scale terrain heightfield/shape. Khepri's fracture canyons and crater-route geometry therefore may require a different terrain/worldspace layer than simple biome replacement.

## Surface worldspace questions

Verify in CK/SF1Edit:

1. What WRLD record is associated with Bel I-a surface generation/overlay?
2. Is there one reusable/generated worldspace relationship or multiple surface worldspaces?
3. Which record links a newly created landing area to the planet?
4. Which fields point from planet data to surface/orbit locations?
5. What changes in plugin/save data after landing on a previously unused Bel I-a coordinate?
6. Which parts are persistent in the save versus regenerated?

Community guides confirm that Starfield planetary locations ultimately connect authored/exterior worldspaces to planetary coordinates and that generated landing-area markers are created when landing. The exact Bel I-a record path still needs local verification.

## Surface flight evidence relevant to Khepri

### Layer 1 — above-surface movement

Planetary vehicle systems already demonstrate high-speed traversal across exterior cells. Some vehicle mods alter vertical limits/boost behavior, although public user reports indicate that not every advertised 'airspeeder' behaves as true free atmospheric flight.

Conclusion: use the vehicle subsystem as a candidate controller architecture, but verify actual 3D vertical freedom ourselves instead of assuming it from mod marketing text.

### Layer 2 — landing/takeoff transitions

2026 SFSE mods demonstrate interception/manipulation of the normal landing/takeoff flow:

- Seamless Planet Takeoffs hides/removes the visible takeoff loading transition and relocates the ship into space;
- Immersive Landing lets the player physically approach a landing marker before invoking native landing.

Conclusion: transition handling is patchable, but this remains separate from surface flight.

### Layer 3 — global planet rendering / true descent

A separately demonstrated 2026 project shows manual/autopilot orbit-to-ground descent using rebuilt 3D planetary rendering, atmospheric layers, biome/climate data, oceans and landing anywhere. Public descriptions explicitly indicate substantial rendering reimplementation.

Conclusion: global seamless descent is no longer merely theoretical, but it is outside the first Khepri probe and should not dictate the low-altitude implementation architecture yet.

## First local extraction package

The first local evidence capture should export, without editing:

```text
records/
  bel-ia-planetdata.txt
  bel-i-parent-planetdata.txt
  bel-ia-referenced-locations.txt
  bel-ia-worldspace-links.txt
  bel-ia-biomes.txt
  bel-ia-content-generation.txt

runtime/
  baseline-version.txt
  landed-reference-observation.jsonl
  pilot-seat-surface-observation.jsonl
  vehicle-controller-observation.jsonl
  orbital-ship-observation.jsonl
```

Recommended additional screenshots only when they clarify relationships:

```text
screens/
  sf1edit-bel-ia-planetdata.png
  ck-bel-ia-galaxy-terraforming.png
  ck-bel-ia-location-links.png
```

Text exports are preferred over screenshots for searchable evidence.

## First no-code experiment

Before writing a plugin or SFSE hook:

1. Land at an unused/random Bel I-a coordinate.
2. Record the landing-area marker name and location.
3. Drive a normal planetary vehicle away from the ship in a straight line.
4. Cross as many exterior cell boundaries as practical.
5. Record performance, terrain pop-in, collision continuity, and distance from ship.
6. Return to the ship.
7. Save/reload the dedicated test save.
8. Verify whether the same generated landing area and nearby procedural layout persist.

This establishes a modern 2026 baseline for surface streaming and persistence before any flying controller is introduced.

## First code experiment after record mapping

Only after the record chain and baseline behavior are captured:

### A — vehicle-controller branch

Instrument the planetary vehicle controller and determine:

- vertical-cap field/function;
- gravity/grounding logic;
- boost acceleration;
- camera anchor;
- collision body;
- streaming anchor.

Attempt a minimal controlled vertical displacement and sustained hover-like state with an ordinary test vehicle before introducing ship visuals.

### B — native-ship branch

Instrument surface pilot-seat activation and compare it with orbital pilot-seat activation.

Identify the earliest divergence in:

- controller initialization;
- exterior reference state;
- camera/input state;
- worldspace/location checks;
- streaming anchor.

Do not patch the divergence until it is understood.

## Decision gate

After these two experiments, choose the production prototype branch using evidence:

| Criterion | Native ship | Vehicle proxy |
|---|---:|---:|
| Surface activation stability | TBD | TBD |
| Terrain collision | TBD | TBD |
| Cell streaming | TBD | TBD |
| Cockpit feasibility | TBD | TBD |
| Ship-builder compatibility | TBD | TBD |
| Weapons reuse | TBD | TBD |
| Landing-state recovery | TBD | TBD |
| Runtime patch complexity | TBD | TBD |

Do not choose the native-ship branch merely because it is conceptually cleaner. Do not choose the vehicle-proxy branch merely because it is easier to make move. The first Crater Run prototype needs the branch that gives the strongest combination of stability, ship identity, terrain interaction, and future extensibility.

## Current conclusion

Bel I-a is sufficiently well matched to Khepri to proceed as the first real implementation laboratory.

The next hard dependency is **local current-version record/runtime evidence**. Public data has given us the starting planet-data record (`0005DFB2`, `BelI-aPlanetData`), but worldspace/location links and runtime controller behavior must be established from the actual installed game before we begin patching.
