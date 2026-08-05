# Acoustic test plan

!!! danger "Competitive make-or-break"
    Silence is the primary axis of competition in this segment. This plan exists early because
    [SYS-002](../01-requirements/srs-system.md#sys-002) cannot be given a number until we can
    measure reference products the same way we will measure our own.

## Objective

Two things, in order:

1. **Establish the target** by measuring reference products (Competitor A, Competitor B, Competitor C)
2. **Verify our unit** against that target across the full load range and all settings

Step 1 is a Phase 1 activity and is currently the blocking input to
[TS-001](../05-trade-studies/TS-001-actuation-concept.md).

## Why dB(A) alone is not enough

A steady 25 dB(A) hum and a 25 dB(A) click once per second are the same number and completely
different products. What wakes a sleeper is **tonal and impulsive content**, and change over time,
not the A-weighted average.

The plan must therefore capture:

- A-weighted level at a defined distance
- **Third-octave or narrowband spectrum** — tonal peaks, and their relation to drive frequency
- **Impulsiveness** — is energy concentrated once per cycle?
- **Modulation** — does the sound change over the cycle, which draws attention
- Behaviour at **start-up and mode change**, not only in steady state

## Method — to be defined in Phase 3

Needs: a room or enclosure with a background below 25 dB(A); a defined microphone position and
height relative to the unit and to where an infant's head would be; loading representative of
3, 10 and 18 kg; measurement of both airborne noise and **structure-borne transmission into the
stand**, which [MEC-004](../01-requirements/srs-mechanical.md#mec-004) requires and which a
free-field measurement misses entirely.

## Practical difficulty

A domestic bedroom at night has a background level around 25–30 dB(A), and the target is likely
near or below it. Measuring a product quieter than the room it is used in requires either a quiet
chamber or a differential method. Establishing this capability early is part of the Phase 1 work,
not a Phase 5 detail — without it, the acoustic requirement cannot be set, and without that,
TS-001 cannot be scored.
