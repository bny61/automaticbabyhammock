# Personas and use cases

!!! note "Phase 0 seed"
    Drafted from the [competitive benchmark](competitive-benchmark.md) and category norms. These
    are hypotheses to be tested against real parent research in Phase 1, not findings.

## Personas

### P1 — The sleep-deprived primary caregiver

Operates the device several times a night, in the dark, one-handed, while holding a baby, at the
lowest cognitive point of their day. Will not read a manual. Will not open an app.

**Design consequence:** the interface must be discoverable by touch. This persona alone justifies
a physical dial over any screen or phone-based control.

### P2 — The occasional caregiver

A grandparent, partner or babysitter using it for the first time, without being shown. Needs the
device to be obvious and to fail visibly rather than silently.

**Design consequence:** no hidden modes, no long-press secrets, unambiguous on/off state.

### P3 — The anxious first-time parent

Reads reviews, checks certifications, worries about what happens if it breaks at 3 a.m. Wants
visible evidence of safety thinking.

**Design consequence:** the safety story must be legible from outside — this is where redundant
load path and a clean technical file become commercial, not just regulatory.

### P4 — The parent of twins

Runs at the top of the load range, possibly with asymmetric loading, for longer sessions.

**Design consequence:** the whole 3–18 kg range must work equally well, not just the middle.

## Use cases

### UC-1 — Night settling (the core case)

Baby stirs at 03:00. Caregiver reaches over, starts the unit, returns to bed. The unit sustains
motion until the baby settles and continues without intervention or timeout.
→ [UN-001](user-needs.md#un-001), [UN-002](user-needs.md#un-002), [UN-004](user-needs.md#un-004),
[UN-005](user-needs.md#un-005)

### UC-2 — Daytime nap

Baby placed in the hammock awake. Unit is started and runs while the caregiver is in another room.
Unsupervised operation raises the safety bar. → [UN-009](user-needs.md#un-009)

### UC-3 — Lifting the baby out

Caregiver lifts the baby mid-session. The unit must detect the loss of load and stop rather than
continue driving an empty hammock at resonance. → [UN-009](user-needs.md#un-009)

### UC-4 — First installation

Buyer attaches the unit to a stand, ceiling hook or door bracket they already own, and to a
hammock we did not make. Everything the unit assumes about that hardware is an `IF-xxx`
assumption. → [UN-006](user-needs.md#un-006)

### UC-5 — The baby grows

Over eighteen months the load roughly triples, moving the resonant frequency. The unit either
adapts automatically or requires re-tuning by the parent — an open product question, and one of
the candidate differentiators in the [vision](vision.md). → [UN-007](user-needs.md#un-007)

### UC-6 — Incompatible stand

The unit is attached to a stand with its own resonance. Driving it can pump energy into an
unintended mode and grow the amplitude beyond design intent. This is a documented competitor
failure mode, so it is a designed-for case, not an edge case.
→ [HAZ-002](../03-safety/hazard-analysis.md#haz-002), [IF-002](../01-requirements/frame-interface-assumptions.md#if-002)

### UC-7 — Something goes wrong at 03:00

A spring fails, the motor stalls, or motion becomes irregular. The unit must reach a safe state
without dropping the load and make the fault obvious to a half-asleep adult.
→ [HAZ-001](../03-safety/hazard-analysis.md#haz-001), [HAZ-006](../03-safety/hazard-analysis.md#haz-006)

### UC-8 — Power interruption and restoration

Mains is lost mid-session and returns. Whether the unit restarts by itself is a **safety decision**
— silently resuming motion over a baby nobody is watching is not obviously correct. To be settled
in Phase 3.

## What is deliberately not a use case

- Monitoring the baby (no camera, microphone or recording)
- Remote or scheduled operation from outside the room
- Any therapeutic or medical use
