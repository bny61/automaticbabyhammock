# IDEA-002 — Electronic resonance tracking replaces manual spring changes

```
Status:  parked — premise partly refuted, see correction
Date:    2026-08-05
Source:  session 2026-08-05-Competitor A-observations
Topic:   control
```

## The idea

Instead of the parent adding springs to keep the resonant frequency inside a drivable band, let the
**drive follow the frequency wherever the load puts it**. The spring pack then never changes, and
the dial can go away or become a simple intensity control.

The incumbent solves the load-range problem in the mechanical domain, manually. This solves it in
the control domain, automatically.

## Why it might work

- Removes the one concrete product complaint the owner raised
- Removes the user-modification hazard raised this session, by removing the user modification
- Enables [IDEA-001](IDEA-001-single-spring-with-secondary-retention.md), which needs stiffness
  adaptation solved elsewhere
- Gives [SYS-010](../../docs/01-requirements/srs-system.md#sys-010) a *true* rationale — the current
  one ("maintain amplitude") turns out not to be the real user pain
- A clean marketing story against every incumbent: *nothing to adjust, ever*
- Twins, or a baby plus bedding, stop being special cases

## Correction, 2026-08-05 — the premise is partly wrong

This idea was written on the assumption that springs are added to keep the resonant frequency in
band, so that tracking frequency electronically would remove the need to add them.

The owner has since clarified that **the springs are there to hold the baby's weight as well as to
provide the swing**, and the analysis in `models/spring-mass-dynamics/static-droop-sets-frequency.md`
shows why that matters:

- Static droop is `x = mg/k`, and frequency reduces to `f = (1/2π)√(g/x)` — it depends **only on
  droop**
- Adding springs to stop a heavier baby over-extending the pack *automatically* restores the
  frequency. The two purposes are one action
- **A control loop cannot substitute for this.** Resonance tracking copes with a frequency shift;
  it cannot stop an 18 kg toddler over-extending a spring sized for a newborn. Static
  over-extension is a strength problem and no firmware fixes it

So electronic tracking **does not eliminate the mechanical adaptation**. Some stiffness change is
unavoidable across a 3–18 kg range. What remains open is only whether the *parent* has to make it —
which points at automatic stiffness change or a progressive-rate spring rather than at a control
loop.

## Why it might not

- **The user rates spring-adding as only "mildly irritating".** This is the honest counterweight:
  it is real, but it may not carry a price premium or justify significant BOM cost
- Frequency is not the only thing that changes with load. Required force scales too, so the
  actuator must cover the whole range — possibly a larger, costlier, louder actuator, which
  attacks [SYS-002](../../docs/01-requirements/srs-system.md#sys-002), the primary competitive axis
- Tracking demands motion sensing and a phase-locked control loop the incumbent apparently does not
  need. More components, more failure modes, more to verify — and with
  [no OTA update path](../../docs/04-decisions/ADR-0003-connectivity-stance.md), more risk
- A tracking loop that locks onto the *wrong* mode is exactly
  [HAZ-002](../../docs/03-safety/hazard-analysis.md#haz-002). Manual tuning cannot chase a stand's
  resonance; an automatic tracker can
- If a fixed spring means running away from resonance at range extremes, the energy cost could
  break [SYS-004](../../docs/01-requirements/srs-system.md#sys-004)

## What would settle it

- **Phase 2 model:** energy per cycle across 3–18 kg with a *fixed* spring rate, versus the
  incumbent's adapted-stiffness approach. If fixed-spring operation is far off resonance at the
  extremes, this idea is expensive and may not survive
- Actuator force envelope across the range — feeds [TS-001](../../docs/05-trade-studies/TS-001-actuation-concept.md)
- Whether the tracker can be made safe against locking onto a stand mode
- Whether a variable-rate or progressive spring narrows the frequency swing enough to make this
  cheap — a middle path worth its own idea if the model suggests it

## Related

[IDEA-001](IDEA-001-single-spring-with-secondary-retention.md) ·
[IDEA-003](IDEA-003-tell-user-when-to-add-a-spring.md) ·
[SYS-010](../../docs/01-requirements/srs-system.md#sys-010) ·
[SYS-004](../../docs/01-requirements/srs-system.md#sys-004) ·
[HAZ-002](../../docs/03-safety/hazard-analysis.md#haz-002) ·
[TS-001](../../docs/05-trade-studies/TS-001-actuation-concept.md)
