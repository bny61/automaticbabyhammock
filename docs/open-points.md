# Open points register

Every unresolved question in the project, what it blocks, and **which artefacts must be
corrected once it is answered**. The last column is the point of this page: when an answer
arrives, it is not enough to write it down — the documents built on the assumption have to be
fixed too.

Kept by hand. Run `python tools/list_open_points.py` to cross-check it against the `TBD`
markers actually present in the tree.

**Status:** `blocking` stops other work · `open` needs an answer · `watching` may resolve itself

---

## The four that block everything else

| ID | Question | Blocks | Artefacts to fix when answered |
|---|---|---|---|
| **OP-001** | **Sleep product or supervised soothing device?** Selects EN 1130 (suspended crib) vs EN 16232 (infant swing) vs EN 12790 (reclined cradle) | Every requirement. Geometry, restraint, labelling and the entrapment probe dimensions all follow from it | `ADR-0001` (accept) · `00-product/regulatory-scope.md` · `03-safety/standards-matrix.md` (clause mapping) · `SAF-007` (probe dimensions) · whole `06-verification/` plan · `07-manufacturing/ce-technical-file.md` |
| **OP-002** | **What is the target unit cost at volume?** And the retail price position | `TS-001` cannot be scored — cost is criterion C3 and there is no number. Same for TS-002…005 | `01-requirements/constraints.md` · `TS-001`…`TS-005` criteria tables · `00-product/vision.md` success criteria |
| **OP-003** | **What is the damping ratio of a real loaded hammock?** [IF-005](01-requirements/frame-interface-assumptions.md#if-005) | Actuator sizing, the energy budget, and the decay window that `ADR-0005` depends on | `IF-005` · `models/control-loop/tap_and_sustain.py` (ζ is assumed) · `models/spring-mass-dynamics/` · `SYS-004` · `TS-001` · `02-architecture/power-tree.md` |
| **OP-004** | **What amplitude and acceleration are actually safe for an infant?** Needs a clinical or standards basis, not an engineering guess | Bounds the entire control design | [HAZ-003](03-safety/hazard-analysis.md#haz-003) · `SAF-002` · `SYS-001` · `TC-003` · `02-architecture/physics-reference.md` (the acceleration figure) |

---

## Physics and modelling

| ID | Question | Status | How it resolves | Artefacts to fix |
|---|---|---|---|---|
| OP-005 | Does droop alone set frequency? Predicted **1.06 Hz at 22 cm** | open | Measure droop, count bounces over 60 s | `models/spring-mass-dynamics/static-droop-sets-frequency.md` · `00-product/competitive-benchmark.md` |
| OP-006 | Does frequency stay constant when spring count changes but droop is restored? | open | Add/remove one spring, re-measure | Same as OP-005; falsifies the whole droop account if it fails |
| OP-007 | Does the dial change amplitude only, or frequency too? | watching | Count bounces at 10 % and 90 % | `IDEA-005` · `00-product/competitive-benchmark.md` · `02-architecture/operating-modes.md` |
| OP-008 | Are the springs linear, or progressive (hardening)? | open | Check whether frequency shifts at large amplitude | `models/spring-mass-dynamics/` · `02-architecture/physics-reference.md` (linearity assumption) |
| OP-009 | Spring rate and free length | open | Measure | `models/` · `MEC-001` · `IF-004` |
| OP-010 | How long does motion stay detectable after the drive stops? | open | Tap with the unit off, time it | `ADR-0005` (the restart window) · `SAF-008` · `models/control-loop/` |
| OP-011 | Is mechanical power really only ~0.06 W, making standby dominate the 5 W? | open | Measure input power in `Soothe` and in `Armed` | `02-architecture/power-tree.md` (assumes the drive rail dominates) · `SYS-004` · `TS-005` |

## Product and commercial

| ID | Question | Status | Artefacts to fix |
|---|---|---|---|
| OP-012 | Sell the drive unit standalone, or only as a complete set? | blocking `IF-*` | `00-product/project-scope.md` · all `IF-xxx` tolerance bands · `02-architecture/interface-control-document.md` |
| OP-013 | Which member states at launch? | open | `00-product/regulatory-scope.md` · `07-manufacturing/ce-technical-file.md` (language, labelling) |
| OP-014 | Launch volume | open | `01-requirements/constraints.md` · `07-manufacturing/dfm-checklist.md` (second sourcing) |
| OP-015 | Where can we actually differentiate? Owner reports no product deficiency drove this project | open | `00-product/vision.md` "Where we might differentiate" — currently three untested hypotheses |

## Regulatory

| ID | Question | Status | Artefacts to fix |
|---|---|---|---|
| OP-016 | Does the harmonised standard apply to the drive unit standalone, the assembled system, or both? | blocking | `00-product/regulatory-scope.md` · `07-manufacturing/ce-technical-file.md` · the whole verification scope |
| OP-017 | Is a notified body required, or does self-assessment suffice? | open | `07-manufacturing/ce-technical-file.md` |
| OP-018 | Is the Machinery Regulation (EU) 2023/1230 genuinely excluded? | open | `00-product/regulatory-scope.md` · `03-safety/standards-matrix.md` |
| OP-019 | Which EMC harmonised standard applies to a motor-driven childcare appliance? | open | `HW-004` · `06-verification/emc-precompliance-plan.md` · `03-safety/standards-matrix.md` |
| OP-020 | Who is the EU responsible person under GPSR? | open | `07-manufacturing/ce-technical-file.md` |

## Architecture and design decisions

| ID | Question | Status | Artefacts to fix |
|---|---|---|---|
| OP-021 | **Adopt tap-to-start?** `operating-modes.md` already assumes it but no ADR accepts it | open | Needs its own ADR · `02-architecture/operating-modes.md` (marked candidate) · `SYS-001` · `TS-004` |
| OP-022 | Tap detection threshold — a lorry passing must not start it, a gentle tap must | open | `02-architecture/operating-modes.md` · `TS-004` · interacts with `IF-002` |
| OP-023 | Discoverability: a first-time user turns the dial and nothing happens | open | `02-architecture/operating-modes.md` · `SYS-006` · persona P2 |
| OP-024 | Out-of-range load: refuse and indicate, or latch a fault? | open | `02-architecture/operating-modes.md` · `SYS-008` |
| OP-025 | Fault clearing: power cycle only, or a deliberate user action? | open | `02-architecture/operating-modes.md` — power cycling means unplugging something above a sleeping baby |
| OP-026 | How is monitor independence realised? | Phase 4 | Needs an ADR · `02-architecture/ecu-block-diagram.md` · `HW-003` · `SW-003` |
| OP-027 | Does any function need to survive a brief input interruption? | open | `02-architecture/power-tree.md` · `SAF-008` |
| OP-028 | Is a separate supply for the monitor justified? | open | `02-architecture/power-tree.md` · `TS-005` |
| OP-029 | Given no OTA, what is the serviceable local firmware update path? | open | `ADR-0003` follow-on · `07-manufacturing/dfm-checklist.md` |

## Benchmark gaps

| ID | Question | Status | Artefacts to fix |
|---|---|---|---|
| OP-030 | Measured noise floor of the reference units in dB(A) | open | `SYS-002` (the number is `TBD-P3`) · `06-verification/acoustic-test-plan.md` · `TS-001` C1 |
| OP-031 | Competitor A's adapter output voltage — the 35 V capacitor hints above 12 V | open | `ADR-0004` context · `competitive-benchmark.md` |
| OP-032 | Does Competitor A have a safety monitor independent of its MCU? | watching | `teardown/competitor-a/findings.md` (recorded as inconclusive) · context for `SAF-005` |
| OP-033 | Where does the rope terminate — top of the spring stack, or the load below it? | open | `teardown/competitor-a/findings.md` · `IDEA-004` |
| OP-034 | Gear ratio and drum diameter | open | `teardown/competitor-a/findings.md` · needed to convert motor revs to cable travel |
| OP-035 | What does Competitor C's "self-learning" motor actually do? | open | `competitive-benchmark.md` · `00-product/vision.md` differentiation hypothesis |
| OP-036 | Actuation approach of Competitors B and C | open | `competitive-benchmark.md` · `TS-001` candidate list |

---

## The `TBD` markers

62 `TBD` placeholders remain in `docs/`, each a number that must come from a phase:

| Marker | Meaning | Count |
|---|---|---:|
| `TBD-P2` | Phase 2 modelling must produce it | 26 |
| `TBD-P3` | Phase 3 analysis must produce it | 20 |
| `TBD-P4` | Phase 4 design must produce it | 16 |

Heaviest concentrations: `frame-interface-assumptions.md` (15), `power-tree.md` (12),
`srs-system.md` (10). **A requirement containing a `TBD` may not be set to `approved`** — see
[why TBDs are deliberate](01-requirements/index.md#tbd-values-are-deliberate).

## Working rule

When an open point is answered:

1. Record the answer where it belongs — a requirement, an ADR, the benchmark
2. **Fix every artefact in its row**, not just the obvious one
3. Re-run `python tools/check_requirements.py` and `python tools/gen_traceability.py`
4. Strike the row here, or move it to a resolved section with the date

The second step is the one that gets skipped, and it is why this column exists.
