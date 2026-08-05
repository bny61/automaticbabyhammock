# Reliability plan

## The problem

[SYS-003](../01-requirements/srs-system.md#sys-003) requires continuous duty with no time limit,
over a product life of roughly two years of nightly use — and possibly a second child after that.
**That cannot be tested in real time.**

Reliability must therefore be established by a combination of accelerated testing, analysis and
component-level data, with the reasoning recorded well enough to be defensible.

## Approach

| Element | Method |
|---|---|
| Load path fatigue | Accelerated cyclic testing — [load path plan](load-path-test-plan.md) |
| Actuator wear | Life test at elevated duty; wear-out mode identified in TS-001 |
| Electronics | Component life analysis; electrolytic capacitor and thermal derating review |
| Thermal ageing | Elevated-ambient soak with functional and mechanical retest |
| Springs | Cyclic test to the required count with margin; inspection for set and crack initiation |

## Acceleration and its limits

Accelerating a life test changes the physics. Running the mechanism faster changes the dynamic
loads; running it hotter changes polymer behaviour and can introduce failure modes that never occur
in service. **The acceleration factor and its justification must be recorded**, and results
interpreted with that in mind — an accelerated test that passes for the wrong reason is worse than
no test.

## What matters most here

**Wear-out modes must be identified before they are accelerated**, or the test measures the wrong
thing. The candidates: spring fatigue, actuator bearing or brush wear, fastener loosening under
continuous vibration, connector fretting on a cable that moves constantly, and electrolytic
capacitor ageing under sustained thermal load.

Connector fretting deserves particular attention: this is a device whose cable flexes continuously
for years, which is not the usual duty cycle for a domestic appliance connector.

## Field feedback

[ADR-0003](../04-decisions/ADR-0003-connectivity-stance.md) means **no telemetry and no OTA**. There
is no field data stream and no remote fix. Reliability information will come only from returns and
support contacts, which makes:

- fault indication rich enough to diagnose over the phone a **reliability requirement**, not a UX one
- returned-unit analysis the primary feedback channel, worth planning for before launch
