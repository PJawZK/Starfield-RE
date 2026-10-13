# Starfield-RE

Reverse-engineering notes, capability probes, evidence, and experimental findings for exploring how far Starfield can be pushed beyond its exposed modding interfaces.

This repository is for **research**, not the shipping overhaul mod.

## Current phase

**Capability Lab**

The immediate goals are to establish reproducible evidence for:

- player-ship lifecycle and surface-flight viability
- terrain collision and streaming at ship speeds
- surface/orbit transition behavior
- alien-world authoring limits
- dynamic/less-repetitive location generation
- useful space exploration mechanics

## Repository roles

- `PJawZK/rea_JZ-Fork` — reverse-engineering tooling
- `PJawZK/Starfield-RE` — engine research, evidence, experiments, capability matrix
- `PJawZK/Starfield-Overhaul` — eventual production mod, build system, assets, scripts, and release packaging

## Research rules

Important findings should be tied to an exact Starfield runtime fingerprint and supported by reproducible evidence. Public demonstrations can guide research, but fragile production architecture should depend on locally reproduced and instrumented findings where possible.

See `docs/starfield-overhaul-foundation.md` for the project vision and research architecture.
