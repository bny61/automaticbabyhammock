# Changelog

All notable changes to this project are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

Because this is a hardware product, releases are tagged per **design revision**
(`hw-A`, `hw-B`, …) as well as per firmware version.

## [Unreleased]

### Added
- Phase 0 repository scaffold: V-model `docs/` structure, requirement ID scheme,
  requirement linter and traceability generator, issue/PR templates, MkDocs site.
- `ADR-0001` (product positioning), `ADR-0002` (power input strategy) and
  `ADR-0003` (connectivity stance) opened as `proposed`.
- Competitive benchmark data for Competitor A, Competitor B-1 and Competitor C.
- First-hand Competitor A teardown; the actuator sits parallel to the load path.
  Photographs are kept local and untracked.
- `ADR-0004` (12 V nominal supply) and `ADR-0005` (behaviour on power restoration —
  sustain, never initiate) **accepted**.
- Physics reference, the static-droop model, and a tap-and-sustain control simulation
  with its figure.
- Open-points register `OP-001`…`OP-036`, with the artefacts each answer obliges us to fix.
- Five specialist reviewer subagents in `.claude/agents/`.
- `docs/project-status.md` — the single source of truth for phase status, artefact
  counts and current blockers.

### Changed
- Phase status corrected across `README.md` and `docs/index.md`: Phases 1–3 are in
  progress in parallel, not "not started".

### Notes
- No hardware design decisions have been made. MCU, actuator, motor driver and sensing
  are deliberately undecided until the Phase 4 trade studies close.
