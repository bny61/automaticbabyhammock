# Project status

**As of 2026-08-06.** Single source of truth for where the project stands. The phase table in the
repository `README.md` mirrors this page; if the two disagree, this page is right.

!!! note "How the numbers here are produced"
    Every count below is checkable, not asserted:

    ```bash
    python tools/check_requirements.py     # requirement counts and link integrity
    python tools/list_open_points.py       # TBD markers and register cross-check
    python tools/gen_traceability.py       # matrix freshness
    ```

## One-line summary

Phase 0 is complete and Phases 1–3 are **in progress in parallel**: the product definition,
physics modelling and hazard analysis all exist in draft. **No requirement is approved, no trade
study is closed, and no hardware is chosen** — which is the intended state, because the two
decisions that gate everything downstream ([OP-001](open-points.md), [OP-002](open-points.md))
are still open.

## Phase status

| Phase | Content | Status | Evidence |
|---|---|---|---|
| 0 | Repository scaffold, tooling, conventions | ✅ complete | linter, traceability generator, open-points tool, CI, MkDocs site all in place |
| 1 | Product definition, regulatory positioning, benchmark | 🟡 in progress | vision, scope, personas, stakeholders, 9 `UN`, benchmark incl. a first-hand teardown, regulatory scope — but `ADR-0001` is still `proposed` and there is **no cost target** |
| 2 | Interface control document, physics & control modelling | 🟡 in progress | ICD with 6 `IF`, [physics reference](02-architecture/physics-reference.md), static-droop model, tap-and-sustain simulation — 26 `TBD-P2` remain, all needing measurement |
| 3 | Hazard analysis, DFMEA, requirements | 🟡 in progress | 9 `HAZ`, 9 `SAF`, safety concept, full SRS set in draft — DFMEA is method-only, 20 `TBD-P3` remain |
| 4 | Architecture and trade studies — **hardware chosen here** | ⬜ scaffolded, not started | `TS-001`…`TS-005` written but all `open`; `TS-001` cannot be scored without a cost target |
| 5 | Schematic, PCB, firmware, mechanical design | ⬜ not started | `hardware/`, `firmware/`, `mechanical/` hold structure only |

Phases 1–3 overlapping is deliberate: hazards are a root of traceability alongside user needs, so
Phase 3 cannot wait for Phase 1 to close, and Phase 2 measurements are what turn Phase 3's `TBD`s
into numbers.

## Artefact counts

| | Count | Note |
|---|---:|---|
| Requirements parsed by the linter | 59 | `UN` 9 · `HAZ` 9 · `SYS` 10 · `HW` 4 · `SW` 4 · `MEC` 5 · `IF` 6 · `SAF` 9 · `TC` 3 |
| Requirements at `approved` | **0** | all are `draft`; a requirement containing a `TBD` may not be approved |
| Linter errors | 0 | `check_requirements.py` passes |
| `TBD` markers in `docs/` | 62 | `TBD-P2` 26 · `TBD-P3` 20 · `TBD-P4` 16 |
| Open points in the register | 36 | `OP-001`…`OP-036` |
| ADRs | 5 | 2 accepted, 3 proposed |
| Trade studies | 5 | all open, none scored |
| Brainstorming ideas awaiting graduation | 5 | `IDEA-001`…`IDEA-005` |

## What is actually decided

Only two decisions are binding — an accepted ADR is immutable and may only be superseded:

| ADR | Decision | Consequence already relied on |
|---|---|---|
| [ADR-0004](04-decisions/ADR-0004-nominal-supply-voltage.md) | Nominal supply of 12 V | `HW-001`, the power tree, the candidate sets in `TS-001`/`TS-003`/`TS-005` |
| [ADR-0005](04-decisions/ADR-0005-behaviour-on-power-restoration.md) | On power restoration the unit sustains, never initiates | `SAF-008`, the operating-mode state machine, `TS-004` |

Three ADRs remain `proposed` — [ADR-0001](04-decisions/ADR-0001-product-positioning.md)
(positioning), [ADR-0002](04-decisions/ADR-0002-power-input-strategy.md) (external SELV adapter)
and [ADR-0003](04-decisions/ADR-0003-connectivity-stance.md) (no radio). Work has been done
consistent with them, so accepting or reversing them is not free.

## What is blocking

Four open points gate the rest of the project. The first two are the ones that stop work outright:

| ID | Question | Why it blocks |
|---|---|---|
| [OP-001](open-points.md) | Sleep product or supervised soothing device? | Selects the harmonised standard, and therefore the permitted geometry, restraint and labelling — i.e. what the product physically is. Closes `ADR-0001` |
| [OP-002](open-points.md) | Target unit cost at volume | `TS-001` weighs acoustics against cost and cannot be scored without it; `TS-002`…`TS-005` inherit the block |
| [OP-003](open-points.md) | Damping ratio of a real loaded hammock | Actuator sizing, the energy budget, and the decay window `ADR-0005` depends on. Currently assumed in the simulation |
| [OP-004](open-points.md) | Safe amplitude and acceleration for an infant | Bounds the whole control design; needs a clinical or standards basis, not an engineering guess |

Two structural gaps sit alongside them:

- **[OP-021](open-points.md) — tap-to-start has no ADR.** `02-architecture/operating-modes.md`
  already assumes it and is marked as carrying a candidate; the assumption is load-bearing for
  `SYS-001` and `TS-004`.
- **The Phase 2 measurement set is untaken.** `OP-005`…`OP-011` are all answerable with a tape
  measure, a stopwatch and a power meter on hardware that is already on hand. They are the
  cheapest open points in the project and they unblock the most `TBD-P2` markers.

## Next actions, in order

1. **Take the Phase 2 bench measurements** (`OP-005`…`OP-011`). No decision is needed to start,
   the equipment is available, and each answer retires several `TBD-P2` markers.
2. **Answer OP-001 and accept or supersede `ADR-0001`.** Everything in Phases 3–5 is written
   against a standard that has not been selected.
3. **Set a cost target (OP-002)**, which unblocks `TS-001` and with it the whole Phase 4 chain.
4. **Write the tap-to-start ADR (OP-021)** so the operating-mode state machine stops resting on
   an undecided candidate.

After any of these lands, run the `impact-auditor` subagent before considering it done — the
open-points register's last column exists because fixing the dependent artefacts is the step that
gets skipped.

## Standing constraints on this status

- No compliance is claimed anywhere in this repository, only *intended* compliance plus the
  verification that will demonstrate it. Nothing above changes that.
- No hardware has been selected, and none may be selected outside a trade study closed by an ADR.
- The traceability matrix is generated. If it looks wrong, the requirements are wrong.
