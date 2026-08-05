# Regulatory scope (EU)

Target market is the **EU only**. No CPSC/ASTM work is in scope.

!!! warning "Nothing here is a compliance claim"
    This page records *intended* compliance and the reasoning behind it. Conformity is
    demonstrated only by test reports against the applicable harmonised standards, recorded in the
    [CE technical file](../07-manufacturing/ce-technical-file.md). Where this page is uncertain, it
    says so — those are the items to put to a test house or consultant in Phase 1.

## The product-safety fault line

A *Federwiege* is sold in Germany as a place where a baby sleeps. That makes the choice of
harmonised standard a **product-defining decision**, not a paperwork detail:

| Standard | Covers | Applies if… |
|---|---|---|
| **EN 1130:2019** | Cribs — scope explicitly includes **suspended cribs** and cradles providing **sleeping accommodation** | the product is marketed for sleep |
| **EN 16232:2013+A1:2018** | Infant swings | the product is a supervised, awake-time soothing device |
| **EN 12790-1:2023** | Reclined cradles | the lying surface is reclined rather than flat |

These carry different geometry, restraint, stability and labelling requirements, and they are not
freely combinable. **[ADR-0001](../04-decisions/ADR-0001-product-positioning.md) resolves this and
must be written before any requirement.**

!!! note "Scope subtlety to resolve with a test house"
    Our product is the **drive unit**, not the complete sleeping place. Whether the harmonised
    standard applies to the drive unit sold standalone, to the assembled system, or to both — and
    who carries the obligation when a customer combines our unit with a third-party stand — is a
    genuinely open question that materially affects the test plan. It is the first item for
    external advice in Phase 1.

### Reality check on rigour

An EU coordinated market-surveillance action (CASP 2021) on reclined cradles and baby swings found
that **49% of tested products failed at least one requirement**, and failures were overwhelmingly
on *mechanical* tests rather than chemical ones. Mechanical verification deserves proportionate
effort: see the [load path test plan](../06-verification/load-path-test-plan.md).

## Horizontal legislation

### GPSR — Regulation (EU) 2023/988

Applies from **13 December 2024**, replacing the General Product Safety Directive. It is a
catch-all obligation that applies alongside the harmonised standards above, not instead of them.
Key duties: general safety obligation, technical documentation, traceability (type/batch/serial,
manufacturer contact), a **responsible person established in the EU**, incident reporting, and
online-listing information duties. GPSR does not itself carry a CE mark.

### EMC — Directive 2014/30/EU

**Applies.** The unit contains a motor drive and switching electronics. Relevant harmonised
standards will be confirmed in Phase 4 once the topology exists; the household-appliance
EN 55014 series is the expected starting point, to be verified against the current OJEU list.
Emissions and immunity both matter — a unit that misbehaves when a phone charger is plugged in
nearby is a safety problem, not just a compliance one.

### LVD — Directive 2014/35/EU

**Expected not to apply to the ECU.** The LVD covers 50–1000 V AC / 75–1500 V DC. With an external
adapter supplying SELV (12 V nominal), mains never reaches our board and the LVD burden sits with
the **adapter manufacturer**, who supplies it pre-certified to EN IEC 62368-1.

This is a deliberate architectural choice with real cost and schedule value, recorded as
[ADR-0002](../04-decisions/ADR-0002-power-input-strategy.md) — not an accident of the design.

### RED — Directive 2014/53/EU

**Applies only if a radio is fitted.** Article 3(3)(d)(e)(f) cybersecurity requirements are now
mandatory for in-scope products, which turns "add BLE" into a compliance workstream covering
security-by-design, personal-data protection and fraud protection, plus the radio testing itself.

Since the [benchmark](competitive-benchmark.md) indicates wireless is a *market negative* in this
segment, the default position is **no radio**. See
[ADR-0003](../04-decisions/ADR-0003-connectivity-stance.md).

### Other

| Instrument | Status |
|---|---|
| RoHS 2011/65/EU | Applies — component selection must be RoHS-compliant |
| REACH 1907/2006 | Applies — SVHC declaration for materials in contact/proximity |
| WEEE 2012/19/EU | Applies — marking and national registration per member state |
| Batteries Regulation (EU) 2023/1542 | Only if a battery or backup cell is fitted — currently none planned |
| Machinery Regulation (EU) 2023/1230 | **To confirm.** Consumer childcare articles are normally handled under product-safety law rather than machinery, but a powered, load-bearing consumer product deserves an explicit determination rather than an assumption |
| Ecodesign / external power supply regulation | Applies to the **adapter**; select a compliant one |

## Conformity route — working assumption

Self-assessment with an internal production-control route, supported by third-party testing at an
accredited laboratory, and a technical file retained for 10 years. **No notified body is expected
to be required**, but this must be confirmed in Phase 1 — it is listed in the
[CE technical file plan](../07-manufacturing/ce-technical-file.md).

## Open questions for Phase 1

1. Does the harmonised standard apply to the drive unit standalone, the assembled system, or both?
2. Is a notified body required for any part of the route?
3. Which member states at launch (affects language and labelling duties under GPSR)?
4. Who is the EU responsible person under GPSR?
5. Is the Machinery Regulation genuinely excluded?
6. Which EMC harmonised standard is correct for a motor-driven childcare appliance?

Each becomes an issue and, where it changes the design, an ADR. Clause-level mapping to
requirements lives in the [standards matrix](../03-safety/standards-matrix.md).
