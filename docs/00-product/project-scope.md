# Project scope

## In scope

The **inline drive unit**, complete:

- Control electronics — PCB, power stage, sensing, user interface
- Firmware
- The mechanical assembly that carries the load: housing, **spring pack**, hooks and retention
- The load path from the top attachment to the bottom hook
- Verification, and the CE technical file for the drive unit

## Out of scope

- **The stand, ceiling mount or door bracket** the unit hangs from
- **The hammock textile and mattress** the unit hangs onto
- The **mains adapter** — a pre-certified external SELV supply is purchased, not designed
  (see [ADR-0002](../04-decisions/ADR-0002-power-input-strategy.md))
- Any app, cloud service or connectivity (see [ADR-0003](../04-decisions/ADR-0003-connectivity-stance.md))
- Non-EU markets
- Packaging and retail branding

!!! danger "The out-of-scope boundary is where this project is most likely to fail"
    The drive unit is sold standalone and attached to hardware we do not control. Every assumption
    it makes about that hardware — suspension geometry, moving mass, stand compliance and
    resonance, attachment strength, hammock geometry — must be an explicit `IF-xxx` assumption
    **with a tolerance band** in the
    [interface control document](../02-architecture/interface-control-document.md).

    This is not theoretical: Competitor A publicly warns that one of its units is incompatible with
    stands that have their own resonance. An assumption left implicit becomes a field failure or a
    product that only works with one stand.

## Work breakdown

| Phase | Deliverable | Gate to exit |
|---|---|---|
| **0** Scaffold | Repository, conventions, tooling | Linter and docs build pass ✅ |
| **1** Product definition | ADR-0001/2/3, regulatory scope, benchmark, `UN-xxx` | ADR-0001 accepted; user needs reviewed |
| **2** Interface & modelling | ICD first cut (`IF-xxx`), spring-mass and frame-coupling models | Resonance, energy and amplitude quantified across 3–18 kg |
| **3** Safety & requirements | Hazard analysis, DFMEA, full SRS, standards matrix | Every hazard mitigated; no orphan requirements; matrix clean |
| **4** Architecture & trade studies | Block diagram, power tree, full ICD, TS-001…005 closed as ADRs | **Hardware platform chosen and justified** |
| **5** Design | Schematic, PCB, firmware, housing and load path | Design review; verification plan executable |

## Phase gates

A phase does not end because its documents exist. It ends when:

1. `python tools/check_requirements.py` is clean
2. The [traceability matrix](../01-requirements/traceability-matrix.md) shows no coverage gaps for
   that phase's scope
3. Every decision the phase was supposed to make is recorded as an accepted ADR
4. Anything deliberately deferred is written down as an open question, with an owner

## The rule that matters most

**No hardware decision may be made before Phase 4.** If Phase 2 or 3 work appears to require
knowing the MCU or actuator, that is a sign the requirement is written at the wrong altitude —
it is specifying a solution rather than a need. Rewrite the requirement.

## Known open questions

Tracked as issues; the ones that would most change the design:

- Does the harmonised standard apply to the drive unit standalone or only to the assembled system?
- Do we sell the unit standalone (as the benchmark products do), which widens the `IF-xxx`
  tolerance bands and puts the resonance-coupling risk on us, or only as a complete set?
- Commercial targets: unit cost, price position, launch volume — needed before TS-001 can weight
  cost against noise
- First-launch member states, for GPSR language and labelling duties
