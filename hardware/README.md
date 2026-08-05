# Hardware

KiCad 9. **Empty until Phase 4 closes the trade studies** — see
[the governing principle](../docs/index.md#the-governing-principle).

| Directory | Contents |
|---|---|
| `ecu-mainboard/` | KiCad project — schematic, PCB, netlist |
| `libraries/` | Project symbols, footprints, 3D models |
| `component-selection/` | [Part selection matrix](component-selection/part-selection-matrix.md) and datasheets |
| `calculations/` | Power budget, thermal, actuator sizing, tolerance analysis |
| `production/` | Per-release fabrication outputs: gerbers, BOM, CPL, fab notes |

## Rules

- **No part enters a schematic without a row in the part selection matrix** — function, cost @1k,
  lifecycle, second source, stock, RoHS/REACH
- **No mains-side circuitry.** [ADR-0002](../docs/04-decisions/ADR-0002-power-input-strategy.md)
  keeps the ECU outside Low Voltage Directive scope; violating it changes the certification route
- **No radio.** [ADR-0003](../docs/04-decisions/ADR-0003-connectivity-stance.md)
- Every design element traces to an `HW-xxx` requirement
- Regenerate `production/` only for tagged releases, in its own commit

## Git hygiene

Commit `.kicad_sch`, `.kicad_pcb`, `.kicad_pro` and project libraries. Backups, autosave and lock
files are excluded by `.gitignore`. Datasheets over ~5 MB are linked from the matrix, not committed.
