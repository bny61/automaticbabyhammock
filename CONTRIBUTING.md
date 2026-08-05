# Contributing

Read [`CLAUDE.md`](CLAUDE.md) first — it is the binding working agreement for humans and AI agents
alike. This file covers mechanics only.

## Branches

```
main                      always green: linter passes, docs build
phase1/<topic>            phase work, e.g. phase1/regulatory-scope
req/<ID>                  work on a specific requirement, e.g. req/SYS-014
adr/<number>-<slug>       e.g. adr/0001-product-positioning
ts/<number>-<slug>        e.g. ts/001-actuation-concept
hw/<topic>  fw/<topic>  mech/<topic>
fix/<slug>
```

## Commits

Conventional-commit prefixes, with the ID in the subject where one applies:

```
req(SYS-014): add continuous-duty thermal limit
adr(0002): accept external SELV adapter strategy
safety(HAZ-003): add secondary retention to load path
hw: add 12 V input protection stage
docs: clarify IF-007 tolerance band
tools: make traceability output deterministic
```

## Before every commit that touches `docs/`

```bash
python tools/check_requirements.py
python tools/gen_traceability.py
mkdocs build --strict
```

Commit the regenerated matrix together with the requirement change that caused it.

## Pull requests

The template asks which requirement IDs the PR implements or changes. Answer it. A PR touching
`hardware/`, `firmware/` or `mechanical/` that implements no requirement needs an explanation.

Additional gates:

- New `SAF-xxx` → must name the `HAZ-xxx` it mitigates and a verification method
- New part in a schematic → must have a row in `hardware/component-selection/part-selection-matrix.md`
- New assumption about the stand or hammock → must be an `IF-xxx` in the ICD with a tolerance band
- Changing an accepted ADR → not allowed; write a superseding ADR instead

## Writing requirements

One requirement per `###` heading, each with a YAML block:

````markdown
### SYS-014 — Continuous operation without thermal derating

```yaml
id: SYS-014
status: draft
parent: UN-006
verification: T
risk: medium
```

The ECU shall operate continuously at maximum rated load for at least 12 h without
reducing bounce amplitude and without any accessible surface exceeding X °C.

**Rationale:** Benchmark units advertise unlimited operating duration; single-spring
competitors are limited to 4 h. Parents use the product for full night sleeps.
````

- Use **shall** for requirements, **should** for goals.
- If you cannot state the verification method, it is not yet a requirement.
- Requirements state *what*, not *how*. "Shall detect loss of occupancy within 2 s" is a
  requirement; "shall use an HX711 load cell amplifier" is a design decision and belongs in an ADR.

## Statuses

`draft` → `review` → `approved` → (`obsolete`)

Only `approved` requirements may be cited as the basis for a design. Changing an `approved`
requirement requires a requirement-change issue explaining the impact.

## KiCad hygiene

- Commit `.kicad_sch`, `.kicad_pcb`, `.kicad_pro`, project libraries and the fab outputs
  under `hardware/production/`.
- Never commit autosave, backup or lock files — `.gitignore` covers them.
- Regenerate fab outputs only for tagged releases, in their own commit.
- Datasheets over ~5 MB: link them in the part-selection matrix rather than committing them.
