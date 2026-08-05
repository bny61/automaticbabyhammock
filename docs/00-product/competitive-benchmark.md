# Competitive benchmark

Reference products for this development, with the data gathered during Phase 0 scoping. This page
is the factual basis for several requirements and hazards, so each figure is attributed.

!!! warning "Attribution and confidence"
    Figures marked *(vendor)* come from manufacturer specification pages and marketing copy. They
    have **not** been independently measured. Anything used to justify a requirement must
    eventually be confirmed by our own measurement or teardown — see [gaps](#what-we-still-do-not-know).

## The product category

A *Federwiege* is a baby hammock suspended on springs. The powered versions sold in the German
market are **inline drive units**: a self-contained module with a carabiner at the top (to the
stand or ceiling) and a hook at the bottom (to the hammock), containing the spring pack, a motor
and the control electronics.

**The motion is vertical bounce, not lateral swinging.** Competitor A states this explicitly of its
stand: *"Up/down movements only, not swinging."* The mechanism is a **driven mass-spring
oscillator pumped near resonance** — this is the single most important fact about the product and
it governs the modelling, the actuator concept and the control law.

This also means the drive unit is sold **standalone**, compatible with third-party stands and
hammocks — which is why our stand and textile are out of scope, and why the
[interface control document](../02-architecture/interface-control-document.md) carries so much
weight.

## Specification comparison

| | **Competitor A A-1** | **Competitor A Maly** | **Competitor B B-1** | **Competitor C** |
|---|---|---|---|---|
| Unit mass | ~1.5 kg *(vendor)* | ~1.5 kg *(vendor)* | — | 4 kg (complete) *(vendor)* |
| Length, hook to hook | ~44 cm *(vendor)* | ~40 cm *(vendor)* | 22 cm (h) *(vendor)* | — |
| Width × depth | 15 × 14 cm *(vendor)* | 18 × 18 cm *(vendor)* | 11 × 18 cm *(vendor)* | — |
| Spring pack | ~22 cm free, ~44 cm loaded *(vendor)* | ~23 cm free, ~44 cm loaded *(vendor)* | up to 7 springs *(vendor)* | — |
| Rated load | 15 kg *(vendor)* | ~18 kg *(vendor)* | 3–18 kg *(vendor)* | — |
| Twins | yes *(vendor)* | yes *(vendor)* | yes *(vendor)* | — |
| Supply | external 12 V, 100–240 V 50–60 Hz *(vendor)* | as A-1 | external adapter *(vendor)* | external adapter |
| Control | rotary knob, stepless *(vendor)* | rotary knob | dial on unit, no app *(vendor)* | self-learning motor *(vendor)* |
| Wireless | none | none | none — advertised as a feature *(vendor)* | none |
| Duty limit | — | — | none stated *(vendor)* | — |
| Noise claim | — | — | "flüsterleise" *(vendor)* | "lautlos" *(vendor)* |
| Running cost | — | — | ~15 ct/month @ 3 h/day *(vendor)* | — |
| Safety features | — | — | weight detection + auto-stop; redundant springs *(vendor)* | shutdown within seconds on smallest irregularity *(vendor)* |

Wider field, not yet analysed: **nonomo**, **moonboon**, **Membantu**, **Elvent**, **Schmusewolke**.

## What the benchmark tells us

Each of the following becomes a requirement, a hazard or an interface constraint. They are not
background colour.

### Redundancy in the load path is the competitive floor

Competitor B's stated rationale for a multi-spring pack is explicit: if one spring fails, the
others prevent a fall. So **single-fault tolerance in the load path is already a shipped feature
of the competition**, not a differentiator. This drives [HAZ-001](../03-safety/hazard-analysis.md#haz-001)
and [SAF-001](../01-requirements/safety-requirements.md#saf-001).

### Roughly 5 W average, and it is advertised

Competitor B quotes ~15 ct/month at 3 h/day. At a German household tariff of roughly €0.30/kWh
that implies about **0.5 kWh/month**, i.e. ~5 W average draw. Treat this as a competitive
constraint to meet, not a target to aim near. *(Derived from a vendor marketing figure — confirm
by measurement before freezing [SYS-004](../01-requirements/srs-system.md#sys-004).)*

### Silence is the primary competitive axis

Both Competitor B and Competitor C lead on quietness. A quantified dB(A) requirement will eliminate
whole actuator families — geared steppers, brushed motors — before
[TS-001](../05-trade-studies/TS-001-actuation-concept.md) even starts. Getting the number right
early is therefore high-leverage.

### Wireless is a market negative here

Competitor B advertises operating *"ganz ohne schädliche Funk-Strahlung"* (entirely without harmful
radio radiation) and stresses that no app is needed. In this segment a radio is not a neutral
feature addition: it costs Radio Equipment Directive compliance work, including the now-mandatory
cybersecurity requirements, **and** it may actively harm positioning with the target buyer. See
[ADR-0003](../04-decisions/ADR-0003-connectivity-stance.md).

### A documented field failure at the frame interface

Competitor A warns that Maly is *"nicht kompatibel mit Gestellen, die eine Eigenschwingung haben"* —
incompatible with stands that have their own resonance. A driven oscillator coupled into a
compliant support can pump energy into an unintended mode and grow the amplitude beyond design
intent. Because our stand is out of scope, this must become a **bounded, testable constraint** in
the ICD rather than an unstated assumption. Drives [HAZ-002](../03-safety/hazard-analysis.md#haz-002)
and [IF-002](../01-requirements/frame-interface-assumptions.md#if-002).

### Continuous duty is a differentiator

Multi-spring units advertise no maximum operating duration, while some single-spring competitors
are limited to 4 h. Parents use these for full-night sleep, so continuous duty becomes a thermal
and reliability requirement rather than a convenience.

### The power architecture is already settled by the market

Every reference unit runs from an external 12 V adapter fed from 100–240 V mains. Mains never
enters the drive unit. This is worth adopting deliberately rather than by imitation, because it
keeps the ECU **out of Low Voltage Directive scope** — see
[ADR-0002](../04-decisions/ADR-0002-power-input-strategy.md).

## What we still do not know

Open items for Phase 1. These are the gaps that would most change the design:

- **Actuator type in each reference unit.** Not published. A teardown or acoustic/current
  signature analysis would tell us what the quiet solutions actually use, which is the single most
  useful input to [TS-001](../05-trade-studies/TS-001-actuation-concept.md).
- **Measured noise floor.** "Flüsterleise" is not a number. We need dB(A) at a defined distance
  for at least two reference units to set a credible target.
- **Actual bounce amplitude and frequency** across the load range — the core input to the
  [spring-mass model](../02-architecture/system-architecture.md).
- **How Competitor C's "self-learning" behaves.** Does it track resonance as the baby grows, or merely
  ramp amplitude on a timer? Determines whether adaptive control is table stakes.
- **What "smallest irregularity" means** for Competitor C's fast shutdown — the detection threshold and
  response time set the bar for our own anomaly detection.
- **Spring rate and pack geometry**, needed before the load-path design can be analysed.
- **Retail pricing and BOM cost position** — not yet gathered.

## Positioning gap analysis

To be completed in Phase 1 once [ADR-0001](../04-decisions/ADR-0001-product-positioning.md) is
decided. The interesting question: every reference product competes on *quietness* and *simplicity*.
Whether there is room to differentiate on adaptive control, safety instrumentation or
certification rigour depends on what the teardown work above reveals.
