# Visual World Scorecard

Status: project-wide comparison rubric

## Purpose

This scorecard is used after the fixed benchmark shot set has been created for a world. Its purpose is to expose weak identity, overreliance on color/effects, generic settlement placement, and environments that look good but do not produce distinctive gameplay.

Scores are deliberately simple. The point is not mathematical precision; the point is forcing explicit comparison.

## Scoring scale

Use 0–5 for each criterion.

- `0` — absent / failed
- `1` — barely present
- `2` — weak or inconsistent
- `3` — functional but ordinary
- `4` — strong and clearly intentional
- `5` — defining / immediately recognizable

Include one or two sentences of evidence for every score of 0–2 and every score of 5.

## Core criteria

| Criterion | Question |
|---|---|
| Silhouette identity | Can the world be recognized from large forms and horizon geometry alone? |
| Ground-level identity | Does the world remain distinctive at human scale? |
| Atmospheric identity | Does atmosphere/weather materially shape the world's look and behavior? |
| Geology/ecology coherence | Do visible forms appear to arise from the world's physical/ecological rules? |
| Material plausibility | Do liquids, ices, dust, minerals and surface states make physical sense for the environment? |
| Human adaptation | Does architecture visibly respond to the specific world rather than use a generic footprint? |
| Future-human unfamiliarity | Does human technology feel culturally/structurally ahead of the present while remaining engineering-readable? |
| Ecological integration | Where conditions permit, does human construction work with natural systems rather than simply erase them? |
| Ship-route readability | Can the player visually infer useful, risky, sheltered or interesting flight routes? |
| Dynamic-state identity | Do storms/anomalies/climate transitions alter the world in a world-specific way? |
| Grayscale / reduced-color resilience | Does identity survive without relying mainly on palette? |
| Procedural resilience | Can the world's rules plausibly produce many varied locations without collapsing into repetition? |
| POI transplant resistance | Would moving a POI unchanged to another reference world obviously look wrong? |
| Earth-familiarity calibration | Is the degree of familiarity appropriate for this world's intended role? |
| Memorability | After seeing all six worlds, is this one easy to describe without mentioning only color? |

Maximum core score: 75.

## Hard-fail checks

These are not averaged away by a high numerical score.

Mark each `PASS`, `WARN`, or `FAIL`.

### H1 — color dependency

Would the core identity disappear if the scene were desaturated?

### H2 — generic terrain dependency

Could the same terrain plausibly appear on several other benchmark worlds with only material changes?

### H3 — generic POI

Could the primary human settlement be moved to another world without structural redesign?

### H4 — decorative alienness

Is the world relying on glowing plants, crystals, colored fog, arbitrary floating rocks, or other shorthand rather than process-driven structure?

### H5 — physical contradiction

Does a defining visual feature conflict with the chosen pressure, temperature, atmosphere, gravity, fluid state, geology or ecology without a documented lore/technology reason?

### H6 — gameplay disconnect

Does the visual concept fail to change traversal, navigation, combat, shelter, discovery or settlement placement?

### H7 — future-human regression

Does human construction look primarily like a present-day industrial park, town, airport, road network or resort with sci-fi surface dressing?

### H8 — nature erasure

On a benign or life-rich world, does advanced human settlement still default to flattening terrain and replacing ecosystems rather than integrating with them?

## World-role calibration

Not every criterion should target the same aesthetic extreme.

### Khepri

Expected strengths:

- silhouette identity;
- geology coherence;
- ship-route readability;
- POI transplant resistance.

Alien ecology is intentionally irrelevant. Its anomaly layer should remain restrained.

### Pelagos

Expected strengths:

- atmospheric identity;
- ecological coherence;
- ground-level identity;
- grayscale structural alienness;
- ship navigation through biological/atmospheric layers.

### Vitria

Expected strengths:

- geology/weather coherence;
- directional silhouette;
- dynamic-state identity;
- flight/weather interaction;
- terrain-shelter logic.

### Nadir-Tau

Expected strengths:

- planetary directionality;
- climate-gradient coherence;
- human adaptation;
- traversal across environmental bands.

### Thalassa

Expected strengths:

- vertical coastal geology;
- open-water composition;
- cliff/caldera architecture;
- ship approach variety.

### Eden-9

Expected strengths:

- human architectural maturity;
- ecological integration;
- settlement/wilderness coexistence;
- intentional familiarity.

Eden-9 is not penalized for being Earth-like when that familiarity is coherent and uncommon across the wider game.

## Comparison table

Fill after completing the benchmark-shot package.

| Criterion | Khepri | Pelagos | Vitria | Nadir-Tau | Thalassa | Eden-9 |
|---|---:|---:|---:|---:|---:|---:|
| Silhouette identity | — | — | — | — | — | — |
| Ground-level identity | — | — | — | — | — | — |
| Atmospheric identity | — | — | — | — | — | — |
| Geology/ecology coherence | — | — | — | — | — | — |
| Material plausibility | — | — | — | — | — | — |
| Human adaptation | — | — | — | — | — | — |
| Future-human unfamiliarity | — | — | — | — | — | — |
| Ecological integration | — | — | — | — | — | — |
| Ship-route readability | — | — | — | — | — | — |
| Dynamic-state identity | — | — | — | — | — | — |
| Reduced-color resilience | — | — | — | — | — | — |
| Procedural resilience | — | — | — | — | — | — |
| POI transplant resistance | — | — | — | — | — | — |
| Earth-familiarity calibration | — | — | — | — | — | — |
| Memorability | — | — | — | — | — | — |
| **Total / 75** | — | — | — | — | — | — |

## Pairwise confusion test

For every pair of worlds, ask:

> If color, UI and names were removed, could a player plausibly confuse these worlds from a ship-approach image or ground-level image?

Priority comparisons:

- Khepri vs Vitria — both sparse and geological;
- Pelagos vs Eden-9 — both life-rich;
- Thalassa vs Eden-9 — both can contain familiar water and vegetation;
- Vitria vs Nadir-Tau — both may use strong directional landscapes;
- Pelagos vs Thalassa — both may use high humidity, storms and unusual life.

If confusion remains high, revise structural rules rather than simply changing colors.

## Implementation-readiness gate

A benchmark world is ready to become a technical implementation target when:

- all six benchmark shots exist;
- there are no unresolved hard `FAIL`s;
- silhouette, coherence, human adaptation and ship-route readability are each at least 4/5;
- any intentional low score is explained by the world's role;
- the defining visual features can be translated into a finite list of Starfield engine-capability questions.

The purpose of this gate is not to demand perfection. It is to ensure technical work has a clear visual target and a reason for each requested engine capability.
