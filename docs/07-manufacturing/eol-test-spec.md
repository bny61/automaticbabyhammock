# End-of-line test specification

!!! note "Phase 5 deliverable — principles only at Phase 0"

## Principle

**Every safety function is tested on every unit.** Sampling is acceptable for performance
characteristics; it is not acceptable for the functions that stand between a fault and an infant.

This principle has a design consequence, which is why it is written down now rather than in
Phase 5: safety functions must be **testable in a fixture, in seconds, without dismantling the
unit**. Retrofitting testability into a finished design is expensive and usually results in the
test being weakened instead.

## Test groups

| Group | Verifies | Every unit? |
|---|---|---|
| Power-on and self-test | Basic function | Yes |
| Sensing calibration and range | [TS-004](../05-trade-studies/TS-004-sensing-approach.md) outcome | Yes |
| **Independent drive disable** | [SAF-005](../01-requirements/safety-requirements.md#saf-005) | **Yes** |
| **Amplitude limit** | [SAF-002](../01-requirements/safety-requirements.md#saf-002) | **Yes** |
| **Occupancy detection and stop** | [SAF-004](../01-requirements/safety-requirements.md#saf-004) | **Yes** |
| Thermal protection trip | [SAF-006](../01-requirements/safety-requirements.md#saf-006) | Yes, by stimulus injection |
| Load path proof | [SAF-001](../01-requirements/safety-requirements.md#saf-001) | Proof load every unit; destructive test by sample |
| Acoustic | [SYS-002](../01-requirements/srs-system.md#sys-002) | Sample — needs a quiet environment |
| Firmware version and serial programming | Traceability, GPSR | Yes |

## The awkward one

**Acoustic testing cannot realistically be done on every unit** — it needs an environment quieter
than a factory. But noise is the product's main competitive claim and a plausible failure mode for
an individual unit (a rubbing part, a loose fastener, a bearing defect).

A proxy is needed: vibration signature, motor current signature, or an accelerometer measurement in
the fixture, correlated against acoustic measurements during development. **Establishing that
correlation is development work that must happen before production**, and it is easy to leave too
late. Flagged here for that reason.

## Records

Results retained per serial number, linked to batch records for load-bearing parts. Required for
GPSR traceability and essential for bounding any future field issue to the affected units rather
than the whole population.
