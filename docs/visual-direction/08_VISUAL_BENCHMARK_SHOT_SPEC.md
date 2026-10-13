# Visual Benchmark Shot Specification

Status: project-wide visual validation standard

## Purpose

The six reference worlds are not validated by one attractive hero image. Each world must remain identifiable and coherent across a repeatable set of views that stress terrain, atmosphere, settlement logic, traversal, and environmental state.

This document defines the fixed benchmark shots to use for every world concept before it is treated as visually locked.

## General rules

All worlds should be evaluated with comparable framing and intent.

- use the same broad camera categories for every world;
- keep UI absent unless a later implementation test specifically needs it;
- include at least one neutral-light or reduced-color test where practical;
- do not hide weak terrain or architecture behind extreme fog, bloom, grading, or cinematic depth of field;
- include a ship or human-scale reference in at least one shot;
- show the environment doing something, not only posing beautifully;
- benchmark images are design evidence, not marketing art.

## Shot A — planetary / long-range identity

Goal: test whether the world has a recognizable large-scale structure.

The frame should answer:

- what dominates the horizon?
- what large geological/climatic/ecological process shaped this place?
- can the world be recognized before individual props are visible?

Typical framing:

- high-altitude approach, orbital-edge approximation, or very distant surface vista;
- minimal foreground clutter;
- one or two dominant planetary-scale forms.

Failure condition: the world reads as a generic rocky, forested, snowy, or coastal planet until close detail is added.

## Shot B — ship-scale traversal

Goal: test whether terrain and environment create meaningful routes for a spacecraft.

Include:

- a ship for scale;
- at least one obvious route choice;
- terrain or environmental structure that affects how the route is flown;
- enough surrounding space to understand why the route exists.

Questions:

- does the environment invite low-altitude flight?
- is there more than one plausible route?
- can terrain/weather/ecology create risk, shelter, concealment, or navigation?

Failure condition: the ship could be composited over any generic landscape without changing the image's logic.

## Shot C — ground-level environment

Goal: prove that the world's identity survives at human scale.

Show:

- terrain/material detail;
- local ecological or geological motifs;
- human-scale visibility conditions;
- a path, route, shelter, or local environmental interaction.

The shot should not depend on a skyline or giant landmark to remain recognizable.

Failure condition: ground level collapses into ordinary rocks, ordinary forest, ordinary snowfield, ordinary beach, or arbitrary decorative alien props.

## Shot D — human settlement / POI exterior

Goal: test the future-human architecture doctrine and world-specific adaptation.

The settlement must visibly respond to:

- local geology;
- climate/weather;
- atmosphere/pressure;
- ecology or water where applicable;
- logistics;
- ship access;
- long-term human use.

Questions:

- why is the settlement here?
- why is it shaped this way?
- what environmental problem does its architecture solve?
- does it look culturally and technologically future-human rather than merely contemporary with sci-fi surface detail?
- does it integrate with nature where conditions permit rather than simply dominate or erase it?

Failure condition: the POI could be transplanted unchanged to another reference world.

## Shot E — environmental event / hostile state

Goal: test the world's dynamic identity.

This is not required to be a conventional weather event. It may instead show the world's defining environmental stressor.

Examples:

- Khepri: strongest localized anomaly zone / deep-shadow collapse sector;
- Pelagos: electrical storm, dense fog layer, or atmospheric biological movement;
- Vitria: incoming storm wall or front impact;
- Nadir-Tau: crossing toward starward heat or nightward cold extreme;
- Thalassa: severe ocean storm / caldera surge / cloud-bound approach;
- Eden-9: ordinary mature weather such as a frontal rainstorm, seasonal flood, or mountain storm rather than exotic catastrophe.

Questions:

- does the event alter traversal and decision-making?
- does architecture react to it?
- does the scene still look like the same world rather than a generic weather preset?

## Shot F — reduced-information identity test

Goal: determine whether identity depends too strongly on color grading or decorative detail.

Create at least one of:

- grayscale version;
- silhouette study;
- reduced saturation study;
- fog-free/neutral-light study where relevant.

A world should retain recognizable structural identity wherever its concept claims structural alienness.

Eden-9 is allowed to score lower here because familiarity is part of its role, but its settlement structure and geography should still remain coherent.

## World-specific benchmark emphasis

### Khepri

Mandatory emphasis:

- enormous crater/basin geometry;
- fracture/collapse routes;
- localized anomaly deformation without fantasy fluid or glowing corruption;
- recessed/subsurface human infrastructure.

### Pelagos

Mandatory emphasis:

- horizontal/suspended biological structure;
- strong atmospheric layering;
- alien ecology recognizable without emissive color;
- elevated/sheltered human architecture.

### Vitria

Mandatory emphasis:

- strongly aligned wind-carved geology;
- visible lee/windward difference;
- approaching storm wall;
- terrain shelter affecting route and architecture.

### Nadir-Tau

Mandatory emphasis:

- persistent directionality toward starward and nightward extremes;
- permanent low-star geometry;
- settlement extending along thermal/climate bands;
- one frame showing environmental transition across the gradient.

### Thalassa

Mandatory emphasis:

- large open-water negative space;
- steep volcanic/tectonic vertical landforms;
- sea arches/caldera/cliff routes;
- architecture attached to or suspended from geology rather than beachside sprawl.

### Eden-9

Mandatory emphasis:

- genuinely familiar and comfortable natural systems;
- mature future-human settlement structure;
- ecological integration;
- low visual hostility;
- enough wilderness and landscape continuity that the planet does not become one continuous city.

## Validation package

A world is visually ready for implementation research when it has:

1. Shot A — long-range identity.
2. Shot B — ship-scale traversal.
3. Shot C — ground-level environment.
4. Shot D — human settlement/POI.
5. Shot E — environmental event or stress state.
6. Shot F — reduced-information identity test.
7. completed visual scorecard.
8. documented failure notes and any unresolved contradictions.

## Decision rule

Do not select an implementation target because its hero image is the most attractive.

Select it because its identity survives all benchmark views and because its defining features translate into concrete engine-capability questions.
