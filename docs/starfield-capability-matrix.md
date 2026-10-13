# Starfield Capability Matrix

Status values:

- `UNKNOWN` — not yet established
- `SUPPORTED` — achievable through stable/ordinary modding interfaces
- `SUPPORTED_NATIVE` — requires SFSE/native extension
- `APPROXIMATION` — achievable convincingly but not as literal engine continuity
- `FRAGILE` — possible but runtime/version sensitive or otherwise risky
- `MANUAL` — primarily Creation Kit/manual authoring
- `BLOCKED` — evidence indicates a hard or impractical engine limitation

Evidence levels:

- `E0` — assumption only
- `E1` — public demonstration or documentation
- `E2` — reproduced locally
- `E3` — reproduced with instrumentation and repeatable procedure
- `E4` — integrated into automated regression coverage

| Area | Capability / question | Status | Evidence | Priority | Acceptance target |
|---|---|---:|---:|---:|---|
| Runtime | Identify exact Steam runtime and executable fingerprint | UNKNOWN | E0 | P0 | Version, SHA-256 and supported SFSE stack recorded |
| Runtime | Automated runtime/version guard | UNKNOWN | E0 | P1 | Experimental native code refuses unsupported runtime safely |
| Ship | Identify player ship exterior runtime object | UNKNOWN | E0 | P0 | Object/type/lifecycle documented |
| Ship | Identify ship interior/exterior relationship | UNKNOWN | E0 | P0 | Relationship and transition lifecycle documented |
| Flight | Activate normal ship flight controller in surface worldspace | UNKNOWN | E0 | P0 | Player can control ship above terrain |
| Flight | Surface-worldspace terrain collision | UNKNOWN | E0 | P0 | Reliable collision without falling through/teleporting |
| Flight | Stable low-altitude flight | UNKNOWN | E0 | P0 | Five-minute flight without state loss/crash |
| Flight | Surface takeoff under player control | UNKNOWN | E0 | P0 | Grounded -> airborne without conventional travel menu |
| Flight | Surface landing under player control | UNKNOWN | E0 | P0 | Airborne -> stable landed state |
| Flight | Ship weapons function near terrain | UNKNOWN | E0 | P0 | Weapons fire/hit correctly without invalid mode transitions |
| Flight | NPC ships function in surface worldspace | UNKNOWN | E0 | P1 | Spawn, navigate and engage near terrain |
| Flight | Surface AI avoids terrain | UNKNOWN | E0 | P1 | No systematic terrain-suicide behavior in test arena |
| Flight | Camera remains valid during surface flight | UNKNOWN | E0 | P0 | Cockpit/third-person camera usable near terrain |
| Flight | Terrain/cell streaming keeps up with ship speed | UNKNOWN | E0 | P0 | Controlled traversal across multiple terrain boundaries |
| Flight | Worldspace boundary behavior understood | UNKNOWN | E0 | P0 | Failure mode and practical limits documented |
| Flight | Save/load while airborne is safe | UNKNOWN | E0 | P1 | Save/load reproduces ship state or is deliberately blocked |
| Flight | Fast travel restrictions coexist with surface flight | UNKNOWN | E0 | P2 | No save/quest corruption from experimental state |
| Transition | Surface -> orbit transition trigger identified | UNKNOWN | E0 | P1 | Engine path/function/state sequence documented |
| Transition | Orbit -> surface transition trigger identified | UNKNOWN | E0 | P1 | Engine path/function/state sequence documented |
| Transition | Heading/orientation can persist across transition | UNKNOWN | E0 | P1 | Visual continuity maintained |
| Transition | Velocity feel can persist across transition | UNKNOWN | E0 | P2 | No obvious dead stop unless intentionally masked |
| Transition | Hidden transition can replace loading/cutscene | UNKNOWN | E1 | P1 | Player-perceived continuous descent/ascent |
| Transition | Literal continuous surface/orbit worldspace | UNKNOWN | E0 | P3 | Research only; not required for project success |
| Space | Physical travel between local orbital destinations | UNKNOWN | E1 | P1 | Destination reachable through flight without map fast-travel |
| Space | Accelerated local travel mode | UNKNOWN | E1 | P2 | Useful travel time without breaking encounters |
| Space | Discoverable hidden spatial POIs | UNKNOWN | E0 | P1 | Signals/objects discoverable through flight/sensors |
| Space | Flyable asteroid tunnels/caverns | UNKNOWN | E0 | P2 | Stable collision, lighting and navigation |
| Space | Asteroid/hollow-body base with hangar ingress | UNKNOWN | E0 | P2 | Ship can approach/enter/land then continue on foot |
| World | Replace/extend biome visual identity | UNKNOWN | E0 | P0 | One showcase biome reads as clearly non-Earth-like |
| World | Modify terrain silhouette substantially | UNKNOWN | E0 | P0 | Terrain differs beyond texture/material substitution |
| World | Custom geological feature distribution | UNKNOWN | E0 | P1 | Repeatable authored/procedural placement path established |
| World | Custom flora morphology | UNKNOWN | E0 | P0 | New flora family with coherent visual language |
| World | Custom fauna morphology/ecology | UNKNOWN | E0 | P1 | New fauna ecosystem can be authored and placed coherently |
| World | Atmosphere/lighting palette control | UNKNOWN | E0 | P0 | Distinctive environment without post-process-only trick |
| World | Unique weather behavior | UNKNOWN | E0 | P1 | Environment-specific weather implemented |
| World | World-specific hazard/traversal mechanic | UNKNOWN | E0 | P1 | Gameplay changes because of environment |
| POI | Prevent obvious repeated vanilla POI selection | UNKNOWN | E0 | P0 | Showcase region avoids duplicate authored layouts |
| POI | Modular location assembly | UNKNOWN | E0 | P1 | Multiple valid layouts from shared module set |
| POI | Runtime/generation-driven location state | UNKNOWN | E0 | P1 | Damage/occupant/history states vary coherently |
| POI | Generated environmental storytelling | UNKNOWN | E0 | P2 | Narrative state is consistent with generated location state |
| POI | Ship-scale surface defenses | UNKNOWN | E0 | P1 | Turrets/defenses engage player ship correctly |
| POI | Ship-accessible hangar | UNKNOWN | E0 | P1 | Fly/land/disembark loop works |
| Tooling | REA can fingerprint/analyze Starfield.exe on Windows | UNKNOWN | E0 | P0 | Repeatable local analysis session established |
| Tooling | Ghidra provider works against selected runtime | UNKNOWN | E0 | P0 | Functions/xrefs/pseudocode retrievable |
| Tooling | Findings stored with binary/version provenance | UNKNOWN | E0 | P0 | Every engine conclusion references runtime fingerprint |
| Tooling | CommonLibSF/SFSE native test plugin builds reproducibly | UNKNOWN | E0 | P0 | Clean build from repo |
| Tooling | Native plugin deploy automation | UNKNOWN | E0 | P1 | One-command dev deployment |
| Tooling | Papyrus compile automation | UNKNOWN | E0 | P1 | Clean script build from source |
| Tooling | SF1Edit/xEdit automation path | UNKNOWN | E0 | P1 | Scripted record inspection/modification demonstrated |
| Tooling | Structured telemetry/logging from native plugin | UNKNOWN | E0 | P1 | JSONL or equivalent runtime events generated |
| Tooling | Automated package/build report | UNKNOWN | E0 | P2 | Dev build emits machine-readable report |

## Priority order

### P0 — establish before production work

1. Runtime/toolchain fingerprint.
2. REA/Ghidra access to `Starfield.exe`.
3. Reproducible SFSE/CommonLibSF test plugin.
4. Player ship object/lifecycle understanding.
5. Surface flight-controller activation.
6. Terrain collision and streaming.
7. Manual takeoff/landing viability.
8. Ship weapons near terrain.
9. First non-Earth biome authoring proof.

### P1 — establish after the first flight proof

- NPC surface flight
- surface combat AI
- transition internals
- ship-accessible POIs
- modular POI architecture
- deployment/telemetry automation
- environmental hazards/weather

### P2/P3 — defer until core viability is proven

- advanced local-space travel
- asteroid tunnel networks
- generated narrative state
- literal continuous planet/orbit worldspace
- advanced flight-model replacement

## Decision rule

A capability should not move from `UNKNOWN` based only on a forum claim, video, or inferred engine behavior.

- Public work may raise evidence to `E1`.
- Local reproduction raises it to `E2`.
- Instrumented, documented reproduction raises it to `E3`.
- Automated regression coverage raises it to `E4`.

Production architecture should preferably depend only on E3/E4 findings for fragile native behavior.
