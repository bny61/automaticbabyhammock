# Traceability matrix

!!! danger "Generated file — do not edit"
    Produced by `python tools/gen_traceability.py` from the requirement blocks in
    `docs/`. Hand edits are overwritten. If something here is wrong, fix the
    requirement that produced it.


## Summary

| Type | Count | Approved | Draft |
|---|---:|---:|---:|
| `UN` | 9 | 0 | 9 |
| `HAZ` | 8 | 0 | 8 |
| `SYS` | 10 | 0 | 10 |
| `HW` | 4 | 0 | 4 |
| `SW` | 4 | 0 | 4 |
| `MEC` | 5 | 0 | 5 |
| `IF` | 6 | 0 | 6 |
| `SAF` | 8 | 0 | 8 |
| `TC` | 3 | 0 | 3 |

**Total:** 57 requirement(s).

## User needs → system requirements

| User need | Title | Derived requirements |
|---|---|---|
| [UN-001](../00-product/user-needs.md#un-001) | Soothe a waking baby back to sleep without the parent getting up | [SYS-001](../01-requirements/srs-system.md#sys-001) |
| [UN-002](../00-product/user-needs.md#un-002) | Not be woken by the device itself | [SYS-002](../01-requirements/srs-system.md#sys-002) |
| [UN-003](../00-product/user-needs.md#un-003) | Trust that the unit cannot drop my baby | [SYS-009](../01-requirements/srs-system.md#sys-009) |
| [UN-004](../00-product/user-needs.md#un-004) | Run all night without a time limit | [SYS-003](../01-requirements/srs-system.md#sys-003) |
| [UN-005](../00-product/user-needs.md#un-005) | Control it half-asleep, without a phone | [SYS-006](../01-requirements/srs-system.md#sys-006) |
| [UN-006](../00-product/user-needs.md#un-006) | Work with the stand and hammock I already own | [SYS-007](../01-requirements/srs-system.md#sys-007) |
| [UN-007](../00-product/user-needs.md#un-007) | Suit my baby from birth through toddlerhood, including twins | [SYS-005](../01-requirements/srs-system.md#sys-005)<br>[SYS-010](../01-requirements/srs-system.md#sys-010) |
| [UN-008](../00-product/user-needs.md#un-008) | Cost almost nothing to run | [SYS-004](../01-requirements/srs-system.md#sys-004) |
| [UN-009](../00-product/user-needs.md#un-009) | Have it stop when my baby is not in it | [SYS-008](../01-requirements/srs-system.md#sys-008) |

## Hazards → safety requirements

| Hazard | Title | Severity | Mitigated by | Verified by |
|---|---|---|---|---|
| [HAZ-001](../03-safety/hazard-analysis.md#haz-001) | Load-path failure releases the baby | catastrophic | [SAF-001](../01-requirements/safety-requirements.md#saf-001) | [TC-001](../06-verification/test-cases/index.md#tc-001) |
| [HAZ-002](../03-safety/hazard-analysis.md#haz-002) | Resonance coupling with the supporting structure causes runaway amplitude | critical | [SAF-003](../01-requirements/safety-requirements.md#saf-003) | — *none* |
| [HAZ-003](../03-safety/hazard-analysis.md#haz-003) | Excessive amplitude or acceleration harms the infant | critical | [SAF-002](../01-requirements/safety-requirements.md#saf-002) | — *none* |
| [HAZ-004](../03-safety/hazard-analysis.md#haz-004) | Continued operation with no occupant or an incorrect load | marginal | [SAF-004](../01-requirements/safety-requirements.md#saf-004) | — *none* |
| [HAZ-005](../03-safety/hazard-analysis.md#haz-005) | Entrapment or entanglement | catastrophic | [SAF-007](../01-requirements/safety-requirements.md#saf-007) | — *none* |
| [HAZ-006](../03-safety/hazard-analysis.md#haz-006) | Motor or control runaway | critical | [SAF-002](../01-requirements/safety-requirements.md#saf-002)<br>[SAF-003](../01-requirements/safety-requirements.md#saf-003)<br>[SAF-005](../01-requirements/safety-requirements.md#saf-005) | [TC-002](../06-verification/test-cases/index.md#tc-002) |
| [HAZ-007](../03-safety/hazard-analysis.md#haz-007) | Thermal hazard under continuous duty | critical | [SAF-006](../01-requirements/safety-requirements.md#saf-006) | — *none* |
| [HAZ-008](../03-safety/hazard-analysis.md#haz-008) | Unexpected restart after power interruption | marginal | [SAF-008](../01-requirements/safety-requirements.md#saf-008) | — *none* |

## Full matrix

| ID | Title | Status | Parent | Verif. | Verified by |
|---|---|---|---|---|---|
| [HAZ-001](../03-safety/hazard-analysis.md#haz-001) | Load-path failure releases the baby | `draft` | *root* | — | — *none* |
| [HAZ-002](../03-safety/hazard-analysis.md#haz-002) | Resonance coupling with the supporting structure causes runaway amplitude | `draft` | *root* | — | — *none* |
| [HAZ-003](../03-safety/hazard-analysis.md#haz-003) | Excessive amplitude or acceleration harms the infant | `draft` | *root* | — | — *none* |
| [HAZ-004](../03-safety/hazard-analysis.md#haz-004) | Continued operation with no occupant or an incorrect load | `draft` | *root* | — | — *none* |
| [HAZ-005](../03-safety/hazard-analysis.md#haz-005) | Entrapment or entanglement | `draft` | *root* | — | — *none* |
| [HAZ-006](../03-safety/hazard-analysis.md#haz-006) | Motor or control runaway | `draft` | *root* | — | — *none* |
| [HAZ-007](../03-safety/hazard-analysis.md#haz-007) | Thermal hazard under continuous duty | `draft` | *root* | — | — *none* |
| [HAZ-008](../03-safety/hazard-analysis.md#haz-008) | Unexpected restart after power interruption | `draft` | *root* | — | — *none* |
| [HW-001](../01-requirements/srs-electrical.md#hw-001) | SELV input only | `draft` | [SYS-004](../01-requirements/srs-system.md#sys-004) | I | — *none* |
| [HW-002](../01-requirements/srs-electrical.md#hw-002) | Input protection | `draft` | [SAF-005](../01-requirements/safety-requirements.md#saf-005) | T | — *none* |
| [HW-003](../01-requirements/srs-electrical.md#hw-003) | Drive disable independent of the control processor | `draft` | [SAF-005](../01-requirements/safety-requirements.md#saf-005) | T | [TC-002](../06-verification/test-cases/index.md#tc-002) |
| [HW-004](../01-requirements/srs-electrical.md#hw-004) | Electromagnetic compatibility | `draft` | [SYS-001](../01-requirements/srs-system.md#sys-001) | T | — *none* |
| [IF-001](../01-requirements/frame-interface-assumptions.md#if-001) | Suspension point static strength | `draft` | [SYS-007](../01-requirements/srs-system.md#sys-007) | A | — *none* |
| [IF-002](../01-requirements/frame-interface-assumptions.md#if-002) | Supporting structure resonance | `draft` | [SYS-007](../01-requirements/srs-system.md#sys-007) | T | — *none* |
| [IF-003](../01-requirements/frame-interface-assumptions.md#if-003) | Suspension geometry | `draft` | [SYS-007](../01-requirements/srs-system.md#sys-007) | I | — *none* |
| [IF-004](../01-requirements/frame-interface-assumptions.md#if-004) | Hammock attachment and mass | `draft` | [SYS-007](../01-requirements/srs-system.md#sys-007) | I | — *none* |
| [IF-005](../01-requirements/frame-interface-assumptions.md#if-005) | Damping contributed by the hammock and occupant | `draft` | [SYS-001](../01-requirements/srs-system.md#sys-001) | A | — *none* |
| [IF-006](../01-requirements/frame-interface-assumptions.md#if-006) | Installation environment | `draft` | [SYS-003](../01-requirements/srs-system.md#sys-003) | A | — *none* |
| [MEC-001](../01-requirements/srs-mechanical.md#mec-001) | Fatigue life of the load path | `draft` | [SYS-009](../01-requirements/srs-system.md#sys-009) | T | — *none* |
| [MEC-002](../01-requirements/srs-mechanical.md#mec-002) | Retention after single-element failure | `draft` | [SYS-009](../01-requirements/srs-system.md#sys-009) | T | [TC-001](../06-verification/test-cases/index.md#tc-001) |
| [MEC-003](../01-requirements/srs-mechanical.md#mec-003) | Closed spring geometry | `draft` | [SAF-007](../01-requirements/safety-requirements.md#saf-007) | I | — *none* |
| [MEC-004](../01-requirements/srs-mechanical.md#mec-004) | Structural noise | `draft` | [SYS-002](../01-requirements/srs-system.md#sys-002) | T | [TC-003](../06-verification/test-cases/index.md#tc-003) |
| [MEC-005](../01-requirements/srs-mechanical.md#mec-005) | Housing and thermal envelope | `draft` | [SAF-006](../01-requirements/safety-requirements.md#saf-006) | T | — *none* |
| [SAF-001](../01-requirements/safety-requirements.md#saf-001) | Redundant load path | `draft` | [SYS-009](../01-requirements/srs-system.md#sys-009) | T | [TC-001](../06-verification/test-cases/index.md#tc-001) |
| [SAF-002](../01-requirements/safety-requirements.md#saf-002) | Independent amplitude limit | `draft` | [SYS-001](../01-requirements/srs-system.md#sys-001) | T | — *none* |
| [SAF-003](../01-requirements/safety-requirements.md#saf-003) | Detection of abnormal motion | `draft` | [SYS-001](../01-requirements/srs-system.md#sys-001) | T | — *none* |
| [SAF-004](../01-requirements/safety-requirements.md#saf-004) | Stop on loss of occupancy | `draft` | [SYS-008](../01-requirements/srs-system.md#sys-008) | T | — *none* |
| [SAF-005](../01-requirements/safety-requirements.md#saf-005) | Independent drive disable | `draft` | [SYS-001](../01-requirements/srs-system.md#sys-001) | T | [TC-002](../06-verification/test-cases/index.md#tc-002) |
| [SAF-006](../01-requirements/safety-requirements.md#saf-006) | Thermal protection | `draft` | [SYS-003](../01-requirements/srs-system.md#sys-003) | T | — *none* |
| [SAF-007](../01-requirements/safety-requirements.md#saf-007) | No entrapment or entanglement points | `draft` | [SYS-009](../01-requirements/srs-system.md#sys-009) | I | — *none* |
| [SAF-008](../01-requirements/safety-requirements.md#saf-008) | Defined behaviour on power restoration | `draft` | [SYS-001](../01-requirements/srs-system.md#sys-001) | T | — *none* |
| [SW-001](../01-requirements/srs-software.md#sw-001) | Deterministic control timing | `draft` | [SYS-001](../01-requirements/srs-system.md#sys-001) | T | — *none* |
| [SW-002](../01-requirements/srs-software.md#sw-002) | Safe state on fault | `draft` | [SAF-005](../01-requirements/safety-requirements.md#saf-005) | T | — *none* |
| [SW-003](../01-requirements/srs-software.md#sw-003) | Amplitude limit enforced independently of the control loop | `draft` | [SAF-002](../01-requirements/safety-requirements.md#saf-002) | T | [TC-002](../06-verification/test-cases/index.md#tc-002) |
| [SW-004](../01-requirements/srs-software.md#sw-004) | Plausibility checking of sensor inputs | `draft` | [SAF-003](../01-requirements/safety-requirements.md#saf-003) | T | — *none* |
| [SYS-001](../01-requirements/srs-system.md#sys-001) | Sustain bounce motion at the hammock's resonant frequency | `draft` | [UN-001](../00-product/user-needs.md#un-001) | T | — *none* |
| [SYS-002](../01-requirements/srs-system.md#sys-002) | Acoustic emission | `draft` | [UN-002](../00-product/user-needs.md#un-002) | T | [TC-003](../06-verification/test-cases/index.md#tc-003) |
| [SYS-003](../01-requirements/srs-system.md#sys-003) | Continuous duty | `draft` | [UN-004](../00-product/user-needs.md#un-004) | T | — *none* |
| [SYS-004](../01-requirements/srs-system.md#sys-004) | Average power consumption | `draft` | [UN-008](../00-product/user-needs.md#un-008) | T | — *none* |
| [SYS-005](../01-requirements/srs-system.md#sys-005) | Rated load range | `draft` | [UN-007](../00-product/user-needs.md#un-007) | T | — *none* |
| [SYS-006](../01-requirements/srs-system.md#sys-006) | On-unit control without connectivity | `draft` | [UN-005](../00-product/user-needs.md#un-005) | D | — *none* |
| [SYS-007](../01-requirements/srs-system.md#sys-007) | Compatibility with third-party stands and hammocks | `draft` | [UN-006](../00-product/user-needs.md#un-006) | A | — *none* |
| [SYS-008](../01-requirements/srs-system.md#sys-008) | Occupancy detection and automatic stop | `draft` | [UN-009](../00-product/user-needs.md#un-009) | T | — *none* |
| [SYS-009](../01-requirements/srs-system.md#sys-009) | Single-fault tolerance of the load path | `draft` | [UN-003](../00-product/user-needs.md#un-003) | T | [TC-001](../06-verification/test-cases/index.md#tc-001) |
| [SYS-010](../01-requirements/srs-system.md#sys-010) | Adaptation to changing load | `draft` | [UN-007](../00-product/user-needs.md#un-007) | T | — *none* |
| [UN-001](../00-product/user-needs.md#un-001) | Soothe a waking baby back to sleep without the parent getting up | `draft` | *root* | — | — *none* |
| [UN-002](../00-product/user-needs.md#un-002) | Not be woken by the device itself | `draft` | *root* | — | — *none* |
| [UN-003](../00-product/user-needs.md#un-003) | Trust that the unit cannot drop my baby | `draft` | *root* | — | — *none* |
| [UN-004](../00-product/user-needs.md#un-004) | Run all night without a time limit | `draft` | *root* | — | — *none* |
| [UN-005](../00-product/user-needs.md#un-005) | Control it half-asleep, without a phone | `draft` | *root* | — | — *none* |
| [UN-006](../00-product/user-needs.md#un-006) | Work with the stand and hammock I already own | `draft` | *root* | — | — *none* |
| [UN-007](../00-product/user-needs.md#un-007) | Suit my baby from birth through toddlerhood, including twins | `draft` | *root* | — | — *none* |
| [UN-008](../00-product/user-needs.md#un-008) | Cost almost nothing to run | `draft` | *root* | — | — *none* |
| [UN-009](../00-product/user-needs.md#un-009) | Have it stop when my baby is not in it | `draft` | *root* | — | — *none* |

## Coverage gaps

**System requirements not yet decomposed:**<br>`SYS-005`, `SYS-006`, `SYS-010`
