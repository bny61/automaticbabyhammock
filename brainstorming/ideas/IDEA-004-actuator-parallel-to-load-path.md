# IDEA-004 — Keep the actuator out of the load path entirely

```
Status:  promising
Date:    2026-08-05
Source:  Competitor A teardown, 2026-08-05 — confirmed by the owner
Topic:   mechanical
```

## The idea

Adopt the incumbent's arrangement as a **design principle**: the springs carry the infant, and the
actuator sits **in parallel**, pulling them. The drive never carries static load.

```
        suspension point
              │
    ┌─────────┴──────────┐
  SPRINGS            MOTOR ▸ GEAR ▸ DRUM ▸ ROPE
  carry the load     pulls the springs
    └─────────┬──────────┘
              │
       hammock + infant
```

## Why it might work

- **No actuator failure mode can drop the infant.** Stripped gear tooth, snapped rope, seized drum,
  shorted MOSFET, dead firmware — all cause *loss of function*, never loss of load. The unit stops
  bouncing and hangs there. This is fail-safe by architecture rather than by detection
- Collapses the scope of [SAF-001](../../docs/01-requirements/safety-requirements.md#saf-001) from
  "the whole drive unit" to "the springs and their two anchorages" — a far smaller, cheaper,
  more analysable safety case
- Makes plastic gears legitimate in a product carrying a baby; they would not be in series
- No brake, ratchet or self-locking element needed to hold the load unpowered, because the drive
  never holds it
- Removes any need for the actuator to be back-driveable or fail-open
- Proven: it is what the market leader ships

## Why it might not

- The rope and its anchorages are still a **hazard to the occupant** even when not load-bearing —
  a steel cable moving continuously above an infant is an entanglement and pinch question, see
  [HAZ-005](../../docs/03-safety/hazard-analysis.md#haz-005)
- A slack or snapped rope could fall into the occupant's space
- Parallel actuation may be less efficient than driving the load directly, since the actuator works
  against spring force rather than with the resonance — to be checked against
  [SYS-004](../../docs/01-requirements/srs-system.md#sys-004)
- It does **not** solve redundancy: the springs remain the load path, so
  [SAF-001](../../docs/01-requirements/safety-requirements.md#saf-001) still needs single-fault
  tolerance there. It narrows the problem rather than removing it
- Constrains the actuation concepts [TS-001](../../docs/05-trade-studies/TS-001-actuation-concept.md)
  may consider — adopting it as a principle rules out any in-line actuator before the study runs,
  which is exactly the kind of premature narrowing this project is set up to avoid

## Interaction with IDEA-001

This weakens [IDEA-001](IDEA-001-single-spring-with-secondary-retention.md) as originally framed.
That idea proposed a hidden secondary retention because redundancy was assumed to be the spring
pack's job. If the actuator is already out of the load path, the remaining question is only whether
*one spring* or *several* carry the infant — a much narrower question, and one where a secondary
retention element is still the cleanest answer if a single spring is wanted.

## What would settle it

- Where the rope terminates on the incumbent — top of the spring stack, or the load below it
- Energy comparison: parallel pull versus in-line actuation, from the Phase 2 model
- Whether the rope can be routed so that a failure cannot drop it into the occupant's space

## Related

[IDEA-001](IDEA-001-single-spring-with-secondary-retention.md) ·
[SAF-001](../../docs/01-requirements/safety-requirements.md#saf-001) ·
[HAZ-001](../../docs/03-safety/hazard-analysis.md#haz-001) ·
[HAZ-005](../../docs/03-safety/hazard-analysis.md#haz-005) ·
[TS-001](../../docs/05-trade-studies/TS-001-actuation-concept.md)
