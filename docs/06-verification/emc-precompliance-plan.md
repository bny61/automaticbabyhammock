# EMC pre-compliance plan

## Objective

Find EMC problems on the bench, before the accredited laboratory finds them at ten times the cost
and with a schedule impact. Verifies [HW-004](../01-requirements/srs-electrical.md#hw-004).

## Applicable standard

EMC Directive 2014/30/EU applies. The specific harmonised standard is confirmed in Phase 4 once the
topology exists; the household-appliance EN 55014 series is the expected starting point, to be
checked against the current OJEU list rather than assumed.

## The clause that matters most

Immunity testing on this product is not only a compliance exercise. **The unit must never produce
uncommanded motion under disturbance**, and a reset is an acceptable response only if the reset
state is safe — which is what [SAF-008](../01-requirements/safety-requirements.md#saf-008) is for.

Pass criteria must therefore be written in terms of *observed motion and safe state*, not only in
terms of continued function. A unit that reboots and resumes bouncing at full amplitude during an
ESD strike has passed a naive functional criterion and failed the product.

## Scope

Emissions: conducted on the DC input and any cable, radiated. The switching converter
([TS-005](../05-trade-studies/TS-005-power-supply.md)) and the actuator drive stage
([TS-003](../05-trade-studies/TS-003-motor-driver.md)) are the expected sources.

Immunity: ESD to all accessible surfaces — a unit at a caregiver's hand height gets touched often —
plus fast transients, surge on the DC input, and radiated fields.

## Design-stage actions

Pre-compliance is cheap only if the design allows fixes. Reserve filter positions, shield-can
footprints and ground-stitching options at layout time; retrofitting them after a failed test is
what makes EMC expensive.
