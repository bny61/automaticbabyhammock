# ADR-0004 — Nominal supply voltage of 12 V

```
Status:      accepted
Date:        2026-08-05
Deciders:    product owner
Trade study: none — decided as a product constraint ahead of TS-005
Affects:     HW-001, TS-001, TS-003, TS-005, power tree
```

## Context

[ADR-0002](ADR-0002-power-input-strategy.md) established that the ECU is fed from an external
pre-certified SELV adapter, keeping the board outside Low Voltage Directive scope. It deliberately
left the **nominal voltage open**, because the actuator choice
([TS-001](../05-trade-studies/TS-001-actuation-concept.md)) could argue for a higher rail.
[HW-001](../01-requirements/srs-electrical.md#hw-001) has carried `TBD-P4` since.

Two inputs now bear on it.

**The benchmark uses 12 V**, per Competitor A's published figures. But the
teardown (`brainstorming/teardown/Competitor A/findings.md`) found a **6800 µF / 35 V** bulk
capacitor. A 35 V part on a 12 V rail is unusually generous derating, which hints the incumbent may
in fact run higher — the adapter output has not been read directly.

**The drive is impulsive.** The teardown confirms a large bulk store feeding burst motor current,
so peak current — not average — sizes the switching devices, the shunt, the connectors and the
copper.

## Options considered

### Option A — 12 V nominal

**Pros:** ubiquitous, cheap, deeply second-sourced adapters; matches the benchmark's published
figure; familiar to customers, and a replacement is easy to buy anywhere; lower voltage stress on
the semiconductors.

**Cons:** **twice the current of 24 V for the same mechanical power.** With an impulsive drive
already drawing high peaks, this pushes on MOSFET conduction loss (I²R), shunt dissipation,
connector and cable rating, and PCB copper — all of which cost money, heat and board area. Heat
works directly against [SAF-006](../01-requirements/safety-requirements.md#saf-006) in a sealed
housing under continuous duty.

### Option B — 24 V nominal

**Pros:** halves the current for the same power, easing every loss and rating above; the incumbent's
35 V capacitor suggests this may be what the market leader actually does; more headroom if the
actuator turns out to need more force than expected.

**Cons:** adapters are less common and typically dearer; a customer replacing a lost adapter is more
likely to buy the wrong one; higher voltage stress on the semiconductors.

### Option C — Defer until TS-001 and TS-005 close

**Pros:** the disciplined answer under this project's own rules — the voltage is a consequence of
the actuator, and deciding it first inverts the intended order.

**Cons:** leaves a constraint open that the owner has a clear commercial preference on, and the
preference is unlikely to change.

## Decision

**Option A — 12 V nominal**, set as a product constraint.

## Rationale

Decided by the product owner on availability and customer-replaceability grounds. A 12 V adapter is
something a customer can buy anywhere, which matters for a device that runs every night and whose
adapter will eventually be lost or damaged.

The decision is recorded honestly as a **constraint accepted ahead of the analysis**, not as an
outcome of it. Option C was the procedurally correct answer under this project's own discipline,
and it was overridden deliberately rather than overlooked.

## Consequences

**Positive:** adapter cost and availability are solved; second sourcing is trivial; matches the
benchmark; the customer-replacement path is easy.

**Negative — and this is the real cost:** at 12 V the drive stage carries roughly **twice the
current** it would at 24 V for the same mechanical power. Concretely, this constrains
[TS-003](../05-trade-studies/TS-003-motor-driver.md) toward lower-R<sub>DS(on)</sub> devices,
raises shunt and connector requirements, adds copper, and adds heat inside a sealed housing that
must already survive continuous duty. **TS-001 is now choosing an actuator inside a fixed power
envelope**, and if the Phase 2 energy model shows the force requirement is higher than expected,
this decision will be the binding constraint.

**Requirements affected:** [HW-001](../01-requirements/srs-electrical.md#hw-001) `TBD-P4` → 12 V
nominal. Input tolerance and over-voltage limits in
[HW-002](../01-requirements/srs-electrical.md#hw-002) remain open pending adapter selection.

**Follow-on work:** read the incumbent's adapter label to settle what it actually uses; carry peak
current explicitly into TS-001 and TS-003 scoring; revisit the thermal analysis for
[SAF-006](../01-requirements/safety-requirements.md#saf-006) with the higher current.

## Revisiting

Revisit if the Phase 2 energy model or TS-001 shows that the required peak current at 12 V drives
the drive stage, thermal design or cost past what 24 V would cost — including the adapter premium.
The evidence that would justify superseding this is a quantified comparison, not a preference.
