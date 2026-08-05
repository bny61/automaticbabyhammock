# Design FMEA

!!! note "Phase 3 deliverable — structure only at Phase 0"
    A meaningful DFMEA needs a design to analyse. This page fixes the method and the scale now, so
    that Phase 3 does not spend its time arguing about ratings.

## Scope

Design FMEA of the drive unit: load path, spring pack, actuator and mounting, electronics, sensing,
firmware and user interface.

The load path is analysed **first and most thoroughly**. It carries the only catastrophic hazard
([HAZ-001](hazard-analysis.md#haz-001)) and, unlike the electronics, has no second line of defence
behind it.

## Method

For each element: failure mode → effect → cause → current control → severity, occurrence, detection
→ RPN → action.

### Severity (S)

| S | Meaning |
|---:|---|
| 10 | Death or life-changing injury to the infant |
| 8–9 | Injury requiring medical attention |
| 5–7 | Minor injury or significant distress |
| 2–4 | Product does not perform; no injury |
| 1 | Nuisance only |

### Occurrence (O) and Detection (D)

Scales to be calibrated in Phase 3 against field data and component reliability figures. Detection
refers to detection **before harm**, whether by the unit, in production test, or by the user.

## Action rules

These override RPN ranking, because RPN under-weights rare catastrophic events — which are exactly
the ones that matter here:

1. **Any failure mode with S = 10 requires action**, regardless of O, D or RPN
2. **Any single failure mode that releases the load requires design change**, not a detection
   control — see [SAF-001](../01-requirements/safety-requirements.md#saf-001)
3. **Detection by the user is not an acceptable primary control** for S ≥ 8. The user is asleep
4. Actions producing new requirements must allocate a `SAF-xxx` and re-run the traceability matrix

## Table

To be produced in Phase 3.

| Item | Failure mode | Effect | Cause | Control | S | O | D | RPN | Action |
|---|---|---|---|---|---:|---:|---:|---:|---|
| | | | | | | | | | |

## Inputs required

The [hazard analysis](hazard-analysis.md) (exists, draft) · a candidate design from Phase 4 ·
component reliability data · Phase 2 load-cycle counts (`models`) for the fatigue analysis
that [MEC-001](../01-requirements/srs-mechanical.md#mec-001) depends on.
