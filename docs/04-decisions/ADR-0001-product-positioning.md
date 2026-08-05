# ADR-0001 — Product positioning: sleep product or soothing swing

```
Status:      proposed        ← DECIDE FIRST. Everything else waits on this.
Date:        2026-08-05
Deciders:    TBD
Trade study: none — this is a product and regulatory decision, not a technical comparison
Affects:     all requirements; SAF-007; the entire verification plan
```

## Context

A *Federwiege* with a powered drive is sold in Germany as a place where a baby **sleeps**. In EU
product-safety law, that framing selects which harmonised standard applies, and the candidates
impose materially different requirements:

| Standard | Covers | Implication if chosen |
|---|---|---|
| **EN 1130:2019** | Cribs, explicitly including **suspended cribs** and cradles providing **sleeping accommodation** | Requirements aimed at unsupervised sleep: sleep-surface geometry, depth, entrapment, stability |
| **EN 16232:2013+A1:2018** | Infant swings | Requirements aimed at supervised, awake-time use; restraint and stability provisions differ |
| **EN 12790-1:2023** | Reclined cradles | Applies if the lying surface is reclined rather than flat |

These are not freely combinable, and the choice is not merely a labelling exercise — it changes
permitted geometry, restraint provisions, the probe dimensions used for entrapment testing
([SAF-007](../01-requirements/safety-requirements.md#saf-007)) and the whole test plan.

The commercial pressure runs one way: the market buys these products for **sleep**, and marketing
them for supervised awake use only would put us at a disadvantage against every reference product.
The safety and regulatory pressure runs the other way: sleep products carry the heavier burden,
because unsupervised infant sleep is where the fatalities are.

### An unresolved complication

Our product is the **drive unit**, not the complete sleeping place. Whether the standard applies to
the unit sold standalone, to the assembled system, or to both — and who carries the obligation when
a customer combines our unit with a third-party stand and hammock — is genuinely unclear and
materially affects the answer. **This must be put to a test house or regulatory consultant before
this ADR is accepted.**

## Options considered

### Option A — Sleep product, built to EN 1130 (suspended crib)

Marketed as a sleeping place, as the reference products are.

**Pros:** matches the market and how customers will use it regardless of what we write; the honest
position given that babies will sleep in it; strongest safety posture; a defensible answer when a
customer uses it for night sleep.

**Cons:** heaviest requirement set; may constrain hammock geometry in ways that conflict with
existing third-party hammocks we do not control ([UN-006](../00-product/user-needs.md#un-006));
higher certification cost.

### Option B — Supervised soothing swing, built to EN 16232

Marketed for awake-time soothing under supervision.

**Pros:** lighter requirement set; lower certification cost; arguably a better fit for a *drive
unit* that does not itself define a sleep surface.

**Cons:** **customers will use it for sleep anyway** — the whole category is bought for night use;
labelling that contradicts actual use is a weak defence after an incident; concedes the main
marketing claim to competitors.

### Option C — Both: qualify against EN 16232 and EN 1130

**Pros:** widest market claim; robust to the scope question above.

**Cons:** highest cost and longest schedule; the two standards may impose conflicting geometry, in
which case "both" is not achievable and the conflict must be resolved anyway.

## Decision

**Not yet decided.** This ADR is `proposed` and is the first task of Phase 1.

## Rationale

Recorded when decided. The decision needs three inputs that do not exist yet:

1. **Regulatory advice** on whether the standard attaches to the drive unit, the assembled system,
   or both
2. **The commercial position** — is "for sleep" a claim we need in order to compete?
3. **A geometry check** on whether EN 1130 requirements are even satisfiable given that the hammock
   is third-party and [out of scope](../00-product/project-scope.md)

## Consequences

To be completed. The consequences are large by construction: this decision propagates into every
requirement, the whole verification plan, and the product's physical form.

**Interim rule while this is open:** write requirements that are **independent of the choice** —
function, noise, power, load range, load-path integrity. Do **not** write geometry, restraint or
labelling requirements yet; they will need rewriting.

## Revisiting

If the product is later marketed differently, or the assembled-system scope question resolves the
other way, this decision must be revisited through a superseding ADR — not by editing this file.
