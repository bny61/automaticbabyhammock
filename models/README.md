# Models

Physics and control modelling. **This is Phase 2 work and it gates Phase 4** — the trade studies
cannot be scored until these produce numbers.

## Why modelling comes before hardware selection

Almost every `TBD-P2` in the requirements is an output of this directory. Without them,
[TS-001](../docs/05-trade-studies/TS-001-actuation-concept.md) cannot size an actuator, and the
most consequential decision in the project would be made on intuition.

## The system

A **driven vertical mass-spring oscillator**: hammock plus occupant plus spring pack, pumped near
resonance. Not a pendulum, not a lateral swing — see
[system architecture](../docs/02-architecture/system-architecture.md#the-physics-a-driven-mass-spring-oscillator).

## Directories

| Directory | Produces | Feeds |
|---|---|---|
| `spring-mass-dynamics/` | Resonant frequency vs load across 3–18 kg, for a range of spring rates | [SYS-005](../docs/01-requirements/srs-system.md#sys-005), [SYS-010](../docs/01-requirements/srs-system.md#sys-010) |
| `actuation-energy-budget/` | Energy per cycle vs damping and amplitude; force/torque envelope | [TS-001](../docs/05-trade-studies/TS-001-actuation-concept.md), [SYS-004](../docs/01-requirements/srs-system.md#sys-004) |
| `frame-coupling/` | Behaviour with a compliant support; runaway bounds | [IF-002](../docs/01-requirements/frame-interface-assumptions.md#if-002), [HAZ-002](../docs/03-safety/hazard-analysis.md#haz-002) |
| `control-loop/` | Resonance tracking, amplitude regulation, phase-error sensitivity | [SW-001](../docs/01-requirements/srs-software.md#sw-001), [SAF-003](../docs/01-requirements/safety-requirements.md#saf-003) |

## Required outputs

1. Resonant frequency across the load range
2. Energy per cycle at target amplitude vs damping ratio — **the actuator sizing input**
3. Amplitude sensitivity to drive phase error — sets the timing budget
4. Coupling bounds with a compliant support
5. **Load-cycle count over product life** — the input to [MEC-001](../docs/01-requirements/srs-mechanical.md#mec-001) fatigue analysis

## The weakest input

Damping ([IF-005](../docs/01-requirements/frame-interface-assumptions.md#if-005)) is the parameter
we know least about and the one that most directly sizes the actuator. Model results should be
presented as **sensitivity to damping**, not as single numbers, until it has been measured on real
hammocks with real occupants.

## Conventions

Python with numpy/scipy; notebooks for exploration, plain modules for anything a requirement
depends on. Every model that produces a requirement value must state its assumptions and cite the
`IF-xxx` or measurement they come from. A number in a requirement must be traceable to the model
run that produced it.
