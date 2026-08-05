# TS-002 — Control processor selection

```
Status:     open
Owner:      TBD
Decides:    an ADR (number allocated when written)
Blocked on: TS-001 (actuation concept sets the control problem); Phase 3 SW timing budget
```

## Question

What processor runs the estimation, control and user-interface software?

## Why it cannot be decided by inspection

The obvious answer — a popular hobby-friendly module — is disqualified by two constraints that are
easy to overlook. [ADR-0003](../04-decisions/ADR-0003-connectivity-stance.md) removes any need for
wireless, which eliminates the usual reason for picking a connected SoC. And
[SAF-005](../01-requirements/safety-requirements.md#saf-005) requires a drive-disable path that does
**not** depend on this processor working, which makes "how cleanly does the platform support an
independent monitor" a first-class selection criterion rather than an afterthought.

## Criteria

| # | Criterion | Derived from |
|---|---|---|
| C1 | Deterministic timing; low interrupt latency and jitter | [SW-001](../01-requirements/srs-software.md#sw-001) |
| C2 | Supports an independent drive-disable path cleanly | [SAF-005](../01-requirements/safety-requirements.md#saf-005), [HW-003](../01-requirements/srs-electrical.md#hw-003) |
| C3 | Peripherals matched to the actuation concept | TS-001 |
| C4 | Analogue front end adequate for the sensing approach | TS-004 |
| C5 | Host-side testability of control and safety logic | [Software architecture](../02-architecture/software-architecture.md#testability) |
| C6 | Power at the operating point | [SYS-004](../01-requirements/srs-system.md#sys-004) |
| C7 | Lifecycle, availability, second source | Part selection matrix (`hardware/component-selection/part-selection-matrix.md`) |
| C8 | Cost at volume | Cost target — not yet set |
| C9 | Toolchain, static analysis and long-term maintainability | No OTA — see below |

**Elimination:** no wireless requirement exists, so integrated radio is not a criterion and its
cost and complexity count against a candidate rather than for it.

## The constraint that changes the shortlist

[ADR-0003](../04-decisions/ADR-0003-connectivity-stance.md) means **there is no over-the-air update
path**. A firmware defect found in the field cannot be fixed remotely. That raises the weight on
C5 (host-side testability) and C9 (toolchain and static analysis) well above where they would
normally sit, because pre-release verification has to carry the load that OTA usually shares.

## Not yet a candidate list

Deliberately empty. Populating it before TS-001 closes would mean choosing a processor before
knowing the control problem it has to solve.
