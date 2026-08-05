# Constraints

Constraints are not requirements: nothing traces to them and they carry no IDs. They are boundaries
that requirements must respect, recorded here so they are visible when trade-offs are made.

## Commercial

| Constraint | Value | Source |
|---|---|---|
| Target unit cost (BOM, at volume) | **TBD — Phase 1** | Blocks [TS-001](../05-trade-studies/TS-001-actuation-concept.md) |
| Retail price position | **TBD — Phase 1** | Benchmark pricing not yet gathered |
| Launch volume | **TBD — Phase 1** | Drives second-sourcing and process choices |
| Target launch date | **TBD** | Certification lead time is the long pole |

!!! warning "The cost target is genuinely blocking"
    [TS-001](../05-trade-studies/TS-001-actuation-concept.md) has to weight acoustic performance
    against cost. Without a cost target the trade study cannot be scored, and the actuator decision
    — the most consequential in the project — cannot be made defensibly. This is the single most
    important item to close in Phase 1.

## Physical

| Constraint | Value | Source |
|---|---|---|
| Overall length, suspension to hammock hook | ≤ ~44 cm | Benchmark; ceiling and stand height are fixed in the customer's home |
| Unit mass | ~1.5 kg class | Benchmark; the unit's own mass is part of the oscillating system |
| Cross-section | ~15 × 15 cm class | Benchmark; must not intrude into the infant's space |

## Environmental and regulatory

| Constraint | Value |
|---|---|
| Market | EU only |
| Operating environment | Indoor domestic bedroom, 10–30 °C ([IF-006](frame-interface-assumptions.md#if-006)) |
| Mains connection | None on the ECU — external SELV adapter only ([ADR-0002](../04-decisions/ADR-0002-power-input-strategy.md)) |
| Radio | None by default ([ADR-0003](../04-decisions/ADR-0003-connectivity-stance.md)) |
| Materials | RoHS and REACH compliant; SVHC declaration required |
| End of life | WEEE marking and national registration |

## Process

| Constraint | Value |
|---|---|
| EDA tool | KiCad 9 |
| Requirements | Markdown docs-as-code in this repository; matrix generated |
| Repository | Private, proprietary |
| Design authority | No hardware platform decision before Phase 4 |

## Conflicts to resolve

Recorded now because each will force a trade-off later:

- **Silence vs cost.** The quietest actuator technologies are the expensive ones, and
  [SYS-002](srs-system.md#sys-002) is a make-or-break competitive requirement.
- **Cooling vs entrapment.** [MEC-005](srs-mechanical.md#mec-005) — vents help thermal performance
  and create apertures.
- **Redundancy vs mass and length.** [SAF-001](safety-requirements.md#saf-001) adds load-path
  elements inside a fixed physical envelope that is already set by the benchmark.
- **Auto-resume vs unattended operation.** [SAF-008](safety-requirements.md#saf-008) — the safest
  behaviour and the most useful behaviour are not the same.
