# TS-005 — Internal power topology

```
Status:     open
Owner:      TBD
Decides:    ADR-0008
Blocked on: TS-001, TS-002, TS-003 — all three define the loads
```

## Question

How are the internal rails generated from the external SELV input, and how is the drive rail
structured to support the actuator's demand profile?

## Why it cannot be decided by inspection

Three requirements conflict:

- **Average efficiency** dominates [SYS-004](../01-requirements/srs-system.md#sys-004), because the
  competitive figure is a *monthly energy cost*. A converter that is excellent at full load and poor
  at the actual average draw fails the requirement while looking good on its datasheet.
- **Switching converters make noise**, both electrically and audibly, in a product whose main
  competitive axis is silence ([SYS-002](../01-requirements/srs-system.md#sys-002)).
- **The monitor rail must not fail with the logic rail**
  ([SAF-005](../01-requirements/safety-requirements.md#saf-005)), which constrains the rail tree
  structure and not merely the component choices.

## Criteria

| # | Criterion | Derived from |
|---|---|---|
| C1 | Efficiency at the typical operating point and in standby | [SYS-004](../01-requirements/srs-system.md#sys-004) |
| C2 | Audible noise contribution | [SYS-002](../01-requirements/srs-system.md#sys-002) |
| C3 | Conducted and radiated emissions | [HW-004](../01-requirements/srs-electrical.md#hw-004) |
| C4 | Supports the actuator's peak/average demand profile | TS-001, TS-003 |
| C5 | Monitor rail independence from the logic rail | [SAF-005](../01-requirements/safety-requirements.md#saf-005) |
| C6 | Behaviour on input interruption and restoration | [SAF-008](../01-requirements/safety-requirements.md#saf-008) |
| C7 | Thermal behaviour under continuous duty | [SAF-006](../01-requirements/safety-requirements.md#saf-006) |
| C8 | Cost and part count | Cost target — not yet set |

## Note on the input voltage

12 V is the benchmark norm, but the nominal input is still open
([HW-001](../01-requirements/srs-electrical.md#hw-001) says `TBD-P4`) because the actuator choice
may argue for 24 V. Decide the input voltage as part of this study, in conjunction with TS-001 —
not before it.
