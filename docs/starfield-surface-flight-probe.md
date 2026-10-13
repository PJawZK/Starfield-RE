# Surface Flight Capability Probe

Status: planned P0 experiment

## Objective

Determine whether Starfield's existing player-ship flight system can be made to operate as a practical low-altitude planetary/lunar vehicle inside a surface worldspace.

This is a capability probe, not a production flight mod.

The experiment should answer specific engine questions with evidence and avoid accumulating unrelated gameplay changes.

## Scope

Target environment: a barren moon or similarly simple surface worldspace.

Initial target behavior:

```text
enter ship
 -> take off
 -> manual low-altitude flight
 -> terrain collision
 -> fire ship weapons
 -> cross terrain/cell boundaries
 -> descend
 -> land
```

Excluded from this phase:

- seamless orbit-to-surface travel
- surface-to-orbit travel
- atmospheric aerodynamics
- realistic orbital mechanics
- supercruise
- large combat rebalance
- ship-builder changes
- production AI behavior
- alien-world environmental work

## Why a barren moon

A barren moon minimizes variables that could obscure the flight experiment:

- no atmosphere requirement
- limited weather
- limited vegetation
- limited fauna
- clear terrain silhouettes
- fewer ecological systems competing for performance

If flight cannot be made stable in this environment, adding atmospheric and biosphere complexity is premature.

## Required baseline capture

Before modifying runtime behavior, record:

- Steam Starfield version
- `Starfield.exe` SHA-256
- executable file version
- SFSE version
- Address Library version, if used
- CommonLibSF commit/tag
- Creation Kit version
- SF1Edit/xEdit version
- Windows version
- compiler version
- REA version/commit
- Ghidra/IDA/Hopper provider and version
- selected test save identifier
- selected test worldspace/cell

All reverse-engineering notes and offsets must be tied to this baseline.

## Research questions

### Ship lifecycle

1. What runtime object represents the player's ship exterior?
2. What object represents the pilot-controlled flight state?
3. What state changes when the player sits in the pilot seat?
4. What creates/destroys or enables/disables the exterior ship representation?
5. How is the interior cell linked to the exterior representation?
6. Which state controls whether the player may leave the pilot seat?

### Flight-mode gating

7. Where is normal ship flight permitted or rejected based on worldspace/location?
8. Is surface flight blocked by an explicit condition, missing setup, absent physics object, camera state, or broader worldspace assumption?
9. Can the normal ship flight controller be initialized while a surface worldspace is active?
10. Does the controller assume zero-gravity/orbital-space data that does not exist on a surface?

### Physics/collision

11. Does the ship collision shape interact with terrain geometry?
12. Does it interact with statics/buildings?
13. Does gravity affect the ship when the flight controller is active?
14. Is ship-ground contact represented by the normal landing state or another mechanism?
15. What happens when the ship impacts terrain at speed?

### Streaming

16. How fast can terrain/cells stream while the player ship moves?
17. Do loaded-cell assumptions depend on player actor position, ship exterior position, or another anchor?
18. Can the streaming anchor be moved with the controlled ship?
19. What occurs at the edge of the generated landing region?
20. Can adjacent terrain be loaded indefinitely, or is the region fundamentally bounded?

### Combat

21. Can ship weapons fire while the surface worldspace is active?
22. Do projectiles collide with terrain and statics correctly?
23. Can surface references receive ship-weapon damage?
24. Can ship-targeting logic operate against surface references or surface-positioned ships?

### Camera/input/UI

25. Does cockpit view work at surface altitude?
26. Does third-person ship view work?
27. Are flight controls routed normally?
28. Do HUD and targeting systems depend on orbital worldspace state?

### Save/load and failure recovery

29. Can the game save safely while the experimental flight state is active?
30. Can such a save reload safely?
31. If not, can saving be blocked while the probe is active?
32. Can the experiment return the game to vanilla state without requiring a restart?

## Investigation order

The order matters. Do not begin by patching arbitrary flight restrictions.

### Phase 0 — fingerprint and observation

- establish baseline
- capture logs around normal orbital flight
- capture logs around normal surface landing/disembarkation
- identify relevant runtime objects/types/events

No behavioral patches.

### Phase 1 — lifecycle mapping

Use REA/Ghidra/CommonLibSF evidence to map:

- pilot-seat activation
- flight-controller initialization
- exterior ship activation
- worldspace checks
- camera/input setup

Output: lifecycle diagram with evidence references.

### Phase 2 — minimal activation

Attempt the smallest possible change that leaves the normal ship controller active or initializes it in a surface worldspace.

The goal is not movement yet. Success is an observable, stable flight-state activation without immediate crash or forced transition.

### Phase 3 — controlled motion

Enable minimal translation/rotation.

Test at very low speed.

Capture:

- ship transform
- player transform
- streaming-anchor transform if known
- active worldspace/cell
- flight-state enum/flags
- collision contacts where available

### Phase 4 — collision

Test in order:

1. level terrain
2. gentle slope
3. large rock/static
4. building/static
5. steep crater wall

Do not test high-speed impacts until basic contact is understood.

### Phase 5 — streaming

Fly a repeatable straight path at increasing speed tiers.

Suggested tiers are relative rather than fixed initially:

- walking-equivalent
- ground-vehicle-equivalent
- low ship speed
- normal combat ship speed

Measure:

- frame-time spikes
- terrain pop-in
- unloaded collision
- cell transition behavior
- memory growth
- invalid references

### Phase 6 — weapons

Enable one simple ship weapon.

Verify:

- projectile creation
- terrain collision
- static collision
- damage event
- no worldspace-state corruption

### Phase 7 — landing

Determine whether normal Starfield landing state can be entered from manual low-altitude flight.

If not, investigate a controlled surface-flight landing state separately.

## Instrumentation requirements

Prefer structured logs over ad-hoc text.

Suggested JSONL event classes:

```json
{"event":"flight_state","time":0.0,"state":"...","worldspace":"...","cell":"..."}
{"event":"ship_transform","time":0.1,"pos":[0,0,0],"rot":[0,0,0],"velocity":[0,0,0]}
{"event":"stream_state","time":0.1,"loadedCells":0,"anchor":[0,0,0]}
{"event":"collision","time":1.2,"other":"terrain","relativeSpeed":0.0}
{"event":"weapon_fire","time":2.5,"weapon":"...","origin":[0,0,0]}
{"event":"probe_fault","time":3.1,"stage":"collision","code":"..."}
```

Exact fields depend on what is accessible.

## Safety/containment rules

The probe must minimize save corruption and persistent changes.

- Use a dedicated test profile/save.
- Prefer runtime-only changes for early experiments.
- Do not write permanent quest/progression state unless required.
- Include an emergency disable path for experimental hooks.
- Refuse unsupported runtime versions.
- Avoid patching unrelated engine systems.
- Log every active experimental patch/hook on startup.
- Do not silently continue after signature mismatch.

## Success levels

### S0 — research baseline

- exact runtime fingerprint recorded
- normal ship lifecycle partially mapped
- candidate flight/worldspace gates identified

### S1 — surface flight state

- normal or equivalent ship flight state active in surface worldspace
- no immediate crash/forced travel
- camera/input remain controllable

### S2 — practical movement

- player can translate and rotate ship over terrain for at least five minutes
- terrain/world geometry remains present
- no progressive state corruption observed

### S3 — usable planetary flight

- collision works
- terrain streaming is usable
- weapons function
- player can return to a stable landed state

### S4 — prototype-ready

- repeated test runs succeed
- save/profile containment established
- known limitations documented
- instrumentation is sufficient for playtest diagnosis

S3 is the minimum threshold for the planned Crater Run vertical slice.

## Failure classification

Every failed experiment should be classified rather than merely described as "doesn't work".

- `GATE` — explicit game-state/worldspace restriction
- `INIT` — required subsystem was not initialized
- `PHYSICS` — controller/collision/gravity incompatibility
- `STREAM` — world/cell loading cannot follow the ship
- `CAMERA` — camera/input assumptions fail
- `UI` — HUD/targeting assumptions fail
- `INTERIOR` — interior/exterior linkage breaks
- `SAVE` — persistence is unsafe
- `PERF` — technically functional but unusable performance
- `VERSION` — runtime-specific hook/signature failure
- `UNKNOWN` — insufficient evidence

This classification determines the next reverse-engineering question.

## Stop conditions

Pause implementation and return to research if any of the following occurs:

- repeated non-deterministic crashes before movement is established
- evidence of save corruption
- terrain collision disappears outside the initial region
- streaming cannot follow the ship even when the correct anchor is identified
- normal flight initialization mutates unrelated quest/world state
- a hook requires broad engine patching before its purpose is understood

## First playtest script

Once S2 is reached, the player test should remain intentionally boring:

1. Load dedicated moon test save.
2. Enter pilot seat.
3. Activate surface-flight probe.
4. Hover/hold position for 30 seconds.
5. Fly straight for 60 seconds at low speed.
6. Turn 180 degrees.
7. Return to start.
8. Fly toward a crater wall.
9. Test gentle terrain contact.
10. Land/disable probe.
11. Exit ship.
12. Save only if save safety has already been established.

No combat and no showcase content until this passes reliably.

## Advancement criterion

Do not begin the Crater Run showcase until the probe reaches S3.

Do not begin serious surface-to-orbit work until the probe reaches at least S2 and the streaming model is understood.
