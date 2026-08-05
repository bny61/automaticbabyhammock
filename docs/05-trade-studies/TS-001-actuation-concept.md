# TS-001 — Actuation concept

```
Status:     open
Owner:      TBD
Decides:    ADR-0004
Blocked on: Phase 2 energy and damping models; the cost target (Phase 1)
```

!!! danger "The keystone decision of the project"
    This determines the drive stage, strongly influences the processor and power design, and is
    the main determinant of both acoustic performance and unit cost. Everything downstream depends
    on it, so it is worth doing properly.

## Question

How is energy injected into the mass-spring oscillator each cycle to sustain the target amplitude?

## Why it cannot be decided by inspection

[SYS-002](../01-requirements/srs-system.md#sys-002) (near-silence) and cost pull hard against each
other, and the quantity that sizes everything — the energy lost per cycle to damping — is currently
unknown ([IF-005](../01-requirements/frame-interface-assumptions.md#if-005)). The load range is
also wide: [SYS-005](../01-requirements/srs-system.md#sys-005) spans 3–18 kg, a factor of six,
which moves both the resonant frequency and the required force.

The benchmark products are all quiet, and **none of them publishes how**. Closing that gap is the
single most valuable input to this study — see [evidence needed](#evidence-needed).

## Criteria

Weights to be set in Phase 4, from the requirements, before any candidate is scored.

| # | Criterion | Derived from | Measured by |
|---|---|---|---|
| C1 | Acoustic emission, including tonal content | [SYS-002](../01-requirements/srs-system.md#sys-002), [MEC-004](../01-requirements/srs-mechanical.md#mec-004) | dB(A) at 1 m + spectrum, on a prototype |
| C2 | Average power at typical operating point | [SYS-004](../01-requirements/srs-system.md#sys-004) | Measurement |
| C3 | Unit cost at volume | Cost target — **not yet set** | Quoted BOM |
| C4 | Performance across the full load range | [SYS-005](../01-requirements/srs-system.md#sys-005) | Model + prototype |
| C5 | Controllability and amplitude precision | [SYS-001](../01-requirements/srs-system.md#sys-001), [SYS-010](../01-requirements/srs-system.md#sys-010) | Model + prototype |
| C6 | Fits the physical envelope and mass budget | [Constraints](../01-requirements/constraints.md) | Layout study |
| C7 | Wear-out behaviour under continuous duty | [SYS-003](../01-requirements/srs-system.md#sys-003), [MEC-001](../01-requirements/srs-mechanical.md#mec-001) | Life analysis |
| C8 | Behaviour on failure — can it fail dangerously? | [HAZ-006](../03-safety/hazard-analysis.md#haz-006) | FMEA |

**Elimination criteria:** any candidate that cannot meet the acoustic requirement, or that can
apply force to the load path exceeding its rated limit on a single fault, is eliminated regardless
of score.

## Candidate concepts

To be developed in Phase 4. The concept space, stated without prejudice:

- **Rotary actuator driving an eccentric or crank** — converts rotation to reciprocating force
- **Linear actuator in the load path** — modulates the effective suspension length directly
- **Impulse actuation** — a short push once per cycle at the right phase, rather than continuous force
- **Variable-stiffness approach** — modulating the spring pre-load rather than applying force
- **Off-resonance rotating mass** — an unbalanced mass driven at the resonant frequency

Each must be evaluated against the same criteria. Note that the concepts differ not only in
hardware but in *how they are controlled*, which is why they feed
[TS-002](TS-002-mcu-selection.md).

## Evidence needed before this study can run {#evidence-needed}

1. **Energy per cycle** at target amplitude across 3–18 kg — from the
   Phase 2 energy model (`models/actuation-energy-budget`)
2. **Damping ratio** of real hammocks with real occupants
   ([IF-005](../01-requirements/frame-interface-assumptions.md#if-005)) — measurement, not estimate
3. **Acoustic target** as a number, from measuring reference products
4. **Cost target** — currently missing and blocking
5. **What the benchmark products actually use.** A teardown, or acoustic and current-signature
   analysis, of a Competitor A or Competitor B unit. They have all solved the quiet-actuation problem
   commercially; not knowing how is the largest avoidable gap in this study.

## Note on the physics

Because the system is resonant, the actuator does **not** have to lift the load — it only replaces
energy lost to damping. That is what makes a ~5 W average plausible, and it means force
requirements may be far lower than intuition suggests. It also means the *phase* of energy
injection matters more than its magnitude, which favours concepts with good phase controllability
and connects directly to the timing requirement in
[SW-001](../01-requirements/srs-software.md#sw-001).
