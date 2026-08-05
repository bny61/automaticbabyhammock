# Physics reference

Every formula the project relies on, in one place, with a worked example and the assumptions
that make them valid.

!!! warning "Derived, not measured"
    The frequency relation is exact for the model. Everything downstream inherits **one assumed
    number** — the damping ratio ζ, which is [IF-005](../01-requirements/frame-interface-assumptions.md#if-005)
    and unmeasured. See [OP-003](../open-points.md). Where a conclusion survives a wide range of ζ,
    that is stated explicitly.

## Symbols

| Symbol | Meaning | Unit |
|---|---|---|
| `m` | oscillating mass — infant + hammock + moving hardware | kg |
| `k` | total spring rate | N/m |
| `x` | **static droop** — how far the pack sags under load | m |
| `A` | bounce amplitude, peak from centre | m |
| `ω` | angular natural frequency | rad/s |
| `f` | natural frequency | Hz |
| `ζ` | damping ratio | — |
| `n` | number of springs in parallel | — |
| `g` | 9.81 | m/s² |

---

## 1. Frequency

Standard mass-spring result, and the static force balance:

$$\omega=\sqrt{k/m}\qquad f=\frac{1}{2\pi}\sqrt{\frac{k}{m}}\qquad x=\frac{mg}{k}$$

Eliminating `k` between them removes **both** mass and spring rate:

$$\boxed{\;f=\frac{1}{2\pi}\sqrt{\frac{g}{x}}\;}$$

**The bounce frequency depends only on how far the springs sag.** This is the most useful result
in the project: it explains why adding springs as the baby grows preserves the motion, and it
makes droop — not stiffness — the design parameter. Derivation and validation plan in
`models/spring-mass-dynamics/static-droop-sets-frequency.md`.

| Droop `x` | `f` | Period |
|---:|---:|---:|
| 10 cm | 1.58 Hz | 0.63 s |
| 15 cm | 1.29 Hz | 0.78 s |
| **22 cm** | **1.06 Hz** | **0.94 s** |
| 30 cm | 0.91 Hz | 1.10 s |
| 40 cm | 0.79 Hz | 1.27 s |

## 2. Spring scaling with load

Springs in parallel add stiffness: `k = n · k_spring`. Holding droop constant as mass rises
requires

$$n \propto m$$

A 3–18 kg range is a factor of 6 in mass, so a factor of 6 in stiffness — which is why packs
offer up to about seven springs. **Load capacity and frequency preservation are the same
requirement**, not two.

## 3. Damping and decay

$$A(t)=A_0e^{-\zeta\omega t}\qquad \tau=\frac{1}{\zeta\omega}\qquad Q=\frac{1}{2\zeta}$$

Time to decay from `A₀` to `A`:

$$t=\frac{\ln(A_0/A)}{\zeta\omega}$$

This is **safety-relevant**, not just descriptive:
[ADR-0005](../04-decisions/ADR-0005-behaviour-on-power-restoration.md) resumes motion only if
motion is still present, so this expression *is* the window in which an unattended restart can
occur. Lower damping widens it.

## 4. Energy and power

Total energy in the oscillator, and the fraction lost per cycle:

$$E=\tfrac12 kA^{2}=\tfrac12 m\omega^{2}A^{2}
\qquad \frac{\Delta E}{E}=1-e^{-4\pi\zeta}$$

Mechanical power the actuator must supply, and the velocity impulse that restores one cycle's
loss when applied at maximum velocity:

$$P_\text{mech}=f\,E\left(1-e^{-4\pi\zeta}\right)
\qquad \Delta v=A\omega\left(1-e^{-2\pi\zeta}\right)$$

!!! success "The actuator never lifts the load"
    It replaces only what damping removed. This is why a device moving a 10 kg baby can average a
    few watts — and why energy injection **phase** matters more than force.

## 5. Forces and accelerations

$$v_\text{pk}=A\omega \qquad a_\text{pk}=A\omega^{2}
\qquad F_\text{static}=mg \qquad F_\text{dynamic}=mA\omega^{2}$$

`a_pk` is the number [HAZ-003](../03-safety/hazard-analysis.md#haz-003) needs a safe limit for —
see [OP-004](../open-points.md).

## 6. Transmission

For the cable-drum arrangement, with drum radius `r` and gear ratio `G`:

$$s=r\theta_\text{drum} \qquad \theta_\text{motor}=G\,\theta_\text{drum}
\qquad F_\text{cable}=\frac{G\,T_\text{motor}}{r}$$

`r` and `G` are unmeasured — [OP-034](../open-points.md).

---

## Worked example

Mid-range load, benchmark geometry, target amplitude. **ζ is assumed.**

`x` = 22 cm · `m` = 10 kg · `A` = 25 mm · `ζ` = 0.03

| Quantity | Value | From |
|---|---:|---|
| `ω` | 6.68 rad/s | §1 |
| `f` | 1.06 Hz | §1 |
| Period | 0.94 s | §1 |
| `k` | 446 N/m | `mg/x` |
| Energy `E` | 139 mJ | §4 |
| Loss per cycle | 31.4 % | §4 |
| **Mechanical power** | **47 mW** | §4 |
| Impulse `Δv` per cycle | 29 mm/s | §4 |
| Decay constant `τ` | 5.0 s | §3 |
| `Q` | 16.7 | §3 |
| Decay 9 mm → 1 mm | 11.0 s | §3 |
| Peak velocity | 0.167 m/s | §5 |
| **Peak acceleration** | **1.12 m/s² = 0.11 g** | §5 |
| Static force | 98 N | §5 |
| Dynamic force | 11 N — **11 % of static** | §5 |

## Three consequences worth acting on

**The mechanical power is trivially small — the actuator is not the power problem.** 47 mW of
useful work against an advertised ~5.6 W average draw is **under 1 %**. And the conclusion is
robust: at five times the assumed damping it is still only 126 mW.

| ζ | `P_mech` |
|---:|---:|
| 0.03 | 47 mW |
| 0.06 | 78 mW |
| 0.15 | 126 mW |

So the 5 W figure is dominated by **standby and fixed losses, not by moving the baby.** That
contradicts the working assumption in [power-tree.md](power-tree.md) that the drive rail
dominates, and it changes how [TS-005](../05-trade-studies/TS-005-power-supply.md) should be
scored — quiescent efficiency matters more than peak conversion efficiency. Recorded as
[OP-011](../open-points.md); confirm by measuring input power in `Soothe` versus `Armed` before
acting on it.

**The dynamic force is small next to the static load.** Bouncing adds about 11 % to what the
springs already carry. Fatigue still governs [MEC-001](../01-requirements/srs-mechanical.md#mec-001),
because it is 11 % applied a hundred million times — but the load path is sized by the baby's
weight, not by the motion.

**Peak acceleration is about 0.11 g** at 25 mm and 1.06 Hz. That is the quantity an infant
experiences, and the one [HAZ-003](../03-safety/hazard-analysis.md#haz-003) needs a defensible
limit for. Note that `a ∝ A·ω²` — halving the period would quadruple acceleration at the same
amplitude, so a stiffer pack is not automatically gentler.

## Where these formulas stop being valid

Each of these is a real limit, not a disclaimer:

- **Linear springs.** Real packs may be progressive; a hardening spring makes frequency rise with
  amplitude, which §1 forbids. [OP-008](../open-points.md).
- **One degree of freedom.** Vertical bounce only. A compliant stand adds a second mode and the
  single-`ω` treatment fails — which is exactly
  [HAZ-002](../03-safety/hazard-analysis.md#haz-002).
- **Light damping**, ζ ≪ 1. Fine at ζ ≈ 0.03; the approximations degrade above ζ ≈ 0.2.
- **Viscous damping.** Textile hysteresis and friction are not purely viscous, so decay may not
  be a clean exponential.
- **Constant mass.** A baby that moves changes the effective mass and shifts `ω` within a session.
- **Impulse applied at maximum velocity.** §4's `Δv` assumes optimal phase; off-phase injection
  does less work and the requirement rises.
