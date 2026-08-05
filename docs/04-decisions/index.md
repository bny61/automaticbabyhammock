# Architecture decision records

Every significant decision is recorded here: what was decided, what else was considered, why, and
what it costs.

## Register

| ADR | Decision | Status | Blocks |
|---|---|---|---|
| [0001](ADR-0001-product-positioning.md) | Product positioning — sleep product or soothing swing | **proposed** | Everything |
| [0002](ADR-0002-power-input-strategy.md) | External SELV adapter; no mains on the ECU | **proposed** | HW requirements, certification route |
| [0003](ADR-0003-connectivity-stance.md) | No radio; physical control on the unit | **proposed** | TS-002, TS-004, RED applicability |
| [0004](ADR-0004-nominal-supply-voltage.md) | Nominal supply voltage of 12 V | **accepted** | HW-001, TS-001, TS-003, TS-005 |

### Expected in Phase 4

| ADR | Decision | Blocked on |
|---|---|---|
| 0005 | Actuation concept | [TS-001](../05-trade-studies/TS-001-actuation-concept.md) |
| 0006 | Control processor | [TS-002](../05-trade-studies/TS-002-mcu-selection.md) |
| 0007 | Actuator drive topology | [TS-003](../05-trade-studies/TS-003-motor-driver.md) |
| 0008 | Sensing approach | [TS-004](../05-trade-studies/TS-004-sensing-approach.md) |
| 0009 | Internal power topology | [TS-005](../05-trade-studies/TS-005-power-supply.md) |
| 0010 | How monitor independence is realised | Phase 4 architecture |
| 0011 | Behaviour on power restoration | [SAF-008](../01-requirements/safety-requirements.md#saf-008) |

## Rules

1. **Accepted ADRs are immutable.** To change a decision, supersede it.
2. **A decision with one option considered is not a decision.** If there is genuinely no
   alternative, say why.
3. **Every ADR states its negative consequences.** One without them is an advertisement.
4. **Decisions requiring comparison need a [trade study](../05-trade-studies/index.md) first.**
   The ADR records the outcome; the trade study carries the analysis.

```bash
python tools/new_adr.py "Actuation concept"    # allocate the next number
```

## Why ADR-0001 blocks everything

It selects the harmonised standard the product is built to, which determines its permitted
geometry, restraint, stability and labelling — that is, what the product physically is. Any
requirement written before it risks being written against the wrong standard, and any design work
risks being wasted. It is the reason Phase 1 exists as a separate phase.
