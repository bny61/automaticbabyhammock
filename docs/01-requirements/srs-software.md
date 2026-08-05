# Software requirements (SW)

Requirements on the firmware. Each traces to a [system requirement](srs-system.md) or a
[safety requirement](safety-requirements.md).

!!! warning "No platform assumptions before Phase 4"
    The MCU is not chosen. Do not write requirements that assume an RTOS, a vendor HAL, a core
    count or a peripheral. Write behaviour and timing; the platform must remain a free variable
    until [TS-002](../05-trade-studies/TS-002-mcu-selection.md) closes.

!!! note "Phase 0 seed — the bulk of this file is written in Phase 3"

---

### SW-001 — Deterministic control timing {#sw-001}

```yaml
id: SW-001
status: draft
parent: SYS-001
verification: T
risk: high
```

The control loop shall execute at a fixed period with jitter below `TBD-P4` % of that period under
all operating conditions, including during user interaction and fault handling.

**Rationale:** Energy injection into a resonant system is phase-sensitive; timing jitter becomes
amplitude error and, at worst, drives the system off-resonance. The "including during user
interaction" clause is the one that catches naive implementations — turning the dial must not
disturb the loop.

### SW-002 — Safe state on fault {#sw-002}

```yaml
id: SW-002
status: draft
parent: SAF-005
verification: T
risk: high
```

On detection of any fault that invalidates the control state — sensor loss, implausible
measurement, timing overrun or internal inconsistency — the firmware shall command drive off,
enter a defined safe state, and indicate the fault to the user.

**Rationale:** [HAZ-006](../03-safety/hazard-analysis.md#haz-006). Stopping is always safe in this
product; there is no continued-operation obligation. The user indication matters because a unit
that stops silently at 03:00 looks identical to one that is working.

### SW-003 — Amplitude limit enforced independently of the control loop {#sw-003}

```yaml
id: SW-003
status: draft
parent: SAF-002
verification: T
risk: high
```

The amplitude limit shall be evaluated by logic that does not share state, timing or sensor
processing with the amplitude control loop, and shall be capable of removing drive on its own.

**Rationale:** The software expression of [SAF-002](safety-requirements.md#saf-002). A limit check
that reads the same possibly-corrupt state as the controller is not a limit. This constrains the
software architecture and should be reflected in
[the architecture document](../02-architecture/software-architecture.md) once Phase 4 begins.

### SW-004 — Plausibility checking of sensor inputs {#sw-004}

```yaml
id: SW-004
status: draft
parent: SAF-003
verification: T
risk: high
```

The firmware shall reject sensor readings that are physically implausible — out of range, changing
faster than the system's dynamics permit, or inconsistent with other sensors — and shall treat
persistent implausibility as a fault per SW-002.

**Rationale:** A failed sensor that reads a plausible constant is more dangerous than one that
reads nothing, because the control loop will act on it confidently. This is the software half of
[SAF-003](safety-requirements.md#saf-003).

---

## To be written in Phase 3

Startup and self-test · resonance acquisition and tracking · amplitude regulation · occupancy
detection logic · anomaly detection thresholds · user interface behaviour and debounce · fault
codes and indication · persistent settings · power-loss and restoration behaviour · logging for
field diagnosis · production and end-of-line test modes.
