# TS-004 — Sensing approach

```
Status:     open
Owner:      TBD
Decides:    an ADR (number allocated when written)
Blocked on: Phase 2 models; Phase 3 hazard analysis
```

## Question

How does the unit measure motion, load and occupancy — and how does the independent safety monitor
get its own trustworthy view of the same quantities?

## Why it cannot be decided by inspection

Four requirements want different things from sensing, and the cheapest answer to each is a
different sensor:

- **Amplitude control** ([SYS-001](../01-requirements/srs-system.md#sys-001)) needs motion, continuously
- **Resonance tracking** ([SYS-010](../01-requirements/srs-system.md#sys-010)) needs frequency and phase
- **Occupancy** ([SYS-008](../01-requirements/srs-system.md#sys-008)) needs load, absolutely and reliably
- **Anomaly detection** ([SAF-003](../01-requirements/safety-requirements.md#saf-003)) needs enough
  information to distinguish normal oscillation from coupled or irregular motion

And a fifth constraint cuts across all of them: [SW-003](../01-requirements/srs-software.md#sw-003)
requires the monitor **not to share sensor processing with the control loop**. So the question is
not only "which sensors" but "how many independent views of the truth do we need".

## Criteria

| # | Criterion | Derived from |
|---|---|---|
| C1 | Resolves amplitude and phase well enough for control | [SYS-001](../01-requirements/srs-system.md#sys-001), [SW-001](../01-requirements/srs-software.md#sw-001) |
| C2 | Resolves load across 3–18 kg well enough for occupancy | [SYS-005](../01-requirements/srs-system.md#sys-005), [SYS-008](../01-requirements/srs-system.md#sys-008) |
| C3 | Detects abnormal motion, including coupled modes | [SAF-003](../01-requirements/safety-requirements.md#saf-003) |
| C4 | Supports an independent path for the monitor | [SW-003](../01-requirements/srs-software.md#sw-003) |
| C5 | Fails detectably rather than silently | [SW-004](../01-requirements/srs-software.md#sw-004) |
| C6 | Survives continuous cyclic motion for the product life | [SYS-003](../01-requirements/srs-system.md#sys-003) |
| C7 | Adds no acoustic or mechanical burden to the load path | [SYS-002](../01-requirements/srs-system.md#sys-002), [MEC-001](../01-requirements/srs-mechanical.md#mec-001) |
| C8 | Cost and count | Cost target — not yet set |

**Elimination:** any approach in which a single sensor failure can leave both the controller and the
monitor confidently wrong is eliminated. That is the failure mode
[SW-004](../01-requirements/srs-software.md#sw-004) exists to prevent.

## A candidate the teardown suggests

Competitor A appears to use **no dedicated sensors at all**: hall sensors in the sensored BLDC give
rotor position and therefore drum angle and cable position, while a 0.060 Ω shunt gives motor
current and therefore torque and an inference of load *(teardown)*.

If that works, it is remarkably economical — amplitude, position and occupancy from parts the drive
already needs. But it collides directly with C4: a single motor supplies **both** the controller and
any monitor, so the independence
[SW-003](../01-requirements/srs-software.md#sw-003) demands cannot come from the motor alone.

## The hard part

A sensor that fails to a **plausible constant value** is more dangerous than one that fails to
nothing, because the control loop and the monitor will both act on it without complaint. Whatever
approach is chosen must make that failure detectable — by redundancy, by physical plausibility
checks against the known dynamics, or by cross-checking sensors of different type. Sensor
diversity, not just sensor duplication, may be required.
