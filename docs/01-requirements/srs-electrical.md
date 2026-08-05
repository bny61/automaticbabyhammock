# Electrical requirements (HW)

Requirements on the electronics. Each traces to a [system requirement](srs-system.md) or a
[safety requirement](safety-requirements.md).

!!! warning "Write these at the right altitude"
    These requirements must remain **platform-neutral until Phase 4**. "Shall accept 12 V nominal
    input" is a requirement; "shall use an LM2596" is a design decision and belongs in an
    [ADR](../04-decisions/index.md) backed by the
    part selection matrix (`hardware/component-selection/part-selection-matrix.md`).

    If a requirement here cannot be written without naming a part, it is a decision in disguise.

!!! note "Phase 0 seed — the bulk of this file is written in Phase 3"

---

### HW-001 — SELV input only {#hw-001}

```yaml
id: HW-001
status: draft
parent: SYS-004
verification: I
risk: high
```

The ECU shall be powered exclusively from an external SELV supply of `TBD-P4` V nominal, and shall
contain no circuitry operating at or connected to mains potential.

**Rationale:** Implements [ADR-0002](../04-decisions/ADR-0002-power-input-strategy.md). Keeping
mains off the board is what places the ECU outside Low Voltage Directive scope, so this is a
*compliance-load-bearing* requirement — violating it changes the certification route, not just the
schematic. All benchmark products use an external 12 V adapter.

### HW-002 — Input protection {#hw-002}

```yaml
id: HW-002
status: draft
parent: SAF-005
verification: T
risk: medium
```

The ECU shall withstand reverse polarity, over-voltage to `TBD-P4` V, and a short circuit on any
externally accessible conductor, without creating a hazard and without damage that could
compromise the drive-disable path.

**Rationale:** The user supplies the adapter and may replace it with the wrong one. The clause
about the drive-disable path matters: input damage that silently disables the protection but
leaves the motor running is far worse than a dead unit.

### HW-003 — Drive disable independent of the control processor {#hw-003}

```yaml
id: HW-003
status: draft
parent: SAF-005
verification: T
risk: high
```

The hardware shall provide a means of removing drive from the actuator that does not require the
primary control processor to be executing correctly.

**Rationale:** The electrical expression of [SAF-005](safety-requirements.md#saf-005). Stated as a
capability so that Phase 4 can satisfy it with a hardware watchdog, an independent supervisor or a
monitored enable line, without this requirement pre-judging which.

### HW-004 — Electromagnetic compatibility {#hw-004}

```yaml
id: HW-004
status: draft
parent: SYS-001
verification: T
risk: medium
```

The ECU shall meet the emission and immunity limits of the applicable harmonised EMC standard, and
shall maintain safe behaviour — never uncommanded motion — throughout immunity testing.

**Rationale:** EMC Directive 2014/30/EU applies. The second clause is the one that matters for
safety: passing an immunity test by resetting is acceptable only if the reset state is safe. See
[SAF-008](safety-requirements.md#saf-008).

---

## To be written in Phase 3

Power tree and rail tolerances · actuator drive stage · current and position sensing · occupancy
sensing front end · user interface electronics · thermal sensing and protection · connector and
cable requirements · ESD immunity · in-circuit test and programming access.
