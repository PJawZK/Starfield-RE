# Alien World Capability Probe

Status: planned P0/P1 experiment

## Objective

Determine how far Starfield's planetary authoring stack can be pushed toward worlds that feel genuinely unfamiliar rather than like Earth biomes with altered color grading.

The goal is not to create a full production planet in this phase. The goal is to prove that one coherent test environment can establish a strong non-Earth identity through multiple systems at once.

## Design rule

A successful alien environment must differ in structure, not only in palette.

Changing sky color, fog, terrain tint, and plant color is insufficient.

The prototype should combine unfamiliar forms with internally consistent geology, ecology, atmosphere, and gameplay.

## Target prototype

Create one life-bearing test environment with all of the following characteristics:

- terrain silhouette that is not immediately Earth-like
- at least one unusual geological structure family
- flora with a morphology unlike common terrestrial trees/shrubs/grass
- atmospheric or lighting behavior that strongly shapes visibility and mood
- environmental hazard or traversal rule tied to the planet's physical conditions
- POI architecture that reacts to the environment
- no obvious duplicated vanilla showcase POIs inside the test region

## Candidate world concepts

These are examples, not locked production designs.

### Silica Storm World

- translucent/mineralized growth structures
- wind-driven abrasive weather
- long rib-like geological formations
- organisms sheltering in pressure shadows
- structures designed around erosion protection

### Dense-Atmosphere Float Biosphere

- low visibility
- buoyant organisms
- wide horizontal flora shaped by prevailing winds
- strong electrical activity
- navigation relying more heavily on instrumentation

### Tidal Terminator World

- extreme permanent day side
- extreme permanent night side
- narrow habitable terminator ecology
- strong lateral climate gradient
- settlements and migration patterns following the twilight band

The first prototype should choose one concept and develop it coherently rather than mix unrelated alien gimmicks.

## Capability questions

### Terrain and geology

1. How much control is available over terrain shape at local and biome scale?
2. Can large signature geological forms be distributed procedurally?
3. Can those forms participate reliably in collision and navigation?
4. Can terrain material logic vary meaningfully with altitude, slope, chemistry, or biome state?
5. Can recognizable planet-specific terrain language be created without hand-placing everything?

### Flora

6. What authoring path exists for fully custom flora meshes/materials?
7. How is flora distributed by biome and local conditions?
8. Can scale, orientation, clustering, and density rules be controlled?
9. Can flora placement avoid obvious repeated stamps?
10. Can flora support gameplay interactions or hazards beyond decoration?

### Fauna/ecology

11. How are fauna species tied to biome/location conditions?
12. How much custom AI/ecological behavior can be introduced?
13. Can predator/prey or territory relationships be represented convincingly?
14. Can spawn rules express environmental logic rather than simple random density?

### Atmosphere/weather/lighting

15. Which systems control atmospheric scattering, fog, sky, sun, exposure, and local lighting?
16. How much can visibility change dynamically with weather?
17. Can weather carry gameplay consequences?
18. Can environmental effects remain coherent indoors/outdoors and during time-of-day changes?

### POI integration

19. Can structures be selected or modified based on biome/environment?
20. Can planetary conditions influence architecture, damage state, defenses, and access routes?
21. Can the test region exclude obvious repeated vanilla POIs?
22. Can custom POIs be assembled from modular authored pieces without obvious repetition?

### Performance

23. How expensive are nonstandard flora densities and large geological forms?
24. What limits are encountered in visibility distance, LOD, shadows, collision, and streaming?
25. Which systems become bottlenecks before visual identity is achieved?

## Success levels

### A0 — authoring map

- relevant records/assets/systems identified
- custom test biome can be created
- toolchain path documented

### A1 — distinctive terrain

- environment silhouette differs clearly from common vanilla Earth-like biomes
- signature geological forms are repeatable and stable

### A2 — coherent biosphere

- custom flora family integrated
- atmosphere/lighting supports the same visual/ecological concept
- environment reads as one world rather than unrelated asset swaps

### A3 — gameplay identity

- at least one hazard/traversal mechanic emerges from planetary conditions
- architecture/POIs respond to those conditions

### A4 — showcase-ready

- test region is visually coherent from ground and air
- repeated vanilla-layout problem is absent from showcase path
- performance is acceptable
- assets and generation rules are reproducible

A3 is the minimum threshold for calling the alien-world pillar technically validated.

## Visual acceptance test

Use screenshot comparison as one acceptance tool.

A tester unfamiliar with the implementation should be able to distinguish the prototype from ordinary Starfield environments without being told which texture/lighting mods were used.

The environment should remain recognizable across:

- wide landscape view
- ground-level traversal
- POI exterior
- close vegetation view
- different weather/time conditions

If the identity disappears when color grading is removed, the prototype has failed the structural-alienness requirement.

## Relationship to surface flight

The alien-world probe should initially be developed independently from the surface-flight probe.

Once both reach useful maturity, combine them deliberately:

- terrain forms should create interesting ship-scale navigation
- vegetation/geology must account for ship collision and clearance
- POIs should include approach paths and landing logic
- atmospheric visibility should affect flight differently from walking exploration

The first combined showcase should happen only after both independent systems are stable enough that failures can be attributed correctly.
