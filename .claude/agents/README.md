# Project subagents

Specialist reviewers for this repository. Each starts **cold** — with no memory of any previous
conversation — so every definition re-establishes the project context it needs. Keep them
self-contained.

| Agent | Run it when | Returns |
|---|---|---|
| `impact-auditor` | An open point is answered, a `TBD` is filled, an assumption turns out wrong | Every artefact that must now change, with `file:line` |
| `safety-reviewer` | Every phase gate; any change to hazards, safety requirements or the safety concept | Findings ranked by severity of harm |
| `standards-researcher` | The regulatory questions `OP-016`–`OP-020`, or any regulatory premise needing a check | A sourced research note in `brainstorming/` |
| `requirements-auditor` | Before a phase gate, or after writing a batch of requirements | Requirement-quality findings with suggested rewrites |
| `model-validator` | A formula or number changes, or a derived figure is about to feed a requirement | Independent re-derivation and any discrepancies |

## Shared conventions

**All five report; none of them edit.** In a project where a mistake can harm an infant, the
find-and-fix steps are deliberately separate — you decide what to act on.

**None of them can ask you a question.** Subagents run autonomously. Each is instructed to flag
uncertainty rather than guess, and a flagged uncertainty is the useful outcome. Anything needing
dialogue belongs in a skill instead — that is why the interviewer is `/brainstorm`.

**They do not repeat the tooling.** `tools/check_requirements.py`, `gen_traceability.py` and
`list_open_points.py` already enforce the mechanical rules. The agents exist for the judgement
those scripts cannot make.

## Not built, deliberately

- **`publication-guard`** — considered and not created. `PUBLISHING.md` plus the `.gitignore` rules
  cover it, and the check is a grep rather than a judgement. Revisit if publication becomes real.
- **Anything that writes ADRs** — an ADR records *your* decision. An agent may prepare options and
  consequences; accepting is yours.
- **Trade-study scoring** — blocked on the cost target, which is a business input.
