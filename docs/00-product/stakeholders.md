# Stakeholders

Who has a stake in this product, what they need from it, and what they can block.

!!! note "Phase 0 seed"
    Names and owners are to be filled in during Phase 1. The point of this page is that each row
    generates requirements or constraints that would otherwise be missed.

| Stakeholder | What they need | What they can block |
|---|---|---|
| **Parent (buyer and operator)** | A baby that settles, without being woken by the device or getting out of bed | The purchase. Primary source of [user needs](user-needs.md) |
| **The infant (user, no voice)** | Not to be harmed. Motion within safe limits; no entrapment, entanglement, overheating or fall | Nothing — which is exactly why the [hazard analysis](../03-safety/hazard-analysis.md) speaks for them |
| **Second caregiver / grandparent** | To operate it without instruction, in the dark, first time | Usability. Drives the case against an app-only interface |
| **Retailer / distributor** | Documented conformity, low return rate, no recall exposure | Listing. Increasingly demands test reports, not assertions |
| **Market surveillance authority** | Conformity with the applicable harmonised standard; a technical file on demand | Sale, EU-wide. CASP 2021 found ~49% of this category non-compliant on at least one point |
| **Notified body / test laboratory** | A testable product and a coherent technical file | The certificate, and the schedule |
| **EU responsible person (GPSR)** | Traceability, contact details, incident reporting path | Legal placing on the market |
| **Contract manufacturer** | Manufacturable design, clear BOM, end-of-line test | Volume production, unit cost |
| **Component suppliers** | Realistic volumes and lead times | The BOM — drives lifecycle and second-source columns in the part selection matrix (`hardware/component-selection/part-selection-matrix.md`) |
| **Third-party stand and hammock makers** | Our unit not to damage or misbehave on their product | Compatibility, and our reputation. They are the reason the [ICD](../02-architecture/interface-control-document.md) exists |
| **Insurer / legal** | Defensible design records: hazard analysis, decisions, test evidence | Nothing day to day — everything after an incident |
| **Development team** | Decisions recorded, requirements stable enough to build against | Delivery |

## Consequences for the design

Three rows above generate obligations that are easy to overlook:

- **The infant has no voice in requirements.** Nobody in the buying chain advocates for them
  directly. The hazard analysis is their proxy, which is why safety requirements need a named
  hazard and a verification method before merge.
- **Third-party stand makers are stakeholders we will never meet.** Our unit will be attached to
  hardware they designed, without coordination. Their interests appear in the repository only as
  `IF-xxx` assumptions.
- **Retailers increasingly demand evidence, not claims.** This raises the value of a clean
  technical file from "regulatory hygiene" to a commercial asset.
