# CE technical file

The dossier that must exist before the product is placed on the EU market, and be retained for
10 years afterwards.

!!! warning "This page is a plan, not evidence"
    It lists what the file must contain and tracks what exists. Compliance is demonstrated by the
    documents themselves, not by this index.

## Contents and status

| Section | Source | Status |
|---|---|---|
| Product description and intended use | [Vision](../00-product/vision.md), [ADR-0001](../04-decisions/ADR-0001-product-positioning.md) | Blocked on ADR-0001 |
| List of applied standards | [Standards matrix](../03-safety/standards-matrix.md) | Partial — horizontal only |
| Risk assessment | [Hazard analysis](../03-safety/hazard-analysis.md), [DFMEA](../03-safety/fmea-design.md) | Draft |
| Design documentation — schematics, PCB, mechanical | `hardware/`, `mechanical/` | Phase 5 |
| Bill of materials with compliance status | Part selection matrix (`hardware/component-selection/part-selection-matrix.md`) | Empty |
| Test reports — product safety | Accredited laboratory | Not started |
| Test report — EMC | [Pre-compliance](../06-verification/emc-precompliance-plan.md), then accredited | Not started |
| RoHS and REACH declarations | Supplier declarations | Not started |
| Adapter certification (EN IEC 62368-1) | Supplier | Not started — see [ADR-0002](../04-decisions/ADR-0002-power-input-strategy.md) |
| Instructions and safety information | Phase 5 | Not started |
| Labelling and marking | Phase 5 | Not started |
| GPSR traceability and responsible person | Phase 1 | Not started |
| Declaration of Conformity | On completion | Not started |

## Open questions blocking the plan

1. **Does the standard apply to the drive unit, the assembled system, or both?** This determines
   what is even being certified, and whether we can certify a unit sold for use with third-party
   stands. First item for external advice.
2. **Is a notified body required?** Working assumption is self-assessment with accredited testing
   and an internal production control route — to be confirmed, not assumed.
3. **Who is the EU responsible person under GPSR?**
4. **Which member states at launch?** Determines language and labelling obligations.
5. **Is the Machinery Regulation genuinely excluded** for a powered, load-bearing consumer product?

## Schedule note

Certification lead time is likely the **critical path to launch**, not design. Laboratory booking,
sample build and the retest cycle after any failure should be planned from Phase 1, not discovered
in Phase 5. Given that market surveillance found roughly half of tested products in this category
failing at least one requirement, budgeting for at least one retest cycle is realistic planning
rather than pessimism.
