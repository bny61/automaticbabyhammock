# ADR-0003 — No radio; physical control on the unit

```
Status:      proposed
Date:        2026-08-05
Deciders:    TBD
Trade study: none — the market evidence and the compliance cost point the same way
Affects:     SYS-006; TS-002; TS-004; RED applicability; firmware update strategy
```

## Context

The default assumption for a modern appliance is app control over BLE or Wi-Fi. In this product
category, that assumption is wrong in both directions — market and compliance.

**Market evidence.** Every reference product uses a **physical dial on the unit** and none offers an
app. Competitor B goes further and advertises that its unit operates entirely without radio
emissions, presenting that as a health benefit, and stresses that no app is needed. In this segment,
the absence of a radio is marketed as a **feature**. Whatever one thinks of the underlying claim,
the buyer's belief is the commercial fact we must design against.

**Use evidence.** The operating persona is a caregiver in a dark room at 03:00, one-handed, holding
a baby ([P1](../00-product/personas-and-use-cases.md#p1-the-sleep-deprived-primary-caregiver)).
Finding and unlocking a phone is worse than reaching for a dial by every measure that matters here
— speed, light emission, and not needing both hands.

**Compliance evidence.** Fitting a radio brings the product under **Radio Equipment Directive
2014/53/EU**, whose Article 3(3)(d)(e)(f) cybersecurity requirements are now mandatory. That is not
a test line item; it is a workstream covering security-by-design, personal-data protection and
fraud protection, plus radio testing, plus a security-maintenance obligation over the product's
life. For a device whose entire user interface is "how hard should it bounce", the ratio of
compliance cost to user value is extreme.

## Options considered

### Option A — No radio; physical control only

**Pros:** RED does not apply, removing a whole conformity workstream and its ongoing security
obligations; matches every reference product; aligns with the segment's marketing position; better
for the actual 03:00 use case; cheaper BOM; no attack surface on a device above an infant; no app
to maintain for the product's life; simpler MCU requirements, widening the
[TS-002](../05-trade-studies/TS-002-mcu-selection.md) field.

**Cons:** no remote control, no usage history, no app-based diagnostics; **no over-the-air firmware
update**, so a field defect requires a physical intervention or a recall; forecloses any future
connected feature without a hardware change; may look dated to some buyers.

### Option B — BLE with a companion app

**Pros:** remote adjustment without entering the room; usage logging; OTA updates; diagnostics.

**Cons:** RED applies in full, including mandatory cybersecurity requirements; an app to build and
maintain for years; runs against the segment's explicit anti-radio marketing; adds cost and MCU
complexity; adds an attack surface to a device that physically moves an infant; the app is a *worse*
interface for the primary use case.

### Option C — No radio now, footprint reserved for later

**Pros:** keeps the option open at low cost.

**Cons:** an unpopulated radio does not remove RED obligations if it is ever populated, so the
decision is only deferred, not avoided; carries layout, shielding and EMC constraints for a feature
that may never ship; invites feature creep.

## Decision

**Option A** — no radio. All functions are controlled by a physical interface on the unit.

## Rationale

This is unusual in that market positioning, the primary use case, safety and compliance cost all
point the same way. The strongest single argument is the market one: in a segment where a
competitor advertises the *absence* of radio as a benefit, adding one incurs a substantial
compliance burden to deliver a feature some of our buyers would count against us.

Option C is rejected because it buys little — the compliance obligation attaches on population, not
on layout — while imposing real constraints now.

## Consequences

**Positive:** RED out of scope; no app to build or maintain; smaller BOM; wider MCU field; no
network attack surface; marketing alignment with the segment.

**Negative — and this one is significant:** **no OTA firmware update.** A firmware defect found in
the field cannot be fixed remotely. For a safety-relevant product this raises the stakes on
pre-release verification considerably, and it must be reflected in the
[verification plan](../06-verification/verification-plan.md) and the reliability strategy. It also
means a serviceable local update path (a connector, a documented procedure) is worth specifying
even without a radio.

Also negative: no usage data to inform future development, and no field diagnostics beyond what a
user can report by phone.

**Requirements affected:** confirms [SYS-006](../01-requirements/srs-system.md#sys-006); removes
radio criteria from [TS-002](../05-trade-studies/TS-002-mcu-selection.md) and
[TS-004](../05-trade-studies/TS-004-sensing-approach.md).

**Follow-on work:** specify a local firmware update path for service; strengthen the verification
plan to compensate for the absence of OTA; specify fault indication rich enough to diagnose over
the phone.

## Revisiting

Revisit if market research contradicts the benchmark reading — for example, if buyers in target
member states expect app control — or if a compelling safety feature genuinely requires
connectivity. Note that reversing this decision is a hardware change, not a firmware one.
