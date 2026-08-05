# Linter fixtures — deliberately invalid

Every block below contains a specific defect the linter must catch. This file
exists so that `check_requirements.py --self-test` proves the linter *rejects*
bad input, rather than merely proving that it runs without crashing.

**Never fix these.** Each comment names the error code that must be produced.

### SYS-902 — Heading ID does not match metadata ID

```yaml
id: SYS-903
status: draft
parent: UN-901
verification: T
```

The ECU shall trigger ID-MISMATCH.

### SYS-904 — Status is not a legal lifecycle value

```yaml
id: SYS-904
status: wip
parent: UN-901
verification: T
```

The ECU shall trigger STATUS-INVALID.

### SYS-905 — Parent does not exist

```yaml
id: SYS-905
status: draft
parent: UN-999
verification: T
```

The ECU shall trigger PARENT-UNKNOWN.

### SYS-906 — Verification method is not A, I, T or D

```yaml
id: SYS-906
status: draft
parent: UN-901
verification: X
```

The ECU shall trigger VERIF-INVALID.

### SYS-907 — No parent at all

```yaml
id: SYS-907
status: draft
verification: T
```

The ECU shall trigger PARENT-MISSING.

### SYS-908 — Written as a wish rather than an obligation

```yaml
id: SYS-908
status: draft
parent: UN-901
verification: T
```

The ECU ought to be quiet. Written as a wish, so it is not verifiable.

### SAF-902 — Safety requirement citing no hazard

```yaml
id: SAF-902
status: draft
parent: SYS-901
verification: T
```

The ECU shall trigger SAF-NO-HAZARD.

### IF-902 — Interface assumption with no tolerance band

```yaml
id: IF-902
status: draft
parent: SYS-901
verification: A
```

The stand shall trigger IF-NO-TOLERANCE.
