# Requirements — overview

## The ID scheme

| Prefix | Meaning | Root? | Needs |
|---|---|---|---|
| `UN-xxx` | User need | yes | — |
| `HAZ-xxx` | Hazard | yes | `severity`, `probability` |
| `SYS-xxx` | System requirement | no | `parent`, `verification` |
| `HW-xxx` | Electrical requirement | no | `parent`, `verification` |
| `SW-xxx` | Software requirement | no | `parent`, `verification` |
| `MEC-xxx` | Mechanical requirement (in scope) | no | `parent`, `verification` |
| `IF-xxx` | Assumption about the out-of-scope stand or hammock | no | `parent`, `verification`, **`tolerance`** |
| `SAF-xxx` | Safety requirement | no | `parent`, `verification`, **`mitigates`** |
| `TC-xxx` | Test case | no | `parent`, **`verifies`** |

IDs are allocated with `python tools/new_req.py <PREFIX>`, never by hand, and are never reused.

## The format

One requirement per level-3 heading, followed by a metadata block, then the statement and its
rationale:

````markdown
### SYS-014 — Continuous operation without thermal derating {#sys-014}

```yaml
id: SYS-014
status: draft
parent: UN-004
verification: T
```

The ECU shall operate continuously at maximum rated load for at least 12 h without
reducing bounce amplitude.

**Rationale:** Benchmark units advertise unlimited operating duration; parents use the
product for full night sleeps.
````

## Rules

- **"Shall" is binding; "should" is a goal.** The linter rejects a `SYS`/`HW`/`SW`/`MEC`/`SAF`
  requirement that does not say "shall".
- **If you cannot state the verification method, it is not a requirement yet.** `A`nalysis,
  `I`nspection, `T`est, `D`emonstration.
- **Requirements state *what*, not *how*.** "Shall detect loss of occupancy within 2 s" is a
  requirement. "Shall use a load cell" is a design decision and belongs in an
  [ADR](../04-decisions/index.md).
- **Every non-root requirement needs a parent that resolves.** No orphans.
- **Safety requirements name the hazard they mitigate**, or they are not safety requirements.
- **User needs are validated, not verified** — they carry no verification method.

## Lifecycle

`draft` → `review` → `approved` → (`obsolete`)

Only `approved` requirements may be cited as the basis for a design. Everything in this repository
is currently `draft`: the real requirements work happens in Phase 3, after the
[modelling](../02-architecture/system-architecture.md) has produced defensible numbers.

## TBD values are deliberate

Many seeded requirements contain `TBD-P2` or `TBD-P3` instead of a number. This is intentional and
correct: those numbers are **outputs of Phase 2 modelling and Phase 3 analysis**. Filling them in
now with plausible-looking guesses would be worse than leaving them empty, because a guess that
survives into Phase 4 silently becomes the specification.

A requirement with a `TBD` may not be set to `approved`.

## Checking your work

```bash
python tools/check_requirements.py     # lint
python tools/gen_traceability.py       # regenerate the matrix
```

The [traceability matrix](traceability-matrix.md) is generated. If it looks wrong, the
requirements are wrong.
