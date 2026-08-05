# Sketch: the two jobs of the spring pack — 2026-08-05

From session [2026-08-05-Competitor A-observations](../sessions/2026-08-05-Competitor A-observations.md).

## What the incumbent does

The Competitor A pack does two unrelated jobs with one set of parts. Springs are added **as the baby
grows**, which is a stiffness decision, and redundancy falls out of it as a by-product.

```
        suspension point
              │
        ┌─────┴─────┐
        │  housing  │
        └─┬─┬─┬─┬─┬─┘
          │ │ │ │ │        2-3 springs at birth ....... 5-7 springs later
          ▓ ▓ ▓ ▓ ▓        parallel springs: k_total = n × k_spring
          │ │ │ │ │
        ┌─┴─┴─┴─┴─┴─┐
        │   hook    │
        └─────┬─────┘
              │
           hammock + baby (m)


  JOB 1  keep resonance in the drivable band     JOB 2  survive one spring failing
         f = (1/2π)·√(k/m)                              (Competitor B markets this)
         m rises  →  k must rise  →  add springs        a by-product of Job 1
```

**Why the numbers line up.** Rated range 3-18 kg is a factor of 6 in mass. Holding f constant needs
a factor of 6 in stiffness. The packs offer up to 7 springs. Those are the same number.

The owner's own history fits: 2-3 → 5-7 springs, ~2.3× stiffness, for a baby going ~4 → ~10 kg.

## What we could do instead

Separate the two jobs. One spring for feel and simplicity; a dedicated element for fault tolerance
that carries **no load until something breaks**; stiffness adaptation moved out of the mechanism
altogether.

```
        suspension point
              │
        ┌─────┴─────┐
        │  housing  │
        └──┬─────┬──┘
           │     ╎          ╎ = secondary retention: slack in normal use,
           ▓     ╎              catches after a few mm if the spring fails
           │     ╎
        ┌──┴─────┴──┐
        │   hook    │
        └─────┬─────┘
              │
           hammock + baby


  JOB 1  → moved to the CONTROL domain          JOB 2  → an explicit, analysable element
           drive follows f wherever load                 sized for one shock event,
           puts it (IDEA-002)                            not millions of fatigue cycles
```

## The catch

Job 1 must actually be solved before the single spring is safe to propose — a fixed spring cannot
hold resonance across 3-18 kg on its own. [IDEA-001](../ideas/IDEA-001-single-spring-with-secondary-retention.md)
therefore depends on [IDEA-002](../ideas/IDEA-002-resonance-tracking-replaces-spring-changes.md),
and IDEA-002 is unproven until the Phase 2 energy model says what off-resonance operation costs.

If it turns out expensive, a **progressive or variable-rate spring** is the middle path: it narrows
the frequency swing mechanically without the user touching anything. Worth its own idea if the
model points that way.

## Status

Reasoning from proportionality and one owner's observation. **No spring rate has been measured**,
so nothing here is quantitative yet.
