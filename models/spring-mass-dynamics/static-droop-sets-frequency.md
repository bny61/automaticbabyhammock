# Static droop sets the bounce frequency

**Status:** analytical result, 2026-08-05. Not yet validated by measurement.

## The result

For a mass suspended on a spring, static droop under load is

    x = m·g / k

and the natural frequency is

    f = (1/2π)·√(k/m)

Substituting k = m·g/x eliminates both mass and spring rate:

    f = (1/2π)·√(g / x)

**The bounce frequency depends only on how far the springs sag under load.** Not on the baby's
weight. Not on the spring rate. Not on how many springs there are.

## Why this explains the whole product

The parent adds springs as the baby grows in order to stop the pack over-extending — a static
strength concern. Adding springs in parallel raises total stiffness, which pulls the droop back to
where it was. And because droop alone sets frequency, **restoring the droop automatically restores
the bounce frequency.**

Load-bearing and frequency-tuning are not two jobs the spring pack happens to share. They are one
job, and keeping the static droop inside a band is the *entire* adaptation strategy.

## It predicts the benchmark

Competitor A publishes spring dimensions of roughly 22 cm free and 44 cm loaded, i.e. a droop of
about 22 cm *(vendor)*:

    f = (1/2π)·√(9.81 / 0.22) ≈ 1.06 Hz

The owner independently describes the bounce as "slow — about one per second" *(observed)*.

Two independent sources agree, from a formula with no fitted parameters. That is decent evidence
the model is right, though it is not a substitute for measurement.

## Droop against frequency

| Droop x | Frequency f | Period |
|---:|---:|---:|
| 10 cm | 1.58 Hz | 0.63 s |
| 15 cm | 1.29 Hz | 0.78 s |
| 20 cm | 1.11 Hz | 0.90 s |
| **22 cm** | **1.06 Hz** | **0.94 s** |
| 25 cm | 1.00 Hz | 1.00 s |
| 30 cm | 0.91 Hz | 1.10 s |
| 40 cm | 0.79 Hz | 1.27 s |

The band is narrow. Across a plausible 15–30 cm of droop the frequency moves only from about
1.3 Hz to 0.9 Hz — which is why a single fixed drive strategy can work at all.

## Consequences for our design

**The design parameter is droop, not spring rate.** Specify the droop band, and the frequency band
follows. This is a much simpler thing to specify, measure and verify than stiffness.

**A control loop cannot substitute for adding springs.** This is the important one. Electronic
resonance tracking copes with a frequency *shift*, but it cannot stop an 18 kg toddler
over-extending a spring sized for a newborn. Static over-extension is a strength problem, and no
firmware fixes it. See the correction recorded in
`brainstorming/ideas/IDEA-002-resonance-tracking-replaces-spring-changes.md`.

**Adaptation must therefore be mechanical**, in some form — more springs, a progressive-rate
spring, or an automatic stiffness change. The remaining question is only whether the *parent* has
to do it.

**A single spring sized for 18 kg would be harsh for a 3 kg newborn**, giving small droop, high
frequency and a very different motion. The load range is what forces variable stiffness, not a
preference for it.

## To validate

- Measure droop and bounce frequency on the owner's unit at its current spring count
- Repeat at a different spring count and confirm the frequency is unchanged
- Check for nonlinearity: does frequency shift at large amplitude? A progressive spring would show
  hardening, which would partly explain the perception of "faster" at 90 % dial
- Establish the acceptable droop band from the geometry constraint (overall length ≤ ~44 cm)
