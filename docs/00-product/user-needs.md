# User needs (UN)

The root of all traceability. Every requirement in this repository must trace back to a user need
or to a [hazard](../03-safety/hazard-analysis.md).

User needs describe **what the user needs and why**, never how it is achieved. They are
*validated* (did we solve the right problem?) rather than *verified*, which is why they carry no
verification method.

!!! note "Status: draft"
    These are Phase 0 seeds derived from the [competitive benchmark](competitive-benchmark.md).
    They must be reviewed against real parent research in Phase 1 before any is set to `approved`.

---

### UN-001 — Soothe a waking baby back to sleep without the parent getting up {#un-001}

```yaml
id: UN-001
status: draft
```

As an exhausted parent at 3 a.m., I need the hammock to start and sustain a soothing motion so
that my baby settles without me having to get out of bed and rock it by hand.

**Rationale:** This is the core job of the product. Every reference product exists for it.

### UN-002 — Not be woken by the device itself {#un-002}

```yaml
id: UN-002
status: draft
```

As a parent sleeping in the same room, I need the unit to be quiet enough that neither the baby
nor I can hear it working.

**Rationale:** Silence is the primary axis of competition in this segment — both Competitor B and
Competitor C lead their marketing with it. A device that solves UN-001 but hums is unsellable.

### UN-003 — Trust that the unit cannot drop my baby {#un-003}

```yaml
id: UN-003
status: draft
```

As a parent, I need confidence that no single failure of the drive unit can let my baby fall,
because the unit hangs directly above them and carries their whole weight.

**Rationale:** The lead hazard of the product category. Competitors already ship redundant spring
packs and advertise the reasoning, so single-fault tolerance is the floor, not a differentiator.

### UN-004 — Run all night without a time limit {#un-004}

```yaml
id: UN-004
status: draft
```

As a parent, I need the unit to run for a full night's sleep without shutting itself off on a
timer or getting hot.

**Rationale:** Multi-spring competitors advertise unlimited duration specifically against rivals
limited to 4 h. A timer that stops mid-night defeats UN-001.

### UN-005 — Control it half-asleep, without a phone {#un-005}

```yaml
id: UN-005
status: draft
```

As a parent in a dark bedroom, I need to adjust the motion with one hand and without finding,
unlocking or waking a phone.

**Rationale:** Every reference product uses a physical dial on the unit, and Competitor B actively
markets the absence of an app and of radio emissions. See
[ADR-0003](../04-decisions/ADR-0003-connectivity-stance.md).

### UN-006 — Work with the stand and hammock I already own {#un-006}

```yaml
id: UN-006
status: draft
```

As a buyer, I need the drive unit to attach to my existing stand, ceiling hook or door frame and
to my existing hammock, so that I am not forced to replace a working setup.

**Rationale:** The category norm is a standalone inline drive unit. This need is what puts the
stand and textile out of scope, and what makes the
[interface control document](../02-architecture/interface-control-document.md) load-bearing.

### UN-007 — Suit my baby from birth through toddlerhood, including twins {#un-007}

```yaml
id: UN-007
status: draft
```

As a parent, I need the same unit to work from a newborn through to roughly two years old, and to
carry twins if I have them, without buying a second product.

**Rationale:** Benchmark units state 3–18 kg and explicitly support twins. A narrower range is a
commercial disadvantage and, more importantly, changes the resonance the control loop must track.

### UN-008 — Cost almost nothing to run {#un-008}

```yaml
id: UN-008
status: draft
```

As a buyer, I need the unit's electricity consumption to be negligible, so that running it every
night is not something I have to think about.

**Rationale:** Competitor B advertises running cost directly (~15 ct/month at 3 h/day, implying
roughly 5 W average). Once a competitor puts a number in the market, it becomes the expectation.

### UN-009 — Have it stop when my baby is not in it {#un-009}

```yaml
id: UN-009
status: draft
```

As a parent, I need the unit to stop by itself when the baby is lifted out, and not to start
against an empty or wrongly loaded hammock.

**Rationale:** Competitor B ships weight detection with automatic stop. Beyond convenience, an
unattended empty hammock swinging at resonance is an uncontrolled hazard in a room with other
children.
