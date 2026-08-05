# ADR-0005 — Behaviour on power restoration

```
Status:      accepted
Date:        2026-08-05
Deciders:    product owner
Trade study: none — a safety behaviour, decided from the hazard analysis
Affects:     SAF-008, HAZ-008, operating modes, SW-002
```

## Context

[SAF-008](../01-requirements/safety-requirements.md#saf-008) requires the ECU to enter a *defined*
state when power returns after an interruption, and deliberately did not say which state. It has
been open since Phase 0 because the safest behaviour and the most useful behaviour are not the same
thing:

- **Resuming silently** over a baby nobody is watching is
  [HAZ-008](../03-safety/hazard-analysis.md#haz-008) — motion the caregiver did not authorise,
  possibly hours after they last touched the unit.
- **Staying off** after a two-second glitch fails
  [UN-001](../00-product/user-needs.md#un-001) at three in the morning, which is the entire reason
  the product exists.

A brief mains blip and a long outage are very different events, and the original framing treated
them as one.

## Options considered

### Option A — Never resume; require a fresh user action

**Pros:** unambiguously safe; trivial to verify. **Cons:** a 200 ms brownout wakes the household. The
parent must get up for something that was not a real failure — precisely the UN-001 failure.

### Option B — Always resume at the previous setting

**Pros:** invisible to the parent; a blip costs nothing. **Cons:** the unit can start motion over an
unattended infant an arbitrary time after the caregiver left, which is HAZ-008 as written.

### Option C — Resume only by re-detecting motion that already exists

On restoration the unit does **not** initiate motion. It looks for oscillation already present in
the hammock. If it finds it, it re-locks and sustains it; if the hammock is at rest, it stays idle.

**Pros:** the distinction between a blip and an outage is made by *physics rather than by a timer*.
After a short interruption the hammock is still moving and the unit simply carries on; after a long
one the motion has decayed and nothing happens. The unit never *creates* motion — it only sustains
motion it did not cause. **Cons:** needs sensing available at startup before driving; the decay time
of the hammock becomes a safety-relevant parameter.

### Option D — Resume only if occupancy is confirmed

**Pros:** directly targets the "unattended infant" concern. **Cons:** depends on occupancy sensing
being trustworthy at startup, and an occupied hammock is not the same as an attended one — the
hazard is about the *caregiver's* absence, not the baby's presence.

## Decision

**Option C.** On restoration of power the ECU shall not initiate motion. It shall sustain
oscillation only if it detects oscillation already present, and shall otherwise remain idle until a
deliberate user action.

## Rationale

Option C is the only one that distinguishes a blip from an outage without inventing a threshold,
and it does so with a property that is easy to state and to test: **the unit never creates motion,
it only sustains motion it finds.** That single sentence discharges HAZ-008 structurally rather
than by a timer whose value would be arbitrary.

It also composes cleanly with the rest of the safety concept. The same "sustain, never initiate"
property means the unit cannot drive an empty hammock
([HAZ-004](../03-safety/hazard-analysis.md#haz-004)) and cannot build amplitude beyond what it was
given ([HAZ-003](../03-safety/hazard-analysis.md#haz-003)).

If the tap-to-start architecture is adopted — see
`brainstorming/ideas/IDEA-005-tap-to-start-user-excites-unit-sustains.md`, which is a **candidate,
not yet decided** — this behaviour comes for free, because the mechanism is identical. This ADR is
deliberately written to be independent of that choice: it constrains behaviour, not implementation.

## Consequences

**Positive:** HAZ-008 is addressed by architecture rather than by firmware logic; no threshold to
justify; no timer to test at boundary values; the same sensing serves start, restart and occupancy.

**Negative:** the ECU must be able to *sense* hammock motion before it drives, which constrains
[TS-004](../05-trade-studies/TS-004-sensing-approach.md) — the sensing path must be alive and
trustworthy within the startup window, and must work while the drive is idle. It also makes the
hammock's **decay time** safety-relevant: if motion persists for minutes after the drive stops, the
window in which a restart can occur is correspondingly long, which must be checked against the
damping figure from Phase 2.

A second-order cost: a caregiver who *wants* it to resume after a long outage must tap it, and will
not necessarily understand why it did not resume by itself.

**Requirements affected:** [SAF-008](../01-requirements/safety-requirements.md#saf-008) — the
"defined state" is now defined; its `TBD` on amplitude is resolved by construction, since the unit
cannot exceed motion it did not create. A potentiometer helps here: being an absolute, stateless
control, the intensity setting survives a power cycle without being stored.

**Follow-on work:** state the maximum startup sensing latency; measure hammock decay time in
Phase 2; add a test case injecting interruptions of varying length; decide the tap-to-start
architecture in its own ADR.

## Revisiting

Revisit if Phase 2 shows the hammock's decay time is long enough that "motion still present" spans
an uncomfortably long outage, or if the sensing approach cannot be made trustworthy at startup.
