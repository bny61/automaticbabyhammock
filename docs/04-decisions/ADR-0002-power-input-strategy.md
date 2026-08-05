# ADR-0002 — External SELV adapter; no mains on the ECU

```
Status:      proposed
Date:        2026-08-05
Deciders:    TBD
Trade study: none — the option space is small and the regulatory consequence is decisive
Affects:     HW-001, HW-002, SYS-004, the conformity route
```

## Context

The unit needs mains-derived power for continuous overnight operation. Where the mains-to-low-
voltage conversion happens determines which directives apply to *our* board.

**Low Voltage Directive 2014/35/EU** covers equipment rated 50–1000 V AC or 75–1500 V DC. Below
that, the LVD does not apply.

Every reference product — Competitor A, Competitor B, Competitor C — uses an **external 12 V adapter fed
from 100–240 V**. The market has already converged here, which is corroborating evidence but not by
itself a reason.

## Options considered

### Option A — External pre-certified SELV adapter

Purchase an adapter certified to EN IEC 62368-1; the ECU accepts ~12 V SELV and contains nothing
above it.

**Pros:** the ECU falls **outside LVD scope** entirely; mains isolation, creepage and clearance,
and the associated safety testing are the adapter supplier's responsibility, already discharged; no
mains-side design, no isolation barrier on our PCB, smaller and cheaper board; no mains inside a
unit suspended above an infant; the adapter can be swapped per country without touching our design.

**Cons:** an external brick the customer must not lose or substitute; a second connector and cable
to specify; adapter quality is outside our control — a customer can fit a wrong or counterfeit one,
which is why [HW-002](../01-requirements/srs-electrical.md#hw-002) exists; the adapter's own
efficiency counts against [SYS-004](../01-requirements/srs-system.md#sys-004).

### Option B — Integrated mains supply inside the drive unit

**Pros:** single cable; no brick to lose; full control of supply behaviour and efficiency.

**Cons:** brings the ECU **into LVD scope**, adding a whole conformity workstream; requires an
isolation barrier, creepage and clearance discipline, and mains-rated components; puts mains
potential inside a moving object suspended over a sleeping infant; larger, heavier and hotter
inside a fixed envelope where [SAF-006](../01-requirements/safety-requirements.md#saf-006) and
mass both matter; substantially more expensive to certify.

### Option C — Battery operation

**Pros:** no mains at all; portable.

**Cons:** continuous overnight operation at ~5 W means a large battery, recharged daily; brings the
Batteries Regulation (EU) 2023/1542 into scope; a lithium cell above a sleeping infant introduces a
thermal-runaway hazard that no benchmark product accepts; a unit that dies at 3 a.m. fails
[UN-001](../00-product/user-needs.md#un-001).

## Decision

**Option A** — power the ECU exclusively from an external, pre-certified SELV adapter. No part of
the ECU operates at or connects to mains potential.

## Rationale

The decisive factor is not cost or convenience but **scope**: Option A removes an entire directive,
its testing and its design constraints from the project, at the price of an external brick that the
market has already normalised. Putting mains potential inside a continuously moving object
suspended above a sleeping infant is also a hazard we would be choosing to create, when the
alternative is simply not to.

Option C fails on the product requirement for uninterrupted overnight operation before its safety
implications are even considered.

## Consequences

**Positive:** LVD does not apply to the ECU; no isolation barrier, no mains-rated components, no
mains-side testing; smaller, cheaper, cooler board; the adapter can be varied by market
independently of our design.

**Negative:** we depend on a supplier's certification and must keep evidence of it in the
[technical file](../07-manufacturing/ce-technical-file.md); the customer can substitute a wrong
adapter, so input protection is mandatory rather than optional; the adapter's standby draw counts
against our advertised running cost even though we did not design it; an extra item to package,
ship and support.

**Requirements affected:** creates [HW-001](../01-requirements/srs-electrical.md#hw-001) and
[HW-002](../01-requirements/srs-electrical.md#hw-002); constrains
[SYS-004](../01-requirements/srs-system.md#sys-004) to include adapter losses.

**Follow-on work:** select the adapter (efficiency at *typical* load, not peak); confirm Ecodesign
external-power-supply compliance; specify the connector so a wrong adapter cannot be fitted easily;
decide the nominal voltage — 12 V is the benchmark norm but the actuator choice
([TS-001](../05-trade-studies/TS-001-actuation-concept.md)) may argue for 24 V, which is why
[HW-001](../01-requirements/srs-electrical.md#hw-001) still says `TBD-P4`.

## Revisiting

Revisit if the actuation concept demands a voltage or power level no reasonable external adapter
supplies, or if the product form factor changes such that an integrated supply becomes necessary.
Neither is expected.
