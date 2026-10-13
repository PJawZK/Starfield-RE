# Existing-World Mapping — Technical Validation

Status: first implementation-oriented validation pass

## Purpose

The six approved visual archetypes are now treated as overhaul targets for existing Starfield worlds rather than as six new planets. This document checks whether the provisional mappings make technical and content sense before implementation begins.

The important distinction is:

- **visual fit** — how well the existing world supports the concept;
- **content risk** — how much handcrafted/quest content already depends on the world;
- **systemic freedom** — how safely the world can be used as a laboratory for terrain, biome, weather, settlement, or flight experiments.

## Provisional mapping summary

| Archetype | Existing world | Physical fit | Existing-content risk | Systemic freedom | Current recommendation |
|---|---|---:|---:|---:|---|
| Eden-9 | Jemison | excellent | very high | low | keep mapping; defer large edits until systems proven elsewhere |
| Thalassa | Volii Alpha | excellent | very high | low-medium | keep mapping; defer deep edits until ocean/settlement systems proven |
| Pelagos | Newton II | excellent | low | high | strong candidate for alien-ecology implementation |
| Vitria | Procyon II | excellent | low | high | strong candidate for weather/geology implementation |
| Khepri | Bel I-a | excellent | very low | very high | best first technical laboratory |
| Nadir-Tau | Katydid III | strong but not fully verified | very low | very high | keep provisional; verify tidal/rotation behavior in records before lock |

## 1. Eden-9 -> Jemison

Vanilla baseline:

- rock world;
- gravity about 0.91 g;
- temperate;
- standard oxygen atmosphere;
- strong magnetosphere;
- safe water;
- 50-hour day;
- roughly 60% ocean;
- deciduous forest, mountains, frozen mountains, and coniferous forest;
- abundant flora/fauna;
- New Atlantis and other handcrafted content already present.

Why it fits:

Jemison already has almost everything the Eden-9 archetype needs physically. The overhaul therefore does not need to justify a pleasant, breathable, biodiverse world from scratch.

Primary work would be:

- metropolitan-scale visual expansion;
- ecological integration around New Atlantis and other settlement regions;
- biome cohesion;
- long-range wilderness continuity;
- future-human architecture and transit;
- improved weather identity;
- keeping large protected wilderness between urbanized regions.

Risk:

Jemison is one of the most quest- and city-dense planets in the game. Large-scale record changes should be treated as high-risk until the project has proven its world-editing and compatibility pipeline elsewhere.

Decision:

**Keep the mapping, but do not use Jemison as the first experimental implementation target.**

## 2. Thalassa -> Volii Alpha

Vanilla role:

- existing ocean world;
- Neon already establishes a major human presence;
- the planet is already central to trade, quests, and handcrafted content.

Why it fits:

Thalassa's strongest advantage is that we do not need to invent the narrative reason for a major oceanic settlement. Neon already supplies that anchor.

Primary work would be:

- make the rest of Volii Alpha visually live up to being an ocean planet;
- develop vertical volcanic/caldera geology;
- storm systems and sea-state identity;
- cliff, floating, and submerged infrastructure;
- marine ecology;
- ocean-flight routes and sheltered approaches;
- broader planetary context for Neon.

Risk:

Neon is a major handcrafted quest hub. Any change to landing, local worldspaces, water behavior, or nearby settlement geometry requires careful compatibility testing.

Decision:

**Keep the mapping, but treat Volii Alpha as a later integration target rather than an early systems laboratory.**

## 3. Pelagos -> Newton II

Vanilla baseline:

- gravity about 1.48 g;
- temperate;
- high molecular-weight atmosphere;
- biological water;
- 44-hour day;
- very strong wind potential;
- biomes include rocky desert, ocean, mountains, swamp, and frozen plains;
- traits include Aeriform Life, Amphibious Foothold, and Ecological Consortium;
- eight fauna and five flora.

Why it fits:

Newton II is already one of the strongest biological/atmospheric foundations for Pelagos. The overhaul can reinterpret existing life and biome systems into a much stranger layered biosphere rather than creating a living planet from zero.

Primary work would be:

- suspended/tethered/buoyant ecosystem structures;
- dense atmospheric layering;
- weather and electrical activity;
- large-scale horizontal biological forms;
- non-Earth-like ecology distribution;
- elevated/tethered human settlements;
- instrument-flight routes through atmosphere and biology.

Open questions:

- how much of the current biome distribution can be replaced or remapped without destabilizing procgen;
- whether large biological canopy structures are best implemented as biome assets, POI-scale statics, worldspace geometry, or a hybrid;
- fauna/navmesh behavior around radically vertical environments.

Decision:

**Strong second-wave implementation candidate.**

## 4. Vitria -> Procyon II

Vanilla baseline:

- gravity about 0.96 g;
- inferno temperature;
- extra-dense CO2 atmosphere;
- no surface water;
- 24-hour day;
- very high wind potential;
- 85% rocky desert / 15% hills;
- traits include Primed For Life, Prismatic Plumes, and Turbulent Lithosphere;
- no flora or fauna.

Why it fits:

This is nearly ideal for Vitria. The dry, dense-atmosphere, high-wind, lifeless baseline supports the entire wind-carved geology + silica-storm concept.

Primary work would be:

- kilometer-scale aligned yardang/blade geology;
- windward/lee differentiation;
- terrain shelter logic;
- storm-wall weather/VFX system;
- flight disturbance/turbulence layer;
- lee-side settlement architecture;
- abrasive-material effects and visibility degradation.

Risk:

Low relative to major inhabited worlds. The main difficulty is not quest compatibility but engine capability: weather-front spatialization, ship disturbance, and large-scale terrain identity.

Decision:

**Excellent technical target after Khepri.**

## 5. Khepri -> Bel I-a

Vanilla baseline:

- barren moon;
- gravity about 0.11 g;
- temperate surface rating;
- no atmosphere;
- no magnetosphere;
- no water;
- 59-day day length;
- 100% crater biome;
- no flora/fauna.

Why it fits:

Bel I-a is an extremely clean base for Khepri. Almost nothing in its physical baseline needs to be contradicted.

Primary work would be:

- major crater-basin identity;
- fracture/collapse terrain;
- localized anomaly scar;
- recessed/subsurface research and mining facilities;
- low-altitude ship routes;
- hidden hangars;
- surface-flight tests;
- terrain-streaming tests at ship speed;
- eventually surface->interior and surface->orbit transition experiments.

Advantages:

- very low content/quest risk;
- no biosphere to preserve;
- no atmosphere/weather system required for the first prototype;
- black-sky/vacuum lighting provides a simple visual validation environment;
- low gravity gives the surface-flight experiment a distinctive handling context.

Decision:

**Best first implementation laboratory.**

## 6. Nadir-Tau -> Katydid III

Vanilla baseline:

- rock world;
- gravity about 1.14 g;
- frozen temperature;
- standard nitrogen atmosphere;
- chemical water;
- 100-day day length;
- wind potential around 100%;
- hills, plateau, rocky desert, frozen plains;
- Energetic Rifting and Turbulent Lithosphere;
- no flora/fauna.

Why it fits:

The extremely long day and dry/frozen terrain make Katydid III a strong foundation for a permanent-direction climate world. It already supports the visual idea of large-scale hot/cold gradients better than most vanilla candidates.

Critical unresolved point:

A 100-day day length is not proof of tidal locking. Before permanently locking this mapping, the underlying planet/orbit/rotation records should be inspected for whether the desired fixed-star geometry can be represented directly, approximated through time/lighting, or must be faked through worldspace/climate systems.

Primary work would be:

- starward -> twilight -> nightward climate bands;
- permanent-direction lighting;
- heat/cold regional transitions;
- thermal-spine settlement structure;
- starward solar/industrial systems;
- nightward cryogenic infrastructure;
- lateral wind/weather circulation;
- flight routes crossing multiple climate bands.

Decision:

**Keep provisional until rotation/lighting behavior is verified in records and in-engine.**

## Implementation order

### Phase 1 — Khepri / Bel I-a

Use as the systems laboratory for:

- surface ship flight;
- ship-terrain collision;
- terrain streaming at flight speeds;
- ship weapons on surface;
- NPC ship surface behavior;
- terrain-scale route authoring;
- hidden hangar / interior transition;
- anomaly-zone environmental effects.

### Phase 2 — Vitria / Procyon II

Add:

- weather-front systems;
- visibility degradation;
- directional particle flow;
- terrain shelter;
- ship turbulence/disturbance;
- weather-aware AI/settlements if feasible.

### Phase 3 — Pelagos / Newton II

Add:

- radically non-Earth-like biome structure;
- large biological statics;
- suspended/tethered ecology;
- dense atmospheric navigation;
- ecology-aware settlement placement.

### Phase 4 — Nadir-Tau / Katydid III

Add:

- persistent climate direction;
- lighting/temperature-band experiments;
- settlement-as-thermal-machine architecture.

### Phase 5 — Thalassa / Volii Alpha

Integrate ocean-world systems into a major existing quest hub only after the project has proven world editing, flight, weather, and settlement adaptation elsewhere.

### Phase 6 — Eden-9 / Jemison

Treat Jemison/New Atlantis as the highest-risk integration target. By this stage, the project should already have mature tooling for world edits, architectural replacement, biome changes, transit, and compatibility validation.

## Current conclusion

The provisional mappings are technically sensible enough to proceed with.

The most important consequence of this pass is that implementation should **not** begin on the most visually ambitious or narratively important planets. It should begin on the cleanest systemic laboratory.

That makes **Bel I-a / Khepri** the correct first target, with **Procyon II / Vitria** second.

## Next verification work

Before coding the Khepri prototype, inspect the relevant game records and runtime behavior for:

1. Bel I-a planet record and biome setup;
2. surface worldspace/landing-area generation;
3. ship actor/reference type on planetary surfaces;
4. flight-state gating;
5. collision and gravity handling;
6. terrain streaming boundaries;
7. surface weapon enablement;
8. NPC ship behavior;
9. transition path between ship flight, landing, and interior spaces;
10. whether the moon can be safely used as a test world without touching quest-critical records.
