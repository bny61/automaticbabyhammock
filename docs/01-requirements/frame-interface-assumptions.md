# Frame interface assumptions (IF)

Everything the drive unit assumes about hardware that is **[out of scope](../00-product/project-scope.md)** —
the stand, ceiling hook or door bracket above it, and the hammock below it.

!!! danger "This is where the project is most likely to fail"
    The unit is sold standalone and attached to hardware we do not control and cannot test. An
    assumption left implicit here becomes either a field failure or a product that silently only
    works with one stand.

    This is not hypothetical: Competitor A publicly warns that one of its units is incompatible
    with stands that have their own resonance. Someone made an implicit assumption; the customer
    found out.

**Every `IF-xxx` requires a `tolerance` band** — the linter rejects one without it. An assumption
without a tolerance is an opinion.

Assumptions here are only useful if they are **communicable to the buyer**
([SYS-007](srs-system.md#sys-007)) and **verifiable by the unit itself** where a violation is
hazardous. An assumption we can neither publish nor detect is a latent defect.

!!! note "Phase 0 seed — all `draft`, values `TBD-P2`"
    Real values come from Phase 2 modelling plus a survey of stands actually on the market.

---

### IF-001 — Suspension point static strength {#if-001}

```yaml
id: IF-001
status: draft
parent: SYS-007
verification: A
tolerance: minimum, no upper bound
```

The suspension point shall sustain a static load of at least `TBD-P2` kg, being the rated load
plus the unit mass plus a dynamic factor of `TBD-P2`.

**Rationale:** Driven oscillation means the peak dynamic load exceeds the static weight
substantially, and the buyer will size their hook by the baby's weight if we let them. This figure
must appear in the user instructions.

### IF-002 — Supporting structure resonance {#if-002}

```yaml
id: IF-002
status: draft
parent: SYS-007
verification: T
tolerance: no resonant mode within TBD-P2 Hz of the drive band
```

The supporting structure shall have no resonant mode within `TBD-P2` Hz of the unit's drive
frequency band, and shall have a vertical stiffness of at least `TBD-P2` N/mm at the suspension
point.

**Rationale:** The direct mitigation for [HAZ-002](../03-safety/hazard-analysis.md#haz-002) and the
known competitor field failure. Two consequences follow: the limit must be published in a form a
buyer can actually apply — which is hard, because no consumer can measure their stand's resonance
— and the unit must therefore *detect* the violation itself
([SAF-003](safety-requirements.md#saf-003)) rather than relying on the instruction being followed.
Closing this gap is a Phase 2 modelling objective.

### IF-003 — Suspension geometry {#if-003}

```yaml
id: IF-003
status: draft
parent: SYS-007
verification: I
tolerance: TBD-P2 mm
```

The unit shall accommodate suspension hardware within a geometric envelope of `TBD-P2`, and shall
require a free vertical drop of no more than `TBD-P2` mm between the suspension point and the
hammock attachment.

**Rationale:** Benchmark units are 40–44 cm hook to hook before the hammock even begins. Ceiling
height and stand height are fixed constraints in the customer's home and cannot be negotiated
after purchase.

### IF-004 — Hammock attachment and mass {#if-004}

```yaml
id: IF-004
status: draft
parent: SYS-007
verification: I
tolerance: TBD-P2 kg
```

The hammock shall attach by a single point compatible with a `TBD-P2` hook, and shall have an
unloaded mass of `TBD-P2` kg ± `TBD-P2` kg.

**Rationale:** The hammock mass is part of the oscillating system, so it shifts the resonant
frequency independently of the baby. A heavy textile hammock and a light net hammock are not
interchangeable from the control loop's point of view.

### IF-005 — Damping contributed by the hammock and occupant {#if-005}

```yaml
id: IF-005
status: draft
parent: SYS-001
verification: A
tolerance: TBD-P2
```

The oscillating system shall present a damping ratio within the range `TBD-P2`, accounting for
textile hysteresis, the occupant's body and air resistance.

**Rationale:** Damping sets the energy that must be injected per cycle, and therefore the actuator
sizing and the [power budget](srs-system.md#sys-004). It is the parameter we know least about and
the one that most directly drives [TS-001](../05-trade-studies/TS-001-actuation-concept.md), so
measuring it on real hammocks is a high-priority Phase 2 task.

### IF-006 — Installation environment {#if-006}

```yaml
id: IF-006
status: draft
parent: SYS-003
verification: A
tolerance: 10 °C to 30 °C, up to 80 % RH non-condensing
```

The unit shall be installed indoors in a domestic bedroom within the stated ambient range, with
unobstructed airflow around the housing.

**Rationale:** Bounds the thermal analysis for [SYS-003](srs-system.md#sys-003) and
[SAF-006](safety-requirements.md#saf-006). "Unobstructed airflow" is optimistic in a real nursery
and the thermal analysis should not lean on it heavily.
