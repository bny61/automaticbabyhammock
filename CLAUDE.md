# Working agreement for AI agents

This repository develops the **electronic control unit (ECU) for an automatic baby hammock**
(a motorised *Federwiege* drive unit) as a real, sellable EU product.

**A defect in this product can kill an infant.** The unit hangs directly above a sleeping baby
and carries its full weight. Treat every rule below as binding.

---

## 1. The core discipline: decisions are outputs, not inputs

Hardware choices — MCU, actuator, motor driver, sensors, topology — are **deliberately not made
yet**. They are decided in Phase 4, as the recorded outcome of a trade study, against requirements
that Phase 2 modelling has quantified.

- **Never** pick a part, MCU or actuator because it seems reasonable. If a decision is needed,
  open a trade study (`docs/05-trade-studies/`) and close it with an ADR (`docs/04-decisions/`).
- **Never** write firmware that assumes a platform before the MCU-selection ADR exists (expected `ADR-0006`, from `TS-002`).
- If work is blocked on an undecided question, say so and name the ADR/TS that must land first.
  Being blocked is a valid, useful outcome. Guessing is not.

## 2. Requirement IDs

| Prefix | Meaning | Root? |
|---|---|---|
| `UN-xxx`   | User need | yes |
| `HAZ-xxx`  | Hazard | yes |
| `SYS-xxx`  | System requirement | no |
| `HW-xxx`   | Electrical requirement | no |
| `SW-xxx`   | Software requirement | no |
| `MEC-xxx`  | Mechanical requirement (in scope: housing, load path, spring pack) | no |
| `IF-xxx`   | Assumption about the out-of-scope stand/hammock | no |
| `SAF-xxx`  | Safety requirement (must cite the `HAZ-xxx` it mitigates) | no |
| `TC-xxx`   | Test case | no |
| `ADR-xxxx` | Architecture decision record | — |
| `TS-xxx`   | Trade study | — |

Rules:

- **Never invent an ID** that is not already allocated, and never reuse a retired one.
  Allocate the next free number with `python tools/new_req.py <PREFIX>`.
- Every non-root requirement needs a `parent` that resolves to a real ID.
- Every requirement needs a `verification` method: `A`nalysis, `I`nspection, `T`est, `D`emonstration.
- Every `SAF-xxx` needs a `mitigates:` field naming a `HAZ-xxx`, **and** a verification method,
  before its PR may be merged.
- Run `python tools/check_requirements.py` before every commit that touches `docs/`.

## 3. Traceability is generated, never hand-written

`docs/01-requirements/traceability-matrix.md` is produced by `python tools/gen_traceability.py`.
**Do not edit it by hand.** If the matrix looks wrong, the requirements are wrong — fix those.

## 4. ADRs are immutable

An ADR with `status: accepted` is never edited. To change a decision, write a new ADR that
supersedes it, and set the old one to `status: superseded by ADR-xxxx`.

## 5. The scope boundary

**In scope:** the inline drive unit — electronics, firmware, housing, load path, spring pack,
hooks and retention.

**Out of scope:** the stand / ceiling mount, and the hammock textile and mattress.

Everything the ECU assumes about those out-of-scope parts goes into
`docs/02-architecture/interface-control-document.md` as an `IF-xxx` **with a tolerance band**.
Never hardcode a stand or hammock property in firmware, a calculation or a model — reference the
`IF-xxx`. A known field failure of a competitor product is exactly this: the drive unit coupling
into a stand that has its own resonance.

## 6. Bill of materials

No part may appear in a schematic or BOM without a row in
`hardware/component-selection/part-selection-matrix.md` covering function, cost @1k, lifecycle
status, second source, stock and RoHS/REACH status.

## 7. Pull requests

Every PR touching `hardware/`, `firmware/` or `mechanical/` must state **which requirement IDs it
implements or changes**. A PR that implements no requirement needs an explanation of why.

## 8. Product-defining facts (do not contradict these without an ADR)

- The motion is **vertical bounce on springs** — a driven mass-spring oscillator at resonance.
  It is **not** a pendulum and **not** lateral swinging.
- The unit is a **load-bearing structural element suspended above an infant**. Load-path failure
  is the lead hazard; single-fault tolerance (redundant springs) is the competitive floor.
- Power comes from an **external 12 V SELV adapter**. Mains never reaches this board, which keeps
  the ECU out of Low Voltage Directive scope. Do not design a mains-side supply.
- **Silence is the primary competitive axis** and average power is roughly **5 W**. Both are hard
  constraints that eliminate actuator families, not aspirations.
- **Wireless is a market negative** in this segment; the benchmark UI is a rotary dial on the unit.
  Adding a radio triggers Radio Equipment Directive obligations including mandatory cybersecurity
  requirements. See `ADR-0003`.
- Load range is **3–18 kg**, birth to ~2 years, twins supported. Continuous duty, no time limit.

## 9. Standards and claims

Regulatory statements must cite the specific standard and clause in
`docs/03-safety/standards-matrix.md`. Do not assert compliance — assert *intended* compliance plus
the verification that will demonstrate it. Only a test report demonstrates compliance.

## 10. Brainstorming

Half-formed thinking belongs in `brainstorming/`, not in `docs/`. Run `/brainstorm` to interview
the user and capture ideas and sketches there.

Nothing in `brainstorming/` is authoritative and none of it may be cited as the basis for a
design. An idea graduates by becoming an ADR, a trade study, a requirement or a hazard — and a
hazard graduates **immediately**, not at the end of a session.

## 11. Style

Requirements use "shall". Goals use "should". Never use "shall" for something that is not
verifiable. If you cannot write the verification method, the requirement is not yet a requirement.
