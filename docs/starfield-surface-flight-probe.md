# Surface Flight Capability Probe

Status: planned P0 experiment, updated 2026-10-13

## Objective

Determine the lowest-risk architecture for practical low-altitude ship flight over a planetary or lunar surface in Starfield.

The probe must no longer assume that only one implementation path is valid. Current 2026 modding evidence shows that the problem separates into at least three layers:

1. **surface locomotion** — moving an aerial vehicle over generated planetary terrain;
2. **surface/orbit state transition** — moving between planetary surface and orbital flight states;
3. **global planetary presentation** — representing the planet, atmosphere, clouds, biomes, oceans, and entry sequence at large scale.

The first implementation goal is layer 1 on a barren moon. Layers 2 and 3 are later work.

This is a capability probe, not a production flight mod.

## Primary test world

**Bel I-a** is the first implementation laboratory and the current mapping target for the Khepri archetype.

Reasons:

- airless;
- very low gravity (~0.11 g in current public planet data);
- waterless;
- heavily cratered surface;
- minimal biological/weather complexity;
- no major city or central quest-hub dependency;
- strong match for the Khepri flight-first concept.

The test save should use an intentionally unimportant landing area on Bel I-a rather than a handcrafted quest location.

## Current external evidence — October 2026

The probe strategy must account for capabilities already demonstrated by the modding community.

### Planetary vehicle flight exists

Existing vehicle mods have demonstrated fast above-surface traversal by modifying the planetary vehicle controller, including removal of vertical limits and effectively aircraft-like motion. This does **not** prove that the normal player-ship flight controller works on a surface, but it proves that Creation Engine surface worldspaces can support a controllable moving object above terrain at substantially higher-than-on-foot traversal speeds.

Implication: a vehicle-controller/proxy architecture is a legitimate fallback or even primary prototype path.

### Surface/orbit transitions are already being manipulated

2026 SFSE mods demonstrate that takeoff and landing flow can be intercepted and altered. Seamless Planet Takeoffs removes the visible takeoff loading screen and relocates the ship into orbital space; Immersive Landing allows physically approaching planetary landing markers before invoking Starfield's existing landing system.

Implication: the surface/orbit boundary is not an untouchable black box. It is still a separate problem from low-altitude surface flight, and should remain outside the first probe.

### Full seamless descent has now been demonstrated externally

A separate unreleased 2026 project has publicly demonstrated manual/autopilot orbit-to-ground descent with rebuilt 3D planetary rendering, atmospheric layers, climate-driven clouds, oceans, lighting, and landing anywhere. Public descriptions state that this required substantial reimplementation of planetary rendering rather than merely unlocking a vanilla switch.

Implication: truly seamless planetary descent appears technically possible, but should not be conflated with the much smaller Khepri surface-flight experiment. It also reinforces the value of preserving a future architecture boundary between low-altitude flight and global-planet rendering.

## Probe architectures

Both branches should be evaluated before committing to production architecture.

### Branch A — native spaceship-controller surface flight

Goal: determine whether the normal player ship exterior/controller can remain active or be initialized while a surface worldspace is active.

Advantages if successful:

- native ship handling;
- native ship weapons;
- native cockpit/third-person camera;
- native ship stats and builder compatibility;
- potentially cleaner transition to orbital flight later.

Risks:

- hard worldspace/state gating;
- assumptions about orbital SpaceCells;
- interior/exterior linkage;
- streaming-anchor mismatch;
- HUD/targeting assumptions;
- landing-state coupling.

### Branch B — surface-flight proxy using planetary vehicle systems

Goal: prove the gameplay loop using a surface-worldspace-native controller while visually and logically representing the player's ship.

Possible architecture:

```text
player ship definition / appearance / stats
            |
            v
surface-flight proxy actor or vehicle
            |
            +--> terrain/worldspace-native movement
            +--> custom flight camera/input layer
            +--> mapped ship thrust/handling values
            +--> mapped weapons where feasible
            |
            v
landed ship / transition back to normal ship state
```

This branch is acceptable for a prototype even if the underlying controller is not the vanilla spaceship controller.

Advantages:

- surface worldspace compatibility is more plausible;
- terrain collision and streaming behavior may already be solved by the vehicle subsystem;
- easier containment from orbital-space assumptions;
- may permit rapid Crater Run proof-of-concept.

Risks:

- cockpit integration may require custom work;
- ship weapon systems may need proxying;
- ship-builder geometry/physics synchronization;
- landing/interior transitions;
- possible vehicle height/speed caps or controller assumptions;
- must avoid feeling like a reskinned rover.

## Initial target behavior

```text
enter ship
 -> activate surface-flight mode
 -> manual low-altitude flight
 -> terrain/static collision
 -> cross cell boundaries
 -> descend
 -> return to landed state
```

Weapons are deliberately moved one stage later than basic movement/streaming.

Excluded from this phase:

- seamless orbit-to-surface travel;
- surface-to-orbit travel;
- atmospheric aerodynamics;
- realistic orbital mechanics;
- supercruise;
- large combat rebalance;
- ship-builder changes;
- production AI behavior;
- alien-world environmental work.

## Why a barren moon

A barren moon minimizes variables that could obscure the flight experiment:

- no atmosphere requirement;
- no normal weather dependency;
- limited vegetation/fauna;
- clear terrain silhouettes;
- fewer ecological systems competing for performance;
- black-sky lighting makes visual discontinuities easier to diagnose.

If flight cannot be made stable here, atmospheric and biosphere complexity is premature.

## Required baseline capture

Before modifying runtime behavior, record:

- Steam Starfield version;
- `Starfield.exe` SHA-256;
- executable file version;
- SFSE version;
- Address Library version;
- CommonLibSF commit/tag;
- Creation Kit version;
- SF1Edit/xEdit version;
- Windows/Proton environment as applicable;
- compiler version;
- REA version/commit;
- disassembler/decompiler and version;
- selected test save identifier;
- Bel I-a planet/location/worldspace identifiers;
- selected landing area/cell.

All reverse-engineering notes and offsets must be tied to this baseline.

## Record-level discovery before runtime patching

Before hooking flight code, identify and record the data chain for Bel I-a:

```text
star system
 -> planet/moon record
 -> planet surface location
 -> biome assignments / BIOM map
 -> generated landing area
 -> surface worldspace
 -> exterior cells
 -> landed ship reference
```

Also capture:

- planet data / PNDT relationship;
- associated surface and orbit locations;
- worldspace pointer/overlay data;
- biome identifiers;
- content-generation settings;
- landing marker/reference classes;
- ship landing-pad/landing-site markers where present.

The first goal is evidence, not editing.

## Research questions

### Ship lifecycle

1. What runtime object represents the player's landed ship exterior?
2. What runtime object represents the orbital player ship exterior?
3. Are these the same object/state or separate representations?
4. What object represents pilot-controlled flight state?
5. What changes when the player sits in the pilot seat on the surface versus in orbit?
6. How is the interior cell linked to the exterior representation?
7. Which state controls whether the player may leave the pilot seat?

### Flight-mode gating

8. Where is normal spaceship flight permitted or rejected based on worldspace/location?
9. Is surface flight blocked by an explicit condition, missing initialization, absent physics state, camera mode, or broader SpaceCell assumption?
10. Can the normal ship controller be initialized while a surface worldspace is active?
11. If not, which responsibilities can be cleanly delegated to the planetary vehicle controller?

### Vehicle-controller branch

12. What class/controller owns planetary vehicle translation, hover/vertical cap, and collision?
13. What limits vertical movement?
14. What controls maximum horizontal speed and acceleration?
15. What object anchors streaming while the player drives a vehicle?
16. Can the vehicle actor/model be replaced or hidden while a ship proxy is rendered?
17. Can camera/input be overridden without losing surface streaming/collision behavior?

### Physics/collision

18. Does the ship/proxy collision shape interact with terrain geometry?
19. Does it interact with statics/buildings?
20. How does low Bel I-a gravity affect the chosen controller?
21. What happens on terrain contact at progressively higher speed?
22. Can a stable hover/ground-clearance rule be implemented without fake camera-only motion?

### Streaming

23. How fast can terrain/cells stream while the controlled object moves?
24. Does loaded-cell behavior follow the player actor, vehicle, ship exterior, camera, or another anchor?
25. Can the streaming anchor follow sustained low-altitude flight?
26. What occurs at the practical edge of the currently generated landing region?
27. Is the limitation a hard worldspace bound, streaming budget, coordinate-origin issue, or generation/persistence boundary?
28. Does the new surface-map/vehicle-era engine behavior differ materially from older 2023 assumptions about landing-area limits?

### Combat

29. Can native ship weapons fire in a surface worldspace under Branch A?
30. Under Branch B, can ship weapon definitions be mapped to proxy projectiles without duplicating the entire combat stack?
31. Do projectiles collide with terrain and statics correctly?
32. Can surface references receive damage?
33. Can another flying proxy/NPC target participate in surface combat?

### Camera/input/UI

34. Does native cockpit view work at surface altitude under Branch A?
35. Can a cockpit-like camera be preserved under Branch B while leaving the streaming/vehicle controller intact?
36. Does third-person ship view work?
37. Which flight HUD systems require orbital state?
38. Which HUD elements can be reused independently?

### Save/load and failure recovery

39. Can the game save safely while experimental surface-flight state is active?
40. Can such a save reload safely?
41. If not, can saving be blocked while the probe is active?
42. Can either branch return the game to vanilla landed state without restart?

## Investigation order

### Phase 0 — fingerprint and record map

- establish exact runtime/tool baseline;
- identify Bel I-a planet/surface/orbit/worldspace records;
- capture a clean dedicated save;
- document landed ship references and pilot-seat behavior;
- capture normal orbital flight lifecycle;
- capture normal planetary vehicle lifecycle.

No behavioral patches.

### Phase 1A — native ship lifecycle mapping

Map:

- pilot-seat activation;
- spaceship-controller initialization;
- landed/orbital exterior transition;
- surface-vs-space checks;
- camera/input setup;
- streaming anchor.

### Phase 1B — planetary vehicle lifecycle mapping

Map:

- vehicle activation;
- movement/hover controller;
- vertical limits;
- speed limits;
- collision body;
- camera/input;
- streaming anchor.

The two lifecycle diagrams should be compared before choosing a branch.

### Phase 2 — minimal motion proof

For each viable branch, attempt only enough change to establish controllable movement in Bel I-a surface worldspace.

Success is:

- stable activation;
- translation/rotation;
- no immediate forced transition;
- camera/input controllable;
- terrain remains loaded.

### Phase 3 — collision and hover

Test in order:

1. level terrain;
2. gentle slope;
3. large rock/static;
4. building/static;
5. steep crater wall.

### Phase 4 — streaming

Fly a repeatable straight path at increasing speed tiers:

- rover-equivalent;
- fast ground-vehicle-equivalent;
- low aircraft/ship speed;
- target Crater Run speed.

Measure:

- frame-time spikes;
- terrain pop-in;
- unloaded collision;
- cell transition behavior;
- memory growth;
- invalid references;
- world-origin/precision artifacts.

### Phase 5 — landing-state return

Before weapons, prove that the experiment can reliably return to a normal landed ship/interior state.

### Phase 6 — weapons

Enable one simple forward weapon and verify projectile creation, collision, damage, and state safety.

### Phase 7 — NPC surface-flight target

Only after the player path is stable, test one simple NPC-controlled flying target/proxy.

## Instrumentation requirements

Prefer structured JSONL logs.

Suggested events:

```json
{"event":"controller_branch","branch":"native_ship|vehicle_proxy"}
{"event":"flight_state","time":0.0,"state":"...","worldspace":"...","cell":"..."}
{"event":"controlled_transform","time":0.1,"pos":[0,0,0],"rot":[0,0,0],"velocity":[0,0,0]}
{"event":"stream_state","time":0.1,"loadedCells":0,"anchor":[0,0,0]}
{"event":"collision","time":1.2,"other":"terrain","relativeSpeed":0.0}
{"event":"landing_state","time":2.0,"state":"..."}
{"event":"weapon_fire","time":2.5,"weapon":"...","origin":[0,0,0]}
{"event":"probe_fault","time":3.1,"stage":"streaming","code":"..."}
```

Exact fields depend on what is accessible.

## Safety/containment rules

- Use a dedicated Bel I-a test profile/save.
- Prefer runtime-only changes for early experiments.
- Do not write permanent quest/progression state unless required.
- Include an emergency disable path for experimental hooks.
- Refuse unsupported runtime versions.
- Avoid patching unrelated engine systems.
- Log every active experimental patch/hook on startup.
- Do not silently continue after signature mismatch.
- Do not initially test in New Atlantis, Neon, or other quest-heavy worldspaces.

## Success levels

### S0 — research baseline

- exact runtime fingerprint recorded;
- Bel I-a record/worldspace chain mapped;
- native ship and planetary vehicle lifecycles partially mapped;
- candidate controller branch identified.

### S1 — surface flight state

- chosen controller/proxy active in surface worldspace;
- no immediate crash/forced travel;
- camera/input remain controllable.

### S2 — practical movement

- player can translate and rotate over terrain for at least five minutes;
- terrain/world geometry remains present;
- cell transitions are stable;
- no progressive state corruption observed.

### S3 — usable planetary flight

- collision works;
- target traversal speed is usable;
- player can return to stable landed state;
- one weapon path functions.

### S4 — prototype-ready

- repeated test runs succeed;
- save/profile containment established;
- known limitations documented;
- instrumentation is sufficient for playtest diagnosis;
- one NPC target/proxy can be exercised if needed for Crater Run.

S3 remains the minimum threshold for the planned Crater Run vertical slice.

## Failure classification

- `GATE` — explicit game-state/worldspace restriction;
- `INIT` — required subsystem not initialized;
- `PHYSICS` — controller/collision/gravity incompatibility;
- `STREAM` — world/cell loading cannot follow the controlled object;
- `BOUNDARY` — generated/loaded surface region cannot support the route;
- `CAMERA` — camera/input assumptions fail;
- `UI` — HUD/targeting assumptions fail;
- `INTERIOR` — interior/exterior linkage breaks;
- `PROXY` — vehicle-proxy synchronization fails;
- `SAVE` — persistence is unsafe;
- `PERF` — technically functional but unusable performance;
- `VERSION` — runtime-specific hook/signature failure;
- `UNKNOWN` — insufficient evidence.

## Stop conditions

Pause implementation and return to research if:

- repeated non-deterministic crashes occur before basic movement;
- there is evidence of save corruption;
- terrain collision disappears outside the initial route;
- streaming cannot follow either candidate controller;
- controller activation mutates unrelated quest/world state;
- a hook requires broad engine patching before its purpose is understood.

Failure of Branch A is **not** failure of the surface-flight project if Branch B remains viable.

## First playtest script

Once S2 is reached:

1. Load dedicated Bel I-a test save.
2. Enter/activate surface-flight state.
3. Hold position for 30 seconds.
4. Fly straight for 60 seconds at low speed.
5. Turn 180 degrees.
6. Return to start.
7. Follow a crater rim for 60 seconds.
8. Descend into a crater/fracture route.
9. Test gentle terrain contact.
10. Return to landed state.
11. Exit vehicle/ship.
12. Save only after save safety is established.

No showcase combat until this passes reliably.

## Advancement criterion

Do not begin the Crater Run showcase until the probe reaches S3.

Do not begin serious surface-to-orbit work until the surface controller architecture and streaming model are understood.
