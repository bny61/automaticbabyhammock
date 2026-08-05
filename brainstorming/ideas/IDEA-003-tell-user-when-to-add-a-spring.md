# IDEA-003 — Simply tell the user when to add a spring

```
Status:  parked
Date:    2026-08-05
Source:  session 2026-08-05-Competitor A-observations
Topic:   interface
```

## The idea

Keep the mechanical adaptation exactly as the incumbent does it, but have the unit **detect that it
is out of its comfortable band and say so** — an indicator meaning "add a spring" or "remove a
spring".

The cheap fallback if [IDEA-002](IDEA-002-resonance-tracking-replaces-spring-changes.md) proves too
expensive.

## Why it might work

- Far cheaper than full resonance tracking: needs enough sensing to know the load or the frequency,
  not a phase-locked drive
- Addresses a real failure mode — the owner adds springs *reactively*, when motion feels wrong.
  Nothing tells them the pack is wrong for the weight right now
- Directly mitigates the user-modification hazard raised this session: an under-sprung unit
  currently announces itself only through degraded feel
- Keeps the proven mechanical arrangement, so it carries much less technical risk

## Why it might not

- Solves the *smaller* half of the problem. The owner still has to do the fiddly job; they are just
  told when
- Adds an interface element to a product whose whole appeal is one dial — and our
  [personas](../../docs/00-product/personas-and-use-cases.md) warn against anything needing
  interpretation at 3 a.m.
- An indicator meaning "modify the load path that holds your baby" is an uncomfortable instruction
  to give an untrained person at night. May need to be a refusal to run rather than a hint
- Requires load sensing anyway, which is much of IDEA-002's cost without its benefit

## What would settle it

- The BOM delta between this and [IDEA-002](IDEA-002-resonance-tracking-replaces-spring-changes.md).
  If small, this is dominated and should be rejected
- Whether "add a spring" can be communicated unambiguously without a screen
- Whether under-springing is dangerous or merely ineffective — decides indicator versus refusal

## Related

[IDEA-002](IDEA-002-resonance-tracking-replaces-spring-changes.md) ·
[SYS-008](../../docs/01-requirements/srs-system.md#sys-008) ·
[SYS-006](../../docs/01-requirements/srs-system.md#sys-006)
