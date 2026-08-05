# Standards matrix

Maps standard and clause to the requirement that implements it and the verification that
demonstrates it. This table is the backbone of the
[CE technical file](../07-manufacturing/ce-technical-file.md).

!!! warning "Blocked on ADR-0001"
    The product-safety standard cannot be filled in until
    [ADR-0001](../04-decisions/ADR-0001-product-positioning.md) selects it. The horizontal
    legislation below applies regardless and can be worked now.

!!! danger "Nothing here is a compliance claim"
    Entries record *intended* compliance and the evidence that will demonstrate it. Only a test
    report demonstrates compliance.

## Product-safety standard — pending ADR-0001

| Candidate | Applies if | Status |
|---|---|---|
| EN 1130:2019 (cribs, incl. suspended cribs) | Marketed for sleep | Candidate |
| EN 16232:2013+A1:2018 (infant swings) | Supervised, awake-time use | Candidate |
| EN 12790-1:2023 (reclined cradles) | Reclined lying surface | Candidate |

Clause-level mapping begins once one is selected. Note that the entrapment probe dimensions in
[SAF-007](../01-requirements/safety-requirements.md#saf-007) come from whichever is chosen — which
is one reason the decision blocks requirements work.

## Horizontal legislation — applies regardless

| Instrument | Applies to | Requirement | Verification | Status |
|---|---|---|---|---|
| EMC 2014/30/EU | Whole unit | [HW-004](../01-requirements/srs-electrical.md#hw-004) | [EMC pre-compliance](../06-verification/emc-precompliance-plan.md) then accredited test | Open |
| LVD 2014/35/EU | **Expected out of scope** | [HW-001](../01-requirements/srs-electrical.md#hw-001) | Inspection: no mains on the ECU | [ADR-0002](../04-decisions/ADR-0002-power-input-strategy.md) |
| RED 2014/53/EU | **Not applicable** | — | Inspection: no radio fitted | [ADR-0003](../04-decisions/ADR-0003-connectivity-stance.md) |
| GPSR (EU) 2023/988 | Whole product | Technical file, traceability, responsible person | Documentation review | Open |
| RoHS 2011/65/EU | All components | Part selection | Supplier declarations | Open |
| REACH 1907/2006 | Materials | Material selection | SVHC declaration | Open |
| WEEE 2012/19/EU | Whole unit | Marking, registration | Inspection | Open |
| Machinery (EU) 2023/1230 | **To confirm** | — | Regulatory determination needed | Open |
| Ecodesign (external PSU) | Adapter | Adapter selection | Supplier declaration | Open |

## How to use this table

1. When a standard clause is identified, add a row naming the clause
2. Write or link the requirement that implements it — allocate an ID if none exists
3. Name the verification that will demonstrate it, and link the `TC-xxx`
4. When evidence exists, link the test report

A clause with no requirement is a gap. A requirement with no verification is not a requirement.
