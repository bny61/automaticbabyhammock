# System requirements (SYS)

Top-level requirements on the drive unit as a whole. Each traces to a
[user need](../00-product/user-needs.md) or a [hazard](../03-safety/hazard-analysis.md).

!!! note "Phase 0 seed — all `draft`, many values `TBD`"
    `TBD-P2` marks a value that must come out of [Phase 2 modelling](../02-architecture/system-architecture.md);
    `TBD-P3` from Phase 3 analysis. See [why TBDs are deliberate](index.md#tbd-values-are-deliberate).

---

### SYS-001 — Sustain bounce motion at the hammock's resonant frequency {#sys-001}

```yaml
id: SYS-001
status: draft
parent: UN-001
verification: T
risk: high
```

The ECU shall sustain vertical oscillation of the loaded hammock at an amplitude of
`TBD-P2` mm ± `TBD-P2` %, indefinitely, across the full rated load range, by injecting energy at
or near the system's resonant frequency.

**Rationale:** The core function. The motion is a driven mass-spring oscillation, not a pendulum
swing — the reference product states "up/down movements only, not swinging". Amplitude is the
parent-visible output and the safety-limited quantity, so it is specified rather than motor speed.

### SYS-002 — Acoustic emission {#sys-002}

```yaml
id: SYS-002
status: draft
parent: UN-002
verification: T
risk: high
```

The ECU shall emit no more than `TBD-P3` dB(A) measured at 1 m in a room with a background level
below 25 dB(A), at any setting and across the full rated load range, including any tonal or
impulsive components.

**Rationale:** Silence is the primary axis of competition; benchmark products lead with
"flüsterleise" and "lautlos". This requirement will eliminate whole actuator families before
[TS-001](../05-trade-studies/TS-001-actuation-concept.md) begins, so the number must be set from
measurement of reference units, not chosen for convenience. Tonal content matters more than
absolute level for waking a sleeper, hence its explicit inclusion.

### SYS-003 — Continuous duty {#sys-003}

```yaml
id: SYS-003
status: draft
parent: UN-004
verification: T
risk: medium
```

The ECU shall operate continuously at maximum rated load for at least 12 h without reducing
amplitude, without exceeding any component's thermal limit, and without imposing an automatic
shutdown timer.

**Rationale:** Multi-spring competitors advertise no maximum duration specifically against rivals
limited to 4 h. A timer that stops mid-night defeats the product's purpose. Note this requirement
*creates* [HAZ-007](../03-safety/hazard-analysis.md#haz-007).

### SYS-004 — Average power consumption {#sys-004}

```yaml
id: SYS-004
status: draft
parent: UN-008
verification: T
risk: medium
```

The ECU shall draw no more than `TBD-P2` W averaged over one hour of operation at mid-range load
and typical amplitude setting, and no more than `TBD-P2` W in standby.

**Rationale:** A benchmark competitor advertises ~15 ct/month at 3 h/day, implying roughly 5 W
average. Once a number is in the market it becomes the expectation. The exact figure must be
confirmed by measurement — the 5 W is derived from marketing copy, not measured.

### SYS-005 — Rated load range {#sys-005}

```yaml
id: SYS-005
status: draft
parent: UN-007
verification: T
risk: high
```

The ECU shall meet all functional and acoustic requirements across a total suspended load of
3 kg to 18 kg, including asymmetric loading representative of twins.

**Rationale:** Matches the benchmark range and covers birth to ~2 years plus twins. A sixfold mass
range moves the resonant frequency substantially, which is the principal difficulty of the control
design — this requirement is what makes fixed-frequency drive untenable.

### SYS-006 — On-unit control without connectivity {#sys-006}

```yaml
id: SYS-006
status: draft
parent: UN-005
verification: D
risk: low
```

The ECU shall provide full control of all user-adjustable functions via a physical interface on
the unit itself, operable one-handed and without visual attention, and shall require no companion
application, network or radio link for any function.

**Rationale:** The operating persona is a caregiver in the dark at 3 a.m. Every benchmark product
uses a physical dial, and one advertises the absence of radio emissions as a feature. See
[ADR-0003](../04-decisions/ADR-0003-connectivity-stance.md).

### SYS-007 — Compatibility with third-party stands and hammocks {#sys-007}

```yaml
id: SYS-007
status: draft
parent: UN-006
verification: A
risk: high
```

The ECU shall attach to third-party suspension points and hammocks that fall within the
assumptions stated in the
[interface control document](../02-architecture/interface-control-document.md), and shall
document those assumptions in the user instructions so an owner can determine compatibility
before use.

**Rationale:** The unit is sold standalone into an installed base we do not control. The second
clause matters: since we cannot test every stand, compatibility limits must be *communicable* to
the buyer, which makes it a product requirement rather than only an engineering one.

### SYS-008 — Occupancy detection and automatic stop {#sys-008}

```yaml
id: SYS-008
status: draft
parent: UN-009
verification: T
risk: medium
```

The ECU shall detect the removal of the occupant within `TBD-P3` s and bring the hammock to rest,
and shall not commence driven motion when the suspended load is outside the rated range.

**Rationale:** Shipped by a benchmark competitor. Beyond convenience, an unattended empty hammock
oscillating at resonance is an uncontrolled hazard — see
[HAZ-004](../03-safety/hazard-analysis.md#haz-004).

### SYS-009 — Single-fault tolerance of the load path {#sys-009}

```yaml
id: SYS-009
status: draft
parent: UN-003
verification: T
risk: high
```

The ECU shall retain the full rated load, without release and without permitting a fall exceeding
`TBD-P3` mm, following any single failure within its load path.

**Rationale:** The lead hazard, [HAZ-001](../03-safety/hazard-analysis.md#haz-001). Competitors
already ship redundant spring packs and publish the reasoning, so this is the category floor. The
fall-distance clause exists because "retains the load" is not sufficient — a sudden drop of even a
short distance onto a remaining element is itself a harm.

### SYS-010 — Adaptation to changing load {#sys-010}

```yaml
id: SYS-010
status: draft
parent: UN-007
verification: T
risk: medium
```

The ECU shall maintain the set amplitude as the suspended mass changes within the rated range,
without requiring the user to re-adjust the control, and shall re-acquire correct operation within
`TBD-P2` s of a load change.

**Rationale:** The resonant frequency shifts as the baby grows. Whether this is done by tracking
resonance or by another means is a design decision for Phase 4, not a requirement. A benchmark
competitor advertises a "self-learning" motor, so some adaptation is likely table stakes.
