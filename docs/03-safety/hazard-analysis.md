# Hazard analysis (HAZ)

Hazards are a **root of traceability**, alongside [user needs](../00-product/user-needs.md). Every
[safety requirement](../01-requirements/safety-requirements.md) must cite the hazard it mitigates.

!!! danger "This product hangs above a sleeping infant"
    The drive unit is a load-bearing structural element carrying an infant's full weight, directly
    over them, unsupervised, for hours. HAZ-001 is not one hazard among several — it is the reason
    the rest of this repository is structured the way it is.

!!! note "Status: draft — Phase 0 seed"
    This is a starting set derived from the product architecture and the
    [competitive benchmark](../00-product/competitive-benchmark.md). Phase 3 performs the real
    analysis with severity/probability ratings and a [DFMEA](fmea-design.md). No hazard here is
    complete until it has at least one `SAF-xxx` and a verification method.

## Rating scale

| Severity | Meaning |
|---|---|
| `catastrophic` | Death or life-changing injury to the infant |
| `critical` | Injury requiring medical attention |
| `marginal` | Minor injury or distress |
| `negligible` | Nuisance only |

| Probability | Meaning (per unit, over product life) |
|---|---|
| `frequent` / `probable` / `occasional` / `remote` / `improbable` | To be defined quantitatively in Phase 3 |

---

### HAZ-001 — Load-path failure releases the baby {#haz-001}

```yaml
id: HAZ-001
status: draft
severity: catastrophic
probability: remote
```

**Hazardous situation:** any element in the chain from the top attachment, through the housing,
spring pack, actuator mounting and bottom hook, fails or releases.

**Harm:** the hammock and infant fall to the floor. Potentially fatal.

**Causes:** spring fatigue fracture; hook opening under dynamic load; housing fracture at a
mounting boss; fastener loosening under continuous vibration; creep in a polymer load-bearing
element; incorrect assembly.

**Note:** the load is *dynamic*, not static. Driven oscillation means the load path sees
continuous cyclic loading for the entire product life, so fatigue — not ultimate strength — is the
governing failure mode. Competitors address this with redundant spring packs and advertise the
reasoning, so single-fault tolerance is the category floor.

### HAZ-002 — Resonance coupling with the supporting structure causes runaway amplitude {#haz-002}

```yaml
id: HAZ-002
status: draft
severity: critical
probability: occasional
```

**Hazardous situation:** the unit is attached to a stand, ceiling or door frame that has its own
resonant mode near the drive frequency. Driving energy pumps that mode instead of, or as well as,
the intended one.

**Harm:** amplitude far beyond design intent; impact against the stand or surroundings; ejection
of the infant; structural overload of the stand.

**Causes:** compliant or lightweight stand; a stand within its own resonance band; the drive
tracking to a coupled mode rather than the hammock mode.

**Evidence this is real:** Competitor A publicly states that one of its units is *"nicht kompatibel
mit Gestellen, die eine Eigenschwingung haben"* — incompatible with stands having their own
oscillation. This is a known category failure mode, not a theoretical one. Because our stand is
[out of scope](../00-product/project-scope.md), it must be bounded in the
[ICD](../02-architecture/interface-control-document.md) as
[IF-002](../01-requirements/frame-interface-assumptions.md#if-002).

### HAZ-003 — Excessive amplitude or acceleration harms the infant {#haz-003}

```yaml
id: HAZ-003
status: draft
severity: critical
probability: occasional
```

**Hazardous situation:** the unit drives motion beyond physiologically safe limits, whether by
control fault, incorrect load estimation, or a parent setting it too high.

**Harm:** injury from acceleration; the infant being thrown against the hammock edge or ejected.

**Open question for Phase 3:** what *is* the safe limit? This needs a defensible clinical or
standards basis, not an engineering guess. It is the highest-value unknown in the whole hazard
set, because it bounds the entire control design.

### HAZ-004 — Continued operation with no occupant or an incorrect load {#haz-004}

```yaml
id: HAZ-004
status: draft
severity: marginal
probability: probable
```

**Hazardous situation:** the unit keeps driving after the baby is lifted out, or starts against an
empty, overloaded or asymmetrically loaded hammock.

**Harm:** an unattended hammock oscillating at resonance in a room with other children; unexpected
behaviour when the baby is put back; wasted energy and wear.

**Note:** Competitor B ships weight detection with automatic stop, so this mitigation is expected
in the category.

### HAZ-005 — Entrapment or entanglement {#haz-005}

```yaml
id: HAZ-005
status: draft
severity: catastrophic
probability: remote
```

**Hazardous situation:** the infant, or a limb, is caught in the spring pack, in a moving part, in
the supply cable, or in a gap between the unit and the hammock.

**Harm:** strangulation, asphyxia, crush or amputation injury.

**Note:** the springs travel a long way — benchmark packs extend from roughly 22 cm free to 44 cm
loaded — creating a large moving gap directly above the infant. Cable routing to a unit that moves
continuously is a strangulation hazard in its own right. Mechanical-test failures dominate the
market-surveillance findings for this product category.

### HAZ-006 — Motor or control runaway {#haz-006}

```yaml
id: HAZ-006
status: draft
severity: critical
probability: remote
```

**Hazardous situation:** a fault in the MCU, firmware, sensing or power stage causes the actuator
to be driven continuously, at full output, or out of phase with the intended motion.

**Harm:** excessive amplitude (see HAZ-003), mechanical overload of the load path (HAZ-001),
overheating (HAZ-007).

**Causes:** firmware lockup with the drive enabled; sensor failure feeding the control loop;
power-stage short; loss of the resonance estimate.

**Note:** this is why the drive-disable path must not depend solely on the same MCU that runs the
control loop.

### HAZ-007 — Thermal hazard under continuous duty {#haz-007}

```yaml
id: HAZ-007
status: draft
severity: critical
probability: remote
```

**Hazardous situation:** the unit runs for many hours continuously, as intended, and a component
or accessible surface exceeds a safe temperature.

**Harm:** burn on contact; degradation of a load-bearing polymer part (feeding HAZ-001); fire.

**Note:** [UN-004](../00-product/user-needs.md#un-004) requires unlimited duty, so this hazard is
created by an explicit product requirement, over a device suspended above bedding.

### HAZ-008 — Unexpected restart after power interruption {#haz-008}

```yaml
id: HAZ-008
status: draft
severity: marginal
probability: occasional
```

**Hazardous situation:** mains is interrupted and restored, and the unit resumes motion by itself
— possibly at a previous high setting, possibly with nobody present.

**Harm:** startling the infant; unattended operation the caregiver did not authorise.

**Open question:** auto-resume is a genuine trade-off against
[UN-001](../00-product/user-needs.md#un-001) — a unit that stays off after a brief glitch has
failed the parent at 3 a.m. To be decided in Phase 3 with an ADR.

---

## Not yet analysed

To be added in Phase 3: electrical hazards from the SELV input; small-parts and choking hazards
from any detachable element; chemical and material hazards (REACH, materials near the infant);
misuse cases such as attaching to an inadequate ceiling fixing; ageing and end-of-life behaviour;
and hazards introduced by the user interface itself, such as a setting that can be changed
accidentally.
