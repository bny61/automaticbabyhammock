# IDEA-005 — Tap to start: the user excites, the unit only sustains

```
Status:  promising
Date:    2026-08-05
Source:  owner observation of Competitor A, 2026-08-05
Topic:   control
```

## The idea

The unit **never initiates motion**. The parent taps the hammock by hand; the ECU detects the
resulting oscillation, locks onto it, and injects energy each cycle to sustain it at the level set
by the dial. Switching the dial on arms the unit; it does not start it.

This is what Competitor A does *(observed)*.

## Why it might work

**It removes the resonance-acquisition problem entirely.** The parent's tap excites the spring-mass
system at its own natural frequency, for free. The unit never has to search for resonance, sweep a
range, or drive the hammock to find out how it responds — it only has to *recognise* motion and
phase-lock to it. Cheap, robust, and much simpler than a frequency search.

**It answers an open question in our own design.** `docs/02-architecture/operating-modes.md` asks:
*"Resonance acquisition may involve motion the parent did not ask for. Whether that is acceptable
over a sleeping baby, and how brief it must be, is unresolved."* Tap-to-start dissolves the
question — there is no acquisition motion, because the human supplies the excitation.

**It is a safety property, not just a UX choice:**

| Hazard | How tap-to-start helps |
|---|---|
| [HAZ-008](../../docs/03-safety/hazard-analysis.md#haz-008) unexpected restart after power loss | The unit **cannot** restart itself — no tap, no motion. Inherently safe, with no logic required |
| [HAZ-004](../../docs/03-safety/hazard-analysis.md#haz-004) driving an empty hammock | Nobody taps an empty hammock. Motion only ever begins with a person present |
| [HAZ-003](../../docs/03-safety/hazard-analysis.md#haz-003) excessive amplitude | The unit sustains rather than builds. It never drives harder than the motion it was given |

**It is an implicit presence check.** A tap is an unambiguous statement that an adult is at the
hammock, right now. No sensor gives that as cheaply or as reliably.

**It explains the sensored motor.** Hall sensors work at zero speed, so a back-driven drum is
detectable while the drive is idle. Sensorless back-EMF detection would not see the tap. The motor
serves as actuator *and* sensor — see the [teardown](../teardown/Competitor A/findings.md).

## Why it might not

- **It is a worse experience at 3 a.m. if the unit stops.** Any safe-stop event now requires the
  parent to get up and tap, which is precisely what [UN-001](../../docs/00-product/user-needs.md#un-001)
  exists to avoid. A false-positive anomaly detection becomes much more costly
- Discoverability: a first-time user turns the dial, nothing happens, and concludes the unit is
  broken. Persona [P2](../../docs/00-product/personas-and-use-cases.md#p2-the-occasional-caregiver)
  — the caregiver using it without being shown — is exactly who this fails
- It forecloses genuinely useful automatic behaviour, such as restarting when the baby stirs
- Detection threshold is a real design problem: too sensitive and a passing lorry or a sibling
  bumping the stand starts it; too coarse and a gentle tap is missed
- The unit must sense while idle, so some sensing path stays powered continuously — a small but
  permanent standby cost against [SYS-004](../../docs/01-requirements/srs-system.md#sys-004)

## What would settle it

- Whether an auto-restart-on-stir behaviour is wanted, or whether tap-only is the product
- Measured tap detection threshold on the incumbent, versus ambient disturbance in a real bedroom
- Whether the safe-stop rate is low enough that "get up and tap" is rare in practice
- How the incumbent communicates the tap requirement to a first-time user

## The open contradiction

The owner reports the dial changes the bounce **rate** (faster/slower). But if the unit locks onto
the natural frequency of the loaded spring-mass system, frequency is fixed by stiffness and mass —
which is precisely why springs must be *added* as the baby grows. A dial cannot change it.

So one of these must be true, and it matters for the control design:

1. The dial sets **amplitude or energy per pulse**, and greater amplitude is perceived as "faster"
2. The dial sets how often the unit pulses — every cycle, every second cycle — changing the *feel*
   without changing the frequency
3. The unit is **not** locked to resonance and does force the rate, in which case adding springs
   serves some other purpose

**Unresolved.** Worth watching the hammock against a clock at both dial extremes.

## Related

[IDEA-002](IDEA-002-resonance-tracking-replaces-spring-changes.md) ·
[IDEA-004](IDEA-004-actuator-parallel-to-load-path.md) ·
[HAZ-008](../../docs/03-safety/hazard-analysis.md#haz-008) ·
[SAF-008](../../docs/01-requirements/safety-requirements.md#saf-008) ·
[TS-004](../../docs/05-trade-studies/TS-004-sensing-approach.md)
