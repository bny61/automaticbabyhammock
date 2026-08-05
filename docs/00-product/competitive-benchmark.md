# Competitive benchmark

Reference products for this development, with the data gathered during Phase 0 scoping. This page
is the factual basis for several requirements and hazards, so each figure is attributed.

!!! warning "Attribution and confidence"
    Figures marked *(vendor)* come from manufacturer specification pages and marketing copy and have
    **not** been independently verified. Figures marked *(observed)* come from an owner's first-hand
    use of a Competitor A unit; *(teardown)* from photographs of that unit's internals, recorded in
    `brainstorming/teardown/Competitor A/findings.md`. Anything used to justify a requirement must
    trace to one of the latter two — see [gaps](#what-we-still-do-not-know).

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

### What the spring pack is actually for

The springs **carry the infant's weight and provide the oscillation** *(owner)*. Competitor B
markets the multi-spring pack as a redundancy feature — if one fails, the others prevent a fall —
which is true but is a by-product, not the purpose.

The parent **adds springs as the baby grows**, going from 2–3 at birth to 5–7 later *(observed)*,
to stop the pack over-extending under the greater load. That is a static strength concern. It also,
unavoidably, keeps the bounce frequency constant:

Static droop is `x = mg/k`, and substituting into `f = (1/2π)√(k/m)` gives

    f = (1/2π)·√(g/x)

**Frequency depends only on droop** — not on the baby's mass, not on the spring rate. So restoring
the droop restores the frequency. Load-bearing and frequency-setting are one job, not two.

This predicts the observed behaviour: the published ~22 cm free / ~44 cm loaded dimensions give a
droop of ~22 cm and therefore ≈ 1.06 Hz, and the owner independently describes the bounce as "about
one per second". Derivation and validation plan in
`models/spring-mass-dynamics/static-droop-sets-frequency.md`.

**The consequence for us is significant.** Adaptation across 3–18 kg *must* be mechanical in some
form — a control loop cannot stop a spring being over-extended. In these products it is also
**manual**, done by the parent, which is what creates
[HAZ-009](../03-safety/hazard-analysis.md#haz-009).

### How Competitor A actually drives the hammock *(teardown)*

A **motorised cable winch**, with the drive deliberately **outside the load path**:

| Element | Part |
|---|---|
| Motor | Sensored BLDC, `JK42BLS01-X055`, 42 mm frame |
| Gate driver | TI `DRV8306H` — three-phase, hardware-interface variant |
| MCU | NXP `LPC1114` (ARM Cortex-M0) |
| Current sense | 0.060 Ω shunt + `LM2904` |
| Bulk store | 6800 µF / 35 V |
| Transmission | Pinion → plastic reduction gear → cable drum → steel wire rope |

The rope **only pulls the springs; the springs carry the infant.** *(confirmed by owner)* So no
actuator failure — stripped gear, snapped rope, seized drum, shorted MOSFET, dead firmware — can
release the load. It is fail-safe by architecture.

Two further consequences. The **6800 µF bulk capacitor confirms an impulsive drive**: a burst of
motor current per cycle, recharged slowly between, which is how average draw stays near 5 W while
peak current is far higher. And **sensing appears entirely motor-intrinsic** — hall position gives
drum angle and therefore cable position, the shunt gives torque and therefore an inference of load.
No accelerometer, load cell or separate encoder is present, which matters for
[TS-004](../05-trade-studies/TS-004-sensing-approach.md).

## Specification comparison

| | **Competitor A A-1** | **Competitor A Maly** | **Competitor B B-1** | **Competitor C** |
|---|---|---|---|---|
| Unit mass | ~1.5 kg *(vendor)* | ~1.5 kg *(vendor)* | — | 4 kg (complete) *(vendor)* |
| Length, hook to hook | ~44 cm *(vendor)* | ~40 cm *(vendor)* | 22 cm (h) *(vendor)* | — |
| Width × depth | 15 × 14 cm *(vendor)* | 18 × 18 cm *(vendor)* | 11 × 18 cm *(vendor)* | — |
| Spring pack | ~22 cm free, ~44 cm loaded *(vendor)*; **user adds springs as baby grows**, 2–3 → 5–7 *(observed)* | ~23 cm free, ~44 cm loaded *(vendor)* | up to 7 springs *(vendor)* | — |
| Rated load | 15 kg *(vendor)* | ~18 kg *(vendor)* | 3–18 kg *(vendor)* | — |
| Twins | yes *(vendor)* | yes *(vendor)* | yes *(vendor)* | — |
| Bounce amplitude | 1–3 cm *(observed)* | — | — | — |
| Actuation | sensored BLDC → gear → cable drum → rope, parallel to load path *(teardown)* | — | — | — |
| Resonance tracking | **none** — user sets rate on the dial *(observed)* | — | — | — |
| Supply | external 12 V, 100–240 V 50–60 Hz *(vendor)* | as A-1 | external adapter *(vendor)* | external adapter |
| Control | one user-facing dial + LED; sets **rate**, not amplitude *(observed)* | rotary knob | dial on unit, no app *(vendor)* | self-learning motor *(vendor)* |
| Wireless | none | none | none — advertised as a feature *(vendor)* | none |
| Duty limit | — | — | none stated *(vendor)* | — |
| Noise claim | soft whir, once per bounce cycle *(observed)* | — | "flüsterleise" *(vendor)* | "lautlos" *(vendor)* |
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

- ~~**Actuator type in each reference unit.**~~ **Answered for Competitor A** by teardown: sensored
  BLDC, plastic reduction gear, cable drum, steel rope, parallel to the load path. Still unknown
  for Competitor B and Competitor C.
- **Measured noise floor.** "Flüsterleise" is not a number. We need dB(A) at a defined distance
  for at least two reference units to set a credible target.
- **Actual bounce amplitude and frequency** across the load range. Amplitude is roughly 1–3 cm
  *(observed)*; frequency is user-set and unmeasured. Still the core input to the
  [spring-mass model](../02-architecture/system-architecture.md).
- **How Competitor C's "self-learning" behaves.** Does it track resonance as the baby grows, or merely
  ramp amplitude on a timer? Determines whether adaptive control is table stakes.
- **What "smallest irregularity" means** for Competitor C's fast shutdown — the detection threshold and
  response time set the bar for our own anomaly detection.
- **Spring rate and free length**, needed before the stiffness reasoning above becomes
  quantitative rather than proportional.
- **Adapter output voltage.** The 35 V-rated bulk capacitor hints the incumbent may run above 12 V;
  the label has not been read. Relevant to [ADR-0004](../04-decisions/ADR-0004-nominal-supply-voltage.md).
- **Whether any safety monitor independent of the MCU exists.** None is visible in the photographs,
  which would put the incumbent below the bar our
  [SAF-005](../01-requirements/safety-requirements.md#saf-005) sets.
- **Retail pricing and BOM cost position** — not yet gathered.

## Positioning gap analysis

To be completed in Phase 1 once [ADR-0001](../04-decisions/ADR-0001-product-positioning.md) is
decided. The interesting question: every reference product competes on *quietness* and *simplicity*.
Whether there is room to differentiate on adaptive control, safety instrumentation or
certification rigour depends on what the teardown work above reveals.
