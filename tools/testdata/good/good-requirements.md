# Linter fixtures — valid

These requirements must always pass `check_requirements.py`. If a change to the
linter starts rejecting them, the linter has become over-eager.

They are fixtures, not real requirements — they use the 900 number range so they
can never collide with the real ones in `docs/`.

### UN-901 — Fixture user need

```yaml
id: UN-901
status: approved
```

As a parent, I need the hammock to soothe my baby without waking me.

### HAZ-901 — Fixture hazard

```yaml
id: HAZ-901
status: approved
severity: catastrophic
probability: remote
```

**Hazardous situation:** the drive unit releases the load.

### SYS-901 — Fixture system requirement

```yaml
id: SYS-901
status: approved
parent: UN-901
verification: T
```

The ECU shall do the fixture thing.

### SAF-901 — Fixture safety requirement

```yaml
id: SAF-901
status: approved
parent: SYS-901
verification: T
mitigates: HAZ-901
```

The ECU shall fail safe in the fixture case.

### IF-901 — Fixture interface assumption

```yaml
id: IF-901
status: approved
parent: SYS-901
verification: A
tolerance: ±10 %
```

The stand shall present a fixture stiffness within the stated tolerance.

### TC-901 — Fixture test case

```yaml
id: TC-901
status: approved
parent: SYS-901
verifies: [SYS-901, SAF-901]
```

**Setup:** fixture rig. **Pass criteria:** fixture passes.
