# Vision

## The problem

Infants settle in motion. Parents know this and rock, drive, push and carry their babies for hours
in the first year, at enormous cost to their own sleep. A spring hammock (*Federwiege*) reproduces
the motion passively, but someone still has to keep it going — which means getting up, every time.

A powered drive unit closes that loop. The unit exists so that a parent does not have to get out
of bed.

## The product

An **inline electronic drive unit** that hangs between a stand and a baby hammock, containing the
spring pack, an actuator and control electronics. It pumps the hammock vertically at its resonant
frequency to sustain a gentle bounce, adapting as the baby grows.

It is deliberately **not** a connected product. Control is a physical dial on the unit.

## Who it is for

Parents of babies from birth to roughly two years, in the EU, who already own or are buying a
spring hammock. See [personas and use cases](personas-and-use-cases.md).

## What "good" means here

The product succeeds if a parent stops noticing it. That imposes four hard constraints, all drawn
from what the [benchmark products](competitive-benchmark.md) already achieve:

1. **Inaudible in a quiet bedroom.** Silence is the primary axis of competition. A device that
   soothes but hums has failed.
2. **Incapable of dropping the baby.** No single failure in the load path may release the load.
   This is not a feature; it is the licence to sell.
3. **Runs all night.** No duty-cycle limit, no thermal derating, no timer that stops at 4 h.
4. **Negligible running cost.** Roughly 5 W average, because a competitor has already put that
   number in the market.

## Where we might differentiate

Every reference product competes on quietness and simplicity, and they are all good at it. Beating
them on those axes alone is not a strategy. The candidate openings, to be tested in Phase 1 once
the [benchmark gaps](competitive-benchmark.md#what-we-still-do-not-know) are closed:

- **Adaptive control.** Automatically tracking the resonant frequency as the baby's mass changes,
  rather than asking the parent to re-tune a dial. Competitor C advertises a "self-learning" motor; we
  do not yet know how deep that goes.
- **Safety instrumentation.** Occupancy sensing, anomaly detection and a demonstrable
  single-fault-tolerant load path, engineered and documented rather than asserted.
- **Certification rigour.** Market surveillance found roughly half of tested products in this
  category failing at least one mechanical requirement. Being demonstrably in the other half is
  worth something, particularly to retailers.

These are hypotheses. Phase 1 tests them; none is committed.

## Explicit non-goals

- Not a connected product; no app, no cloud, no radio unless
  [ADR-0003](../04-decisions/ADR-0003-connectivity-stance.md) is overturned
- Not a monitor: it does not watch, listen to or record the baby
- Not a complete sleeping system — we do not build the stand or the textile
- Not a medical device and makes no therapeutic claim
- Not sold outside the EU in this development

## Success criteria

To be quantified in Phase 1 and traced to [user needs](user-needs.md). The commercial targets
(unit cost, price position, volume) are not yet set and are needed before
[TS-001](../05-trade-studies/TS-001-actuation-concept.md) can weight cost against noise.
