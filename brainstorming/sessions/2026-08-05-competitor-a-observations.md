# Session: Competitor A first-hand observations — 2026-08-05

```
Participants: product owner, Claude
Duration:     first session
Focus:        Grounding — what is known first-hand; extracting observations from an owned unit
```

## What we covered

The first brainstorming session, run before any modelling exists. The purpose was grounding: how
much of the project's knowledge is first-hand versus inherited from vendor marketing.

The answer changed the session's direction almost immediately — **the owner has a Competitor A unit
in the house and is willing to open it.** That converts the
[competitive benchmark](../../docs/00-product/competitive-benchmark.md), which currently rests
entirely on unverified vendor claims, into something measurable.

The most valuable output was not planned: a question about the intensity dial led to the discovery
that the multi-spring pack is a **load-adaptation mechanism**, not primarily a redundancy feature.

## What the user knows

**Owns a Competitor A unit, in use with a growing baby.** [observed] Willing to open it carefully
and reassemble, and to photograph the PCB and motor.

**Acoustic signature: a soft whir, once per bounce cycle.** [observed] A whir is a rotating motor;
hearing it once per cycle means the motor runs in **short bursts rather than continuously**. This
is direct evidence for impulse-style energy injection — spin briefly at the correct phase, coast
for the rest of the cycle. Acoustically favourable: broadband whir is far more sleepable than a
click or a pure tone.

**Amplitude: 1–3 cm.** [observed] Smaller than assumed. Makes the advertised ~5 W average draw
considerably more plausible.

**Rate is set by the user via a potentiometer** — turning it makes the bounce faster or slower,
not stronger. [observed] There is **no automatic resonance tracking** in the market-leading
product.

**As the baby grows, the user adds springs to the pack.** [observed] Started with 2–3 springs, now
running 5–7. Describes the task as mildly irritating and volunteered that *"one spring would be
better like in other solutions"*.

**Interface is a single dial plus an LED.** [observed] No timer, no separate power switch. The LED
is noticeable but tolerable in a dark room.

**Motivation:** business opportunity and personal/engineering interest — explicitly **not** driven
by the existing products being too expensive or deficient. The spring-adding complaint was the
first concrete product criticism to surface, and it emerged only through questioning.

## Surprises

### The spring pack is a stiffness-adaptation mechanism

The benchmark recorded the multi-spring pack as a **redundancy** feature, because that is how
Competitor B markets it ("if one spring fails, the others prevent a fall"). Observation says
otherwise: the user adds springs **as the baby gains weight**.

The physics is consistent. For a mass-spring system, frequency goes as √(k/m). Holding the
resonant frequency in the same band as mass rises requires stiffness to rise proportionally, and
springs in parallel add stiffness linearly. The rated range of 3–18 kg is a factor of six; the
packs offer up to seven springs. **Those are the same number.**

The user's own history corroborates it: 2–3 → 5–7 springs, roughly 2.3× stiffness, tracking a baby
from roughly 4 kg to 9–10 kg.

Redundancy appears to be a genuine but **secondary** benefit of a mechanism the design needed
anyway — and good marketing. See `sketches/2026-08-05-spring-pack-dual-function.md`.

### Adaptation is manual in the market leader

`docs/02-architecture/system-architecture.md` asserts that a fixed drive frequency cannot serve the
load range and that "some form of adaptation is unavoidable rather than a luxury".

That is true of the *system*, but the market leader implements the adaptation **mechanically and
manually** — the parent adds springs and re-tunes a dial. Automatic adaptation is therefore **not
table stakes**, contrary to the assumption behind [SYS-010](../../docs/01-requirements/srs-system.md#sys-010).

This cuts both ways, and the honest reading is mixed: it is a real differentiator opportunity,
but the user rates the pain as only *mildly* irritating, so it should not be over-weighted as a
selling point.

### A hazard we had missed

**The user modifies the load path themselves.** Adding springs means an untrained person alters
the component carrying their baby, unsupervised and unchecked. They can fit too few for the
weight, fit one incorrectly, over-extend the pack, or mix worn springs with new.

The existing [HAZ-001](../../docs/03-safety/hazard-analysis.md#haz-001) assumes the load path
leaves the factory correct and stays that way. Nothing covers user-serviceable load-path
modification. **Raised for immediate addition to the hazard analysis.**

## Ideas raised

| Idea | Captured as | First reaction |
|---|---|---|
| Single user-facing spring plus hidden secondary retention | [IDEA-001](../ideas/IDEA-001-single-spring-with-secondary-retention.md) | Promising — resolves the user's wish without a single point of failure |
| Electronic resonance tracking to eliminate spring changes | [IDEA-002](../ideas/IDEA-002-resonance-tracking-replaces-spring-changes.md) | Promising, but check the energy cost off-resonance |
| Simply tell the user when to add a spring | [IDEA-003](../ideas/IDEA-003-tell-user-when-to-add-a-spring.md) | Cheap fallback if IDEA-002 proves expensive |

## Sketches

- `sketches/2026-08-05-spring-pack-dual-function.md` — the two jobs the spring pack currently
  conflates, and how they might be separated

## Answers that unblock something

| Question | Answer | Unblocks |
|---|---|---|
| What does a reference unit sound like? | Soft whir, once per bounce cycle | [TS-001](../../docs/05-trade-studies/TS-001-actuation-concept.md) — evidence for impulse actuation |
| Bounce amplitude? | 1–3 cm | Phase 2 energy model; sanity-checks [SYS-004](../../docs/01-requirements/srs-system.md#sys-004) |
| Does the incumbent track resonance? | No — user sets rate on a pot | Reframes [SYS-010](../../docs/01-requirements/srs-system.md#sys-010) as differentiator, not table stakes |
| What is the spring pack for? | Stiffness adaptation to load | Corrects the benchmark; feeds `models/spring-mass-dynamics` |
| Stiffness range used in practice | 2–3 → 5–7 springs for ~4 → ~10 kg | Real calibration point for the Phase 2 model |

## Still open

- **Which actuator is inside?** Awaiting PCB and motor photographs. Highest-value open item.
- **Spring rate and free length** — needed before any stiffness calculation is more than
  proportional reasoning.
- **Does the pot change drive frequency directly, or motor run-time per cycle?** The whir-per-cycle
  observation suggests the latter may be what is really happening.
- **Is the unit driven at resonance at all**, or is it forced oscillation at a user-chosen rate?
  This materially changes the energy budget and remains genuinely unresolved.
- **Cost target** — still unset, still blocking [TS-001](../../docs/05-trade-studies/TS-001-actuation-concept.md).
- **ADR-0001 positioning** — not discussed this session.
- Measured noise level, and power draw. The owner has not opted to measure these yet.

## Suggested next steps

Offered, not done:

1. **Add a hazard** for user modification of the load path — the one item that should not wait
2. **Correct the benchmark**: reclassify the spring pack as load adaptation, with redundancy as a
   secondary benefit; add the observed amplitude, acoustic signature and interface details as
   *(measured)* rather than *(vendor)*
3. **Photograph the PCB and motor** into `brainstorming/teardown/Competitor A/`
4. **Revisit [SYS-010](../../docs/01-requirements/srs-system.md#sys-010)** — its rationale is now
   known to be wrong, even if the requirement survives
5. Count and measure the springs, if the unit is opened anyway
