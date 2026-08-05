# Mechanical requirements (MEC)

Requirements on the parts of the drive unit that are **in scope**: the housing, the spring pack,
the actuator mounting, the hooks and the load path between them.

!!! danger "This is structural, safety-critical hardware"
    The mechanical design carries an infant's weight above them, under continuous cyclic loading,
    for the product's whole life. It is not enclosure work. Fatigue, not ultimate strength, is the
    governing failure mode.

The stand and the hammock textile are [out of scope](../00-product/project-scope.md); assumptions
about them live in [frame interface assumptions](frame-interface-assumptions.md).

!!! note "Phase 0 seed — the bulk of this file is written in Phase 3"

---

### MEC-001 — Fatigue life of the load path {#mec-001}

```yaml
id: MEC-001
status: draft
parent: SYS-009
verification: T
risk: high
```

Every load-bearing element shall survive `TBD-P2` fully reversed load cycles at maximum rated load
without crack initiation, where the cycle count corresponds to continuous operation over the
stated product life with a margin of `TBD-P3`.

**Rationale:** Driven oscillation at a few hertz for hours nightly accumulates cycles quickly — the
cycle count over a two-year life is large enough that fatigue, not static strength, governs. The
Phase 2 model must produce the actual cycle count before this number can be set.

### MEC-002 — Retention after single-element failure {#mec-002}

```yaml
id: MEC-002
status: draft
parent: SYS-009
verification: T
risk: high
```

Following the failure of any single load-bearing element, the remaining structure shall retain the
rated load with the hammock descending no more than `TBD-P3` mm, and shall continue to do so for
at least `TBD-P3` hours so that the fault can be noticed.

**Rationale:** [SAF-001](safety-requirements.md#saf-001). The duration clause is the important one:
a redundant load path that fails progressively over minutes protects nobody at night. Benchmark
products use multi-spring packs precisely so that one spring failing is survivable and visible.

### MEC-003 — Closed spring geometry {#mec-003}

```yaml
id: MEC-003
status: draft
parent: SAF-007
verification: I
risk: high
```

The spring pack shall present no accessible coil gap at any point in its travel, from unloaded to
maximum rated load, into which a finger or limb can enter.

**Rationale:** [HAZ-005](../03-safety/hazard-analysis.md#haz-005). Benchmark packs extend from
roughly 22 cm free to 44 cm loaded — a large moving gap directly above an infant. Coil gaps that
open under load are the classic entrapment mechanism in spring products.

### MEC-004 — Structural noise {#mec-004}

```yaml
id: MEC-004
status: draft
parent: SYS-002
verification: T
risk: medium
```

The mechanical assembly shall not radiate or transmit noise that causes the unit to exceed its
acoustic limit, including squeak, rattle, resonance of the housing, and structure-borne
transmission into the stand.

**Rationale:** [SYS-002](srs-system.md#sys-002) is a competitive make-or-break. A silent actuator
in a housing that resonates is a noisy product, and structure-borne transmission into a metal stand
can be worse than the airborne path. This requirement exists so that acoustics is treated as a
whole-assembly property rather than an actuator specification.

### MEC-005 — Housing and thermal envelope {#mec-005}

```yaml
id: MEC-005
status: draft
parent: SAF-006
verification: T
risk: medium
```

The housing shall maintain accessible surface temperatures within the limit of
[SAF-006](safety-requirements.md#saf-006) under continuous duty at maximum load, at the upper
ambient of [IF-006](frame-interface-assumptions.md#if-006), without relying on vents that could
admit a finger or allow ingress of small objects.

**Rationale:** Thermal management and entrapment prevention pull in opposite directions — vents
help cooling and hurt safety. Stating both in one requirement forces the conflict to be resolved in
design rather than discovered in test.

---

## To be written in Phase 3

Material selection and ageing · fastener retention under vibration · corrosion and cleaning
resistance · hook and carabiner specification · drop and misuse loading · assembly and disassembly
(and prevention of incorrect reassembly) · marking and label durability · ingress protection.
