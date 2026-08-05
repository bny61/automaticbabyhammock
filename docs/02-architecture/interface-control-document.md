# Interface control document (ICD)

The definitive record of every boundary the drive unit crosses.

!!! danger "The most important architecture document in this repository"
    The unit is sold standalone and attached to hardware we do not control, cannot test and will
    never see. Any assumption about that hardware that is not written here — with a tolerance band
    — becomes either a field failure or a product that silently works with only one stand.

    A competitor already publishes a compatibility warning about stands with their own resonance.
    That warning is the visible end of an assumption someone did not write down in time.

!!! note "Phase 0 seed — real values come from Phase 2"

## Interface register

| # | Interface | Type | Other side | In scope? | Governed by |
|---|---|---|---|---|---|
| I-1 | Suspension attachment | Mechanical, load-bearing | Stand / ceiling hook / door bracket | Our hook only | [IF-001](../01-requirements/frame-interface-assumptions.md#if-001), [IF-002](../01-requirements/frame-interface-assumptions.md#if-002), [IF-003](../01-requirements/frame-interface-assumptions.md#if-003) |
| I-2 | Hammock attachment | Mechanical, load-bearing | Hammock | Our hook only | [IF-004](../01-requirements/frame-interface-assumptions.md#if-004) |
| I-3 | Dynamic coupling | Mechanical, dynamic | Stand + hammock + occupant | No | [IF-002](../01-requirements/frame-interface-assumptions.md#if-002), [IF-005](../01-requirements/frame-interface-assumptions.md#if-005) |
| I-4 | Power input | Electrical | External SELV adapter | Connector only | [HW-001](../01-requirements/srs-electrical.md#hw-001) |
| I-5 | User interface | Human | Caregiver | Yes | [SYS-006](../01-requirements/srs-system.md#sys-006) |
| I-6 | Ambient environment | Environmental | Bedroom | No | [IF-006](../01-requirements/frame-interface-assumptions.md#if-006) |
| I-7 | Acoustic emission | Environmental | Bedroom, infant, parent | Yes | [SYS-002](../01-requirements/srs-system.md#sys-002) |
| I-8 | Infant proximity | Safety | Infant | Yes | [SAF-007](../01-requirements/safety-requirements.md#saf-007) |

## I-3 — Dynamic coupling: the interface that bites

This interface has no connector and no drawing, which is exactly why it gets missed. The unit does
not merely *hang from* the stand; it **drives it**. Force applied to the hammock is applied equally
and oppositely to the suspension point, at the drive frequency, continuously, for hours.

If the stand has a resonant mode near the drive band, three things happen:

1. Energy is pumped into the stand's mode as well as the hammock's
2. The unit's own resonance estimate may lock onto the coupled mode instead of the intended one
3. Amplitude can grow beyond design intent — [HAZ-002](../03-safety/hazard-analysis.md#haz-002)

### The unsolved problem

[IF-002](../01-requirements/frame-interface-assumptions.md#if-002) bounds the acceptable stand.
But **no consumer can measure their stand's resonant frequency**, so the assumption cannot be
discharged by instructing the user. Two implications:

- The unit must **detect** the violation itself — [SAF-003](../01-requirements/safety-requirements.md#saf-003)
- The instructions must express the limit in terms a buyer *can* apply — likely a whitelist of
  tested stands plus a qualitative test, not a frequency in hertz

Closing this properly is a **Phase 2 objective**, not a Phase 5 detail. It may turn out to
constrain the commercial model: if the risk cannot be bounded for arbitrary stands, selling the
unit standalone becomes a decision with a safety cost attached, which belongs in an ADR.

## I-1, I-2 — Load-bearing attachments

To be specified in Phase 3, drawn in Phase 5. Must define: hook type and dimensions; static and
dynamic load rating; failure mode (must not open under load); compatibility with common stand
hardware; and how a user can confirm correct engagement — because an incorrectly latched hook is a
[HAZ-001](../03-safety/hazard-analysis.md#haz-001) event and the user is the last line of defence.

## I-4 — Power input

Nominal 12 V SELV from an external adapter, per
[ADR-0002](../04-decisions/ADR-0002-power-input-strategy.md). To be specified: connector type,
polarity, current rating, cable length and strain relief.

The connector needs a property the benchmark does not obviously have: the cable runs to a unit that
**moves continuously**, above an infant, so flex life and the strangulation risk of a hanging loop
([HAZ-005](../03-safety/hazard-analysis.md#haz-005)) are interface requirements, not packaging
details.

## I-5 — User interface

Physical control on the unit, one-handed, no visual attention, no app
([SYS-006](../01-requirements/srs-system.md#sys-006)). To be specified in Phase 3: control type and
travel, indication of state and fault, and behaviour in darkness — an indicator bright enough to
read is bright enough to disturb a sleeping room.

## Change control

Changing an interface in this document is a **breaking change**. Any change requires:

1. An issue recording the reason and the affected `IF-xxx`
2. Impact assessment on the [hazard analysis](../03-safety/hazard-analysis.md)
3. An ADR if it changes a decision already accepted
4. Re-run of the [traceability matrix](../01-requirements/traceability-matrix.md)
