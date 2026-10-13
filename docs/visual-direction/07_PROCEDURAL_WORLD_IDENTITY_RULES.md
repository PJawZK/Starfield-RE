# Procedural World Identity Rules

Status: visual/procedural design baseline

## Purpose

This document defines how procedural generation may create variety without flattening every planet into the same underlying Starfield experience.

The goal is not maximal randomness. The goal is **causal variety inside a strong world identity**.

A generated location should feel like one possible outcome of that world's geology, climate, ecology, history, and human use — not like a generic prefab selected from a global pool.

## Core rule

Procedural generation may vary **solutions**, but it must preserve **causes**.

For every generated region or POI, the system should be able to answer:

1. Why is the terrain shaped this way?
2. Why is this ecology here?
3. Why was this site chosen for human use?
4. Why is the architecture shaped this way?
5. Why is this route safe/dangerous/useful?
6. Why did this location end up in its current state?

If the answer is merely "the generator selected it," the content has failed.

## Generation hierarchy

World generation should proceed from large causes toward local details.

```text
planetary physics
-> global climate / geology
-> regional process
-> terrain structure
-> ecology / resource distribution
-> human use case
-> site selection
-> settlement / POI topology
-> current state / occupants
-> local dressing / narrative evidence
```

The generator should not start with a building and then search for somewhere to place it.

## Identity invariants

Each world/archetype requires a small number of traits that procedural generation is not allowed to erase.

Examples:

### Khepri invariants
- impact/collapse geometry dominates;
- broad emptiness between major structures;
- human occupation is recessed or buried;
- anomaly effects stay localized;
- no generic surface-water logic.

### Pelagos invariants
- horizontal/layered biological silhouettes;
- atmospheric depth affects visibility;
- wind/moisture shape both ecology and construction;
- ship corridors exist through biological layers;
- no terrestrial forest horizon.

### Nadir-Tau invariants
- starward/nightward direction always matters;
- infrastructure follows thermal bands;
- ecology responds to the fixed gradient;
- the same site reads differently depending on viewing direction.

### Vitria invariants
- terrain reveals prevailing wind direction;
- lee/windward distinction affects architecture and traversal;
- severe weather has spatial/gameplay consequences;
- mineral identity comes from layering/erosion, not random crystals.

### Thalassa invariants
- stable land is scarce and vertical;
- coast/ocean geometry drives settlement form;
- marine logistics matter;
- open water remains meaningful negative space.

### Eden-9 invariants
- familiarity is deliberate;
- mature ecology is preserved rather than erased by settlement;
- human infrastructure is future-alien and ecologically integrated;
- broad civilian habitation feels plausible rather than survival-driven.

## What may repeat globally

Global reuse is acceptable when it represents shared civilization or gameplay language.

Examples:

- common docking standard;
- cargo container family;
- pressure door interface;
- faction signage;
- emergency symbols;
- modular reactor family;
- maintenance robots;
- ship components;
- standardized beacon protocol;
- UI/holographic conventions;
- common medical/security equipment.

These should function like recurring industrial standards, not repeated locations.

## What may repeat within a world

Within one world, recurring motifs help establish identity.

Examples:

- Khepri: crater-wall pressure galleries and buried service shafts;
- Pelagos: beacon towers and storm-braced connectors;
- Vitria: lee-side hangars and sacrificial abrasion skins;
- Nadir-Tau: paired hot-side/cold-side thermal structures;
- Thalassa: cliff anchors and vertical cargo lifts;
- Eden-9: ecological transit corridors and integrated civic habitat shells.

The rule is **motif repetition, not layout duplication**.

## What must vary

The following should vary even when two POIs share purpose:

- approach direction;
- topology;
- elevation changes;
- relation to terrain;
- access points;
- circulation path;
- exterior/interior sequence;
- damage state;
- occupant history;
- hazard placement;
- usable cover;
- views and landmark relationship;
- loot/resource rationale;
- alternate traversal routes.

Two mining sites may share machinery standards without sharing room order, corpse placement, terminal text, or encounter rhythm.

## POI generation model

A useful POI should be assembled from several independent-but-constrained dimensions.

### 1. Purpose

Examples:
- mining;
- research;
- agriculture;
- logistics;
- habitation;
- security;
- power generation;
- atmospheric observation;
- salvage;
- smuggling;
- military;
- abandoned infrastructure.

### 2. Site reason

Why here?

Examples:
- mineral seam;
- sheltered lee zone;
- stable crater shelf;
- thermal sweet spot;
- deep-water access;
- river junction;
- natural cavern;
- sensor horizon;
- ecological resource;
- old transport route.

### 3. Construction generation

The construction solution depends on:

- world conditions;
- faction;
- technology generation;
- age;
- available local material;
- expected lifetime;
- budget/importance;
- whether the site grew organically or was master-planned.

### 4. History state

Examples:
- functioning;
- expanded;
- partially abandoned;
- storm damaged;
- structurally failing;
- occupied by another faction;
- repurposed;
- excavated further;
- emergency-sealed;
- overgrown/reclaimed where ecology permits.

### 5. Current use

Current occupants should make sense relative to the site.

A pirate group does not magically generate a pirate base. They occupy, modify, exploit, or build something for a reason.

## Narrative generation

Environmental storytelling should derive from state changes rather than random props.

Example:

```text
Vitria mineral survey station
-> built behind fin because of wind
-> expanded after rich seam found
-> severe storm damaged exposed processing line
-> company abandoned site
-> smugglers reopen protected hangar
-> current player encounter
```

Every visible clue can then derive from that chain:

- damaged windward equipment;
- abandoned corporate machinery;
- patched smuggler power feeds;
- inaccessible old work areas;
- new hidden cargo route.

This produces narrative coherence without requiring a bespoke quest for every location.

## Procedural architecture rule

Do not choose architecture independently of terrain.

Generation should prefer:

```text
terrain opportunity
-> site topology
-> structural response
-> modular architecture
```

not:

```text
prefab building
-> flatten terrain
-> place building
```

## Route generation

Procedural environments must consider ship, ground, and on-foot movement separately.

Each significant region should define some combination of:

- safe ship approach;
- risky shortcut;
- hidden approach;
- ground route;
- interior route;
- maintenance route;
- emergency route;
- environmental route that changes with weather/time/state.

Not every site needs every route, but route logic should be intentional.

## Landmark hierarchy

Generated worlds need visual hierarchy.

Use three scales:

### Planet/region scale
Features visible from great distance and useful for orientation.

### Encounter scale
Features guiding the player toward routes, settlements, hazards, or discoveries.

### Human scale
Details supporting close exploration and environmental storytelling.

Randomly distributing equally important objects destroys hierarchy.

## Density rules

More content is not automatically better.

Use deliberate quiet zones to:

- establish scale;
- make landmarks meaningful;
- allow weather/geology to dominate;
- create anticipation;
- preserve visual identity.

Khepri especially requires large empty intervals. Pelagos may be biologically dense but still needs visual clearings. Thalassa requires open ocean. Eden-9 needs undeveloped wilderness around mature settlement.

## Procedural novelty budget

Every generated region should contain:

- familiar world motifs;
- one or more variations on those motifs;
- occasionally a genuinely rare feature.

Rare features lose meaning if every region contains one.

Suggested conceptual distribution:

```text
common structural language: frequent
regional variants: regular
unusual combinations: uncommon
unique landmarks/anomalies: rare
```

Exact percentages should be determined later through playtesting rather than guessed now.

## Cross-world reuse test

Before approving a generated asset/module, ask:

1. Could this appear unchanged on another benchmark world?
2. If yes, is it a genuinely standardized human technology?
3. If not, what world-specific adaptation is missing?

If the answer to #2 is no, the asset should be adapted or rejected.

## Duplicate-content test

Two generated locations fail if a player can predict:

- room sequence;
- enemy positions;
- corpse positions;
- terminal story;
- loot room;
- key location;
- entry/exit route;
- major encounter timing;

because they have seen the same POI elsewhere.

Repeated industrial components are acceptable. Repeated authored experience is not.

## World identity scorecard

For any generated region, score whether the following are visible without reading lore text:

- planetary physics;
- dominant geological/climatic process;
- ecological adaptation if applicable;
- human environmental adaptation;
- local history/state;
- route logic;
- world-specific silhouette.

A region should communicate several of these visually before the player opens a terminal.

## Procedural generation doctrine

> Procedural generation is a constrained authoring system, not a substitute for authorship.

The system should multiply coherent authored rules rather than multiply arbitrary combinations.