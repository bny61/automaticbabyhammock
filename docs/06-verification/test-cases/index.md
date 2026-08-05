# Test cases (TC)

Each test case cites the requirements it verifies. The
[traceability matrix](../../01-requirements/traceability-matrix.md) reports approved requirements
that no test case covers.

!!! note "Phase 0 seed"
    Three examples, to establish the format and to exercise the traceability generator. The full
    set is written in Phase 3 alongside the requirements, and pass criteria containing `TBD`
    cannot be executed.

---

### TC-001 — Single-fault tolerance of the load path {#tc-001}

```yaml
id: TC-001
status: draft
parent: SAF-001
verifies: [SYS-009, SAF-001, MEC-002]
```

**Setup:** complete drive unit on a test rig, loaded to maximum rated load with a representative
dynamic profile.

**Steps:** for each load-bearing element in turn, introduce a deliberate failure of that element
while the unit is under load and in motion. Record the descent of the load, and hold the remaining
configuration under load for the required duration.

**Pass criteria:** the load is retained; descent does not exceed `TBD-P3` mm; the remaining
structure holds for at least `TBD-P3` hours.

**Note:** the failure must be **introduced physically**, not simulated by analysis. The question is
how the remaining structure behaves after a sudden dynamic redistribution of load, which analysis
assumes rather than answers.

### TC-002 — Independent drive disable with the processor halted {#tc-002}

```yaml
id: TC-002
status: draft
parent: SAF-005
verifies: [SAF-005, HW-003, SW-003]
```

**Setup:** unit in the Soothe state at maximum amplitude, with debug access to halt the control
processor.

**Steps:** halt the processor. Separately, hold it in reset. Separately, corrupt the control loop's
amplitude estimate while leaving the processor running.

**Pass criteria:** in every case, drive is removed within `TBD-P3` ms and the hammock comes to rest
without being braked.

**Note:** this is the test that determines whether the independence claimed by the
[safety concept](../../03-safety/safety-concept.md) is real. Verifying the monitor only while the
processor is healthy verifies nothing.

### TC-003 — Acoustic emission across the load range {#tc-003}

```yaml
id: TC-003
status: draft
parent: SYS-002
verifies: [SYS-002, MEC-004]
```

**Setup:** unit installed on a reference stand with a reference hammock, in an environment with a
background level below 25 dB(A), per the [acoustic test plan](../acoustic-test-plan.md).

**Steps:** measure A-weighted level and narrowband spectrum at the defined microphone position, at
loads of 3, 10 and 18 kg, at minimum, mid and maximum amplitude settings, in steady state and
during start-up and mode change. Measure structure-borne transmission into the stand separately.

**Pass criteria:** A-weighted level ≤ `TBD-P3` dB(A); no tonal component exceeding `TBD-P3` dB above
the local spectrum; no impulsive content exceeding `TBD-P3`.

**Note:** the A-weighted number alone is insufficient — a tonal or impulsive emission at the same
level is far more likely to wake a sleeper.
