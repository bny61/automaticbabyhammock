# TS-003 — Actuator drive stage

```
Status:     open
Owner:      TBD
Decides:    ADR-0006
Blocked on: TS-001 — the actuation concept determines what is being driven
```

## Question

How is electrical energy delivered to the actuator, under control, quietly and safely?

## Why it cannot be decided by inspection

The drive stage is a major and frequently underestimated **noise source** in its own right, quite
apart from the actuator. Switching frequency, current ripple and control scheme all produce
audible artefacts — magnetostriction in inductors, coil whine, and tonal content at the switching
or commutation frequency. In a product whose main competitive axis is silence
([SYS-002](../01-requirements/srs-system.md#sys-002)), that makes this a acoustic decision as much
as an electrical one.

## Criteria

| # | Criterion | Derived from |
|---|---|---|
| C1 | Acoustic contribution — switching artefacts, ripple, tonal content | [SYS-002](../01-requirements/srs-system.md#sys-002) |
| C2 | Efficiency at the *typical* operating point, not peak | [SYS-004](../01-requirements/srs-system.md#sys-004) |
| C3 | Controllability — resolution and phase fidelity | [SYS-001](../01-requirements/srs-system.md#sys-001), [SW-001](../01-requirements/srs-software.md#sw-001) |
| C4 | Supports an independent disable that the processor cannot override | [SAF-005](../01-requirements/safety-requirements.md#saf-005) |
| C5 | Fault behaviour — short, open, over-temperature, stall | [HAZ-006](../03-safety/hazard-analysis.md#haz-006) |
| C6 | Current sensing quality, if the sensing approach depends on it | TS-004 |
| C7 | Thermal behaviour under continuous duty | [SYS-003](../01-requirements/srs-system.md#sys-003), [SAF-006](../01-requirements/safety-requirements.md#saf-006) |
| C8 | Cost, size and lifecycle | Cost target — not yet set |

**Elimination:** a stage whose fault modes can drive the actuator continuously without an
independent means of removing power is eliminated.

## Note

Energy injection into a resonant system may be **impulsive and low duty cycle** rather than
continuous. If TS-001 chooses such a concept, the drive stage sees short high-current bursts and
long idle periods — which changes the efficiency question (standby loss dominates), the thermal
question (peak versus average) and the acoustic question (impulsive noise is far more likely to
wake a sleeper than steady noise of the same level). This is a good reason not to run this study
before TS-001.
