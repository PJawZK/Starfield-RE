# Starfield Overhaul Project Foundation

Status: initial architecture and research baseline

## Purpose

This project aims to explore how far Starfield can be transformed into a more coherent, alien, spatially explorable space RPG while preserving the parts of the base game that already work well.

The goal is not to reproduce Elite Dangerous, No Man's Sky, or another existing space game. The goal is to expand Starfield's existing ship, exploration, combat, and world systems so they feel physically connected and creatively distinctive.

The immediate phase is technical exploration rather than production overhaul development.

## Design pillars

### 1. Strange worlds

Planets should not default to familiar Earth analogues with a different skybox.

Earth-like features are valid where biologically and geologically plausible, but they should be the exception rather than the visual norm.

Planetary identity should come from a coherent combination of:

- geology
- terrain silhouette
- atmosphere
- weather
- lighting
- flora morphology
- fauna morphology
- ecological relationships
- hazards
- resource structure
- architecture and ruins
- traversal constraints
- unique gameplay mechanics

A planet should change how the player behaves, not merely how the screenshots look.

### 2. No meaningless repetition

Repeated POIs with identical layouts, bodies, terminals, loot, and environmental storytelling are considered a core design failure.

Procedural systems should support authored structure rather than repeatedly selecting static prefabs.

Long-term location generation should combine coherent elements such as:

- location purpose
- construction style
- faction history
- environmental state
- damage state
- current occupants
- room/module graph
- defenses
- loot logic
- local ecology
- narrative state

### 3. Space is a place

Space should be explorable rather than functioning only as a staging cell before another fast-travel action.

Travel through space should be capable of containing:

- hidden bases
- asteroid installations
- wreck fields
- derelicts
- signals
- patrols
- ambushes
- mining activity
- smugglers
- environmental hazards
- unusual astronomical phenomena

### 4. Ships are vehicles

The player ship should feel like a physical vehicle, not an interior cell attached to a destination-selection interface.

The overhaul should preserve Starfield's existing ship-building identity and broadly preserve its accessible combat handling unless a later experiment demonstrates a clear reason to replace it.

### 5. Planetary flight enables adventure

The central flight objective is not complete aerospace simulation.

The required experience is the ability to use the existing ship as a meaningful planetary and lunar vehicle:

- take off
- fly near terrain
- enter craters and canyons
- collide with terrain correctly
- use ship weapons
- encounter ships and defenses
- discover locations through flight
- land again

Long-term examples include:

- low-altitude canyon runs
- crater assaults
- asteroid tunnels
- hollow moons or asteroids
- pirate bases embedded into terrain
- concealed hangars
- ship-accessible caverns

### 6. Procedural generation supports authorship

Procedural generation is not rejected. Repetition without systemic meaning is rejected.

Generated content should encode causal relationships, world history, and environmental logic.

### 7. Fewer deep experiences are preferable to larger content counts

A smaller number of memorable, coherent worlds is preferable to a very large number of interchangeable environments.

## Acceptable technical illusion

The project does not require technical purity if the player experience is convincing.

For example, if a truly continuous surface-to-orbit worldspace cannot be achieved safely, a hidden state transition may be acceptable when all of the following are preserved convincingly:

- player control
- ship heading
- apparent velocity
- cockpit state
- destination continuity
- visual continuity
- no map interaction
- no conventional loading screen

A transition concealed by atmosphere, cloud, plasma blackout, or another natural event is acceptable if it feels continuous to the player.

The project should optimize for player-perceived continuity rather than engine-theoretical purity.

## Technical architecture

Three logical repositories are preferred.

### `rea_JZ-Fork`

Purpose: reverse-engineering tooling.

Responsibilities:

- REA development
- Ghidra/IDA/Hopper integration
- analysis automation
- evidence collection
- reusable reverse-engineering workflows

Starfield-specific production mod code should not live here.

### `Starfield-RE`

Purpose: Starfield engine research and experimental findings.

Proposed structure:

```text
Starfield-RE/
  README.md
  versions/
  engine/
    worldspace/
    ships/
    physics/
    cells/
    terrain/
    streaming/
    loading/
    planets/
  symbols/
  offsets/
  types/
  hooks/
  experiments/
  findings/
  evidence/
```

This repository should record conclusions and evidence separately from production code.

### `Starfield-Overhaul`

Purpose: shipping mod and supporting build system.

Expected areas:

```text
Starfield-Overhaul/
  docs/
  specs/
  src/native/
  src/papyrus/
  plugins/
  assets/
  tools/
  tests/
  telemetry/
  staging/
  .github/
```

## Core development stack

Initial target stack:

- Steam Starfield runtime
- Creation Kit
- SFSE
- Address Library where applicable
- active CommonLibSF fork/tooling
- Papyrus
- SF1Edit/xEdit
- C++ native plugins only where required
- Python/PowerShell for generation, validation, packaging, and telemetry analysis
- REA with Ghidra/IDA/Hopper for closed-engine investigation

## Research rules

1. Prefer vanilla records and supported Creation Kit interfaces when sufficient.
2. Use Papyrus for event-driven game logic and glue.
3. Use SFSE/native code only when vanilla interfaces are insufficient or materially unsuitable.
4. Reverse engineer before guessing about hard engine limits.
5. Keep experimental hooks isolated from production systems.
6. Record evidence for important engine conclusions.
7. Separate runtime-version-specific offsets and signatures from gameplay logic.
8. Build instrumentation alongside experimental systems.
9. Treat Bethesda updates as expected rather than exceptional.
10. Make every important experiment reproducible.

## Initial research programmes

### A. Surface Flight

Question: can Starfield's existing ship become a practical planetary/lunar vehicle?

Highest-priority unknowns:

- player ship runtime representation
- flight-mode activation
- surface-worldspace restrictions
- ship physics controller behavior in surface worldspaces
- terrain collision
- landing state
- weapons
- NPC ship behavior
- terrain streaming at ship speeds
- cell/worldspace boundaries
- camera behavior
- player/ship interior relationship

### B. Surface-to-Orbit Continuity

Question: how much of the transition between planetary surface and orbital space can remain under player control?

This is secondary to proving surface flight.

### C. Alien World Authoring

Question: how far can terrain, biome, flora, fauna, lighting, weather, and POI systems be altered to create a world that does not read as Earth with substitutions?

### D. Dynamic Locations

Question: how much POI layout/state variation can be generated while remaining stable and believable?

### E. Space Exploration

Question: how much meaningful spatial content can exist between conventional Starfield travel destinations?

## First vertical slices

### Vertical Slice 1: Surface Flight Capability Probe

Use a barren moon to minimize atmospheric and ecological variables.

Required sequence:

```text
enter ship
 -> take off
 -> manual low-altitude flight
 -> terrain collision
 -> ship weapons
 -> crater/canyon traversal
 -> land again
```

This experiment deliberately excludes:

- orbit
- seamless atmospheric entry
- interplanetary travel
- major AI changes
- advanced flight physics

Success criteria are defined separately in `starfield-surface-flight-probe.md`.

### Vertical Slice 2: Alien Biosphere Prototype

Create one deliberately non-Earth-like life-bearing environment.

The prototype should prove that the project can achieve a coherent visual/ecological identity that is recognizable from screenshots without relying on a single gimmick.

Minimum targets:

- unfamiliar terrain silhouette
- non-default geological forms
- non-Earth flora morphology
- coherent environmental color/lighting
- unique weather or atmospheric behavior
- at least one environment-specific traversal or hazard mechanic
- unique POI visual language
- no obvious vanilla prefab repetition in the showcase area

## First showcase target: The Crater Run

Once surface flight is technically viable, the first gameplay showcase should demonstrate adventure enabled by flight rather than flight as a technical demonstration.

Concept:

```text
orbital/surface arrival
 -> crater rim
 -> descending canyon
 -> defensive emplacements
 -> hostile ships
 -> narrow terrain route
 -> concealed pirate facility
 -> external landing zone or hangar
 -> on-foot continuation
```

The exact implementation depends on capability-probe results.

## Player-test workflow

The intended development loop minimizes required player intervention.

A normal test cycle should be:

1. Developer/agent prepares a numbered build.
2. Automated checks run.
3. Build is deployed to a clean development profile.
4. Player performs a short explicit scenario.
5. Player reports observations and optionally provides video/logs.
6. Telemetry and logs are analyzed.
7. Findings and next actions are recorded.

A useful player report should be short, for example:

```text
Build 0.0.7
- takeoff works
- terrain collision works
- stutter crossing terrain boundary
- weapons work
- landing oscillates above ground
```

## Project phase definition

Current phase: **Capability Lab**

The Capability Lab ends when the major systems are classified as one of:

- supported directly
- supported through records/Creation Kit
- supported through Papyrus
- supported through SFSE/native extension
- supported with controlled approximation
- fragile/version-sensitive
- manual-authoring-only
- blocked by engine behavior
- unknown / requires further research

Production overhaul work should begin only after enough of this matrix is known to avoid building major systems on untested assumptions.
