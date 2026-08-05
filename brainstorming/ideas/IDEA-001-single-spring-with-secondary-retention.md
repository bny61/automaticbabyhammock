# IDEA-001 — Single user-facing spring plus hidden secondary retention

```
Status:  promising
Date:    2026-08-05
Source:  session 2026-08-05-Competitor A-observations
Topic:   mechanical
```

## The idea

Give the user **one spring** — simple to look at, nothing to add or remove — and carry the
redundancy on a **separate, hidden retention element** (a strap, cable or sleeve) that bears no
load at all until the spring fails, then catches it after a few millimetres.

This separates two jobs that the Competitor A pack currently conflates: *load-range adaptation*
(springs added as the baby grows) and *fault tolerance* (extra springs happen to provide it).

## Why it might work

- The user asked for exactly this: that a single spring would be preferable, as other products use
- Redundancy stops being a side effect of the spring count and becomes a **designed, analysable
  element** — which is a much stronger position for
  [SAF-001](../../docs/01-requirements/safety-requirements.md#saf-001) and the technical file
- A dedicated retention element can be sized for a single dramatic event, whereas a spring must
  survive millions of fatigue cycles. Different duty, different design, probably cheaper
- Makes the safety story legible to a buyer — persona P3 in
  [personas](../../docs/00-product/personas-and-use-cases.md) explicitly wants visible evidence of
  safety thinking
- Removes the assembly step that creates the user-modification hazard raised this session

## Why it might not

- **Only works if stiffness adaptation is solved elsewhere.** A single fixed spring cannot hold the
  resonant frequency across 3–18 kg. This idea depends on [IDEA-002](IDEA-002-resonance-tracking-replaces-spring-changes.md)
  or a variable-rate spring
- A slack retention element that never carries load is hard to *verify* in service — it could be
  broken, corroded or wrongly fitted for years and nobody would know. May itself need a check
  mechanism, which erodes the simplicity
- The catch event applies a shock load to a structure that was designed for smooth cyclic loading;
  the shock path must be analysed, and it may drive the housing design
- A slack strap near an infant is an entanglement question — see
  [HAZ-005](../../docs/03-safety/hazard-analysis.md#haz-005)
- Competitor B markets multi-spring redundancy as a *feature*; going to one spring means arguing
  against a competitor's safety story, which needs to be convincing to a nervous parent

## What would settle it

- Whether stiffness adaptation can be solved without changing springs — [IDEA-002](IDEA-002-resonance-tracking-replaces-spring-changes.md)
- A shock-load calculation for the catch event at maximum rated load
- Whether the retention element can be made **self-evidently intact** on inspection by a parent
- Teardown: how do the single-spring competitors the user referred to actually handle redundancy?

## Related

[IDEA-002](IDEA-002-resonance-tracking-replaces-spring-changes.md) ·
[SAF-001](../../docs/01-requirements/safety-requirements.md#saf-001) ·
[MEC-002](../../docs/01-requirements/srs-mechanical.md#mec-002) ·
[HAZ-001](../../docs/03-safety/hazard-analysis.md#haz-001) ·
[HAZ-005](../../docs/03-safety/hazard-analysis.md#haz-005)
