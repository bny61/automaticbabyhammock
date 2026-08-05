# Load path test plan

!!! danger "The only catastrophic hazard"
    [HAZ-001](../03-safety/hazard-analysis.md#haz-001) is the failure that kills. This plan verifies
    [SYS-009](../01-requirements/srs-system.md#sys-009),
    [SAF-001](../01-requirements/safety-requirements.md#saf-001),
    [MEC-001](../01-requirements/srs-mechanical.md#mec-001) and
    [MEC-002](../01-requirements/srs-mechanical.md#mec-002).

## Why static strength testing is not sufficient

The load is **dynamic and continuous**. The unit oscillates for hours nightly across a product life
of around two years, accumulating a very large number of load cycles. **Fatigue, not ultimate
strength, is the governing failure mode.** A load path that passes a static proof test by a wide
margin can still fail by fatigue crack growth in service.

The Phase 2 model must produce the actual cycle count before
[MEC-001](../01-requirements/srs-mechanical.md#mec-001) can state a number.

Market surveillance in this product category found failures overwhelmingly on **mechanical** tests,
which is a reason to weight this plan heavily rather than treat it as a formality.

## Test groups

### 1. Static proof and ultimate

Rated load with defined margin; then to failure, to learn the actual failure mode and location.

### 2. Fatigue

Cyclic loading representative of service — amplitude, frequency and mean load from the Phase 2
model — to the required cycle count with margin. Inspect for crack initiation, not only for
separation.

### 3. Single-fault tolerance

**The most important group, and the one most likely to be skipped.** For each load-bearing element
in turn: introduce the failure deliberately and verify that the remaining structure retains the
load, that the drop does not exceed the limit, and that it holds long enough to be noticed
([MEC-002](../01-requirements/srs-mechanical.md#mec-002)).

This must be done **by failing the element**, not by analysis. Analysis assumes the remaining
structure behaves as designed after a sudden dynamic load redistribution; testing finds out.

### 4. Entrapment

Probe testing per the standard selected by
[ADR-0001](../04-decisions/ADR-0001-product-positioning.md), **through the full range of spring
travel and load** — not only at rest. The gap that traps a finger is the one that opens under load
([MEC-003](../01-requirements/srs-mechanical.md#mec-003)).

### 5. Misuse and environment

Overload beyond rated; shock from a dropped or jerked load; incorrect assembly; ageing and thermal
conditioning before retest, since polymer load-bearing elements lose strength with temperature and
time ([SAF-006](../01-requirements/safety-requirements.md#saf-006)).

## Sample and acceptance

To be defined in Phase 3. Note that fatigue results are statistical: a single passing sample
demonstrates very little, so sample size must be set deliberately rather than by convenience.
