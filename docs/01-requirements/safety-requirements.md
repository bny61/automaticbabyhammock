# Safety requirements (SAF)

Every requirement here **must** cite the [hazard](../03-safety/hazard-analysis.md) it mitigates
and a verification method. The linter enforces both.

Safety requirements are derived from the hazard analysis, not invented alongside it. If a hazard
has no `SAF-xxx`, the [traceability matrix](traceability-matrix.md) flags it as a gap.

!!! note "Phase 0 seed — all `draft`"
    The real derivation happens in Phase 3, after the [DFMEA](../03-safety/fmea-design.md).

---

### SAF-001 — Redundant load path {#saf-001}

```yaml
id: SAF-001
status: draft
parent: SYS-009
verification: T
mitigates: HAZ-001
risk: high
```

The load path shall contain no single element whose failure releases the load. Every load-bearing
element shall be either duplicated or rated with a margin of `TBD-P3` against its worst-case
dynamic load over the full product life.

**Rationale:** [HAZ-001](../03-safety/hazard-analysis.md#haz-001) is catastrophic. The load is
cyclic for the entire product life, so fatigue rather than ultimate strength governs — a static
safety factor alone does not discharge this requirement.

### SAF-002 — Independent amplitude limit {#saf-002}

```yaml
id: SAF-002
status: draft
parent: SYS-001
verification: T
mitigates: [HAZ-003, HAZ-006]
risk: high
```

The ECU shall stop driving the hammock, and shall not resume automatically, when the measured
amplitude exceeds `TBD-P3` mm. This limit shall be enforced by a mechanism that does not depend
on the correct operation of the amplitude control loop.

**Rationale:** A limit implemented inside the loop it is supposed to constrain fails whenever the
loop does. Independence is the whole point — see
[HAZ-006](../03-safety/hazard-analysis.md#haz-006). *How* the independence is achieved is a Phase 4
architecture decision, not a requirement.

### SAF-003 — Detection of abnormal motion {#saf-003}

```yaml
id: SAF-003
status: draft
parent: SYS-001
verification: T
mitigates: [HAZ-002, HAZ-006]
risk: high
```

The ECU shall detect motion inconsistent with the expected single-degree-of-freedom oscillation —
including growing amplitude at constant drive, unexpected frequency content, and irregular period
— and shall bring the hammock to rest within `TBD-P3` s.

**Rationale:** The primary mitigation for resonance coupling with a compliant stand
([HAZ-002](../03-safety/hazard-analysis.md#haz-002)), which is a documented competitor field
failure. A benchmark competitor advertises shutdown "within seconds on the smallest irregularity",
so the capability is expected in the category.

### SAF-004 — Stop on loss of occupancy {#saf-004}

```yaml
id: SAF-004
status: draft
parent: SYS-008
verification: T
mitigates: HAZ-004
risk: medium
```

The ECU shall cease driving and bring the hammock to rest within `TBD-P3` s of detecting that the
suspended load has left the rated range.

**Rationale:** [HAZ-004](../03-safety/hazard-analysis.md#haz-004). Also prevents driving an empty
hammock at resonance, which is an uncontrolled hazard in a room with other children.

### SAF-005 — Independent drive disable {#saf-005}

```yaml
id: SAF-005
status: draft
parent: SYS-001
verification: T
mitigates: HAZ-006
risk: high
```

The ECU shall remove drive from the actuator within `TBD-P3` ms of a failure of the primary
control processor, by a path that does not require that processor to be functioning.

**Rationale:** A watchdog serviced by the same software that has locked up proves nothing. This
requirement constrains the Phase 4 architecture without dictating it — a hardware watchdog, an
independent supervisor or a monitored enable line would all satisfy it.

### SAF-006 — Thermal protection {#saf-006}

```yaml
id: SAF-006
status: draft
parent: SYS-003
verification: T
mitigates: HAZ-007
risk: medium
```

The ECU shall limit the temperature of any accessible surface to `TBD-P3` °C and shall shut down
before any load-bearing element exceeds the temperature at which its rated strength is affected.

**Rationale:** [SYS-003](srs-system.md#sys-003) mandates unlimited continuous duty over bedding,
so this hazard is created by our own product requirement. The second clause links thermal
protection back to [HAZ-001](../03-safety/hazard-analysis.md#haz-001): a hot polymer load-bearing
part is a load-path failure waiting to happen.

### SAF-007 — No entrapment or entanglement points {#saf-007}

```yaml
id: SAF-007
status: draft
parent: SYS-009
verification: I
mitigates: HAZ-005
risk: high
```

The unit shall present no gap, moving aperture or accessible spring coil, throughout its full
range of travel and under all load conditions, that admits an infant's finger, limb or head per
the probe dimensions of the applicable harmonised standard. The supply cable shall be routed and
restrained so that no accessible loop can form.

**Rationale:** [HAZ-005](../03-safety/hazard-analysis.md#haz-005). Benchmark spring packs travel
from roughly 22 cm free to 44 cm loaded — a large, continuously changing gap directly above the
infant. The applicable probe dimensions come from the standard selected in
[ADR-0001](../04-decisions/ADR-0001-product-positioning.md), which is why that decision must land
first.

### SAF-008 — Defined behaviour on power restoration {#saf-008}

```yaml
id: SAF-008
status: draft
parent: SYS-001
verification: T
mitigates: HAZ-008
risk: medium
```

On restoration of power after an interruption the ECU shall not initiate motion. It shall sustain
oscillation only where oscillation is already present in the hammock, and shall otherwise remain
idle until a deliberate user action.

**Rationale:** [HAZ-008](../03-safety/hazard-analysis.md#haz-008), decided by
[ADR-0005](../04-decisions/ADR-0005-behaviour-on-power-restoration.md). This distinguishes a brief
blip from a real outage **by physics rather than by a timer**: after a short interruption the
hammock is still moving and the unit carries on; after a long one the motion has decayed and
nothing happens. The unit never creates motion, only sustains motion it did not cause — which also
prevents exceeding the previous amplitude by construction.

### SAF-009 — Verify the load-path configuration before driving {#saf-009}

```yaml
id: SAF-009
status: draft
parent: SYS-009
verification: T
mitigates: HAZ-009
risk: high
```

Where any part of the load path is user-serviceable, the ECU shall detect a configuration that is
incorrect or inadequate for the suspended load, shall not commence driven motion, and shall
indicate the condition to the user.

**Rationale:** [HAZ-009](../03-safety/hazard-analysis.md#haz-009). The benchmark product requires
the parent to add springs as the baby grows and then does nothing to check the result — an
under-configured load path announces itself only through degraded feel, if at all. Written
conditionally because the cleanest mitigation is to remove user serviceability from the load path
altogether, which is a Phase 4 design decision rather than a requirement.
