# Shape Language and Anti-Patterns

Status: initial visual constraint set

## Why shape language matters

Alien environments fail when their identity depends on color, fog, emissive materials, or isolated props. The project should establish visual identity through silhouette and repeated structural rules first.

Each important world should have a limited set of dominant shapes that recur across geology, ecology, architecture, and traversal without becoming monotonous.

## Shape-language framework

For each world define:

- **Primary form** — the shape seen from the horizon or orbit.
- **Secondary form** — the shape encountered during traversal.
- **Detail form** — the small-scale pattern visible at close range.
- **Void form** — characteristic negative space: arches, fissures, gaps, sinkholes, channels, caverns.
- **Directional bias** — vertical, horizontal, radial, layered, branching, wind-swept, concentric, fractured, etc.

Example:

```text
World: silica storm world
Primary: long ribbed ridges
Secondary: leaning blade formations
Detail: glassy laminated surfaces
Void: narrow wind-cut slots
Bias: strongly aligned with prevailing winds
```

The same logic can influence buildings: walls align behind pressure shadows, roads follow protected slots, antennas sit on ridge ends, landing pads hide behind formations.

## Silhouette families worth exploring

These are visual tools, not mandatory planet categories:

- radial crater systems;
- stepped terraces;
- long parallel wind-carved ribs;
- vast horizontal shelves;
- vertical needle forests;
- branching fracture networks;
- giant arches and perforated terrain;
- bulbous pressure-grown geology;
- layered sediment cliffs at non-Earth scale;
- collapsed subsurface chambers;
- floating/buoyant forms;
- enormous root/web structures;
- crystalline fans and fracture planes;
- kilometer-scale biological mats;
- broken plate fields with deep glowing or fog-filled seams.

## Density rules

Alien does not mean everything must be busy.

Use visual density deliberately:

- large quiet regions make landmarks stronger;
- dense biology should have ecological reasons;
- geological complexity should concentrate around faults, impact zones, vents, shorelines, or other causal systems;
- settlement clutter should cluster around actual logistics and use.

The project should preserve negative space.

## Explicit anti-patterns

### 1. Earth biome plus recolor

Bad pattern:

```text
temperate forest
+ purple foliage
+ green fog
= alien planet
```

Recoloring may be part of the result but never the primary transformation.

### 2. Universal glowing flora

Bioluminescence should have an ecological or environmental function and should not be the default shorthand for alien life.

### 3. Giant mushrooms as automatic Morrowind homage

Fungal forms are valid where coherent, but using mushroom silhouettes everywhere would copy the surface signal instead of the underlying design lesson.

### 4. Random exotic props

A scene containing crystals, tentacle plants, floating rocks, glowing pools, and unusual fog is not automatically coherent.

Prefer two or three related ideas with clear physical logic.

### 5. Uniform procedural carpet

Avoid terrain where props are distributed at roughly equal density everywhere.

Life and geology should form clusters, corridors, edges, gradients, voids, and transition zones.

### 6. POI-on-a-plate

Avoid a complete prefab sitting on a flattened circular patch with no relationship to surrounding terrain.

The site should affect the structure before decoration is applied.

### 7. Every landmark is monumental

If everything is gigantic, nothing feels gigantic. Reserve extreme scale for strong focal elements and support them with quieter terrain.

### 8. Repetition hidden only by rotation

Rotating the same building or room layout does not create meaningful variety.

Variation should affect topology, approach, occupancy, damage, environment, and function.

### 9. Noise as complexity

Do not solve barren worlds by scattering more rocks and decals. Barren environments can be visually powerful through large forms, lighting, material transitions, erosion, and scale.

### 10. Alien architecture without engineering logic

Human structures can look adapted and unusual, but they should retain believable access, support, sealing, power, logistics, maintenance, and landing requirements.

## Grayscale test

Before approving a major environment concept:

1. remove or heavily reduce color information;
2. inspect horizon and mid-distance silhouette;
3. compare it with other reference worlds;
4. verify that major environmental identity survives.

If not, revise shape language before adding more palette effects.

## Thumbnail test

At small screenshot size, the world should still communicate:

- dominant terrain direction;
- one or two major forms;
- atmosphere depth;
- recognizable landmark or route.

This helps ensure scenes are composed rather than merely detailed.
