# Design for manufacture checklist

!!! note "Phase 5 deliverable — checklist only at Phase 0"
    Populated as the design emerges. Listed now so that DFM constraints are known while decisions
    are still cheap to change.

## Electronics

- [ ] Component footprints and courtyards suit the chosen assembly process
- [ ] Panelisation and fiducials defined
- [ ] Test points for [end-of-line test](eol-test-spec.md) placed and accessible in-fixture
- [ ] Programming access defined — and note that
      [ADR-0003](../04-decisions/ADR-0003-connectivity-stance.md) means no OTA, so a **serviceable
      local update path** matters more than usual
- [ ] Every part has a second source, or a documented reason why not
- [ ] No component in the BOM at end-of-life or not-recommended-for-new-design
- [ ] Polarity and orientation markings unambiguous on silkscreen
- [ ] Assembly cannot be completed incorrectly without being obvious

## Mechanical

- [ ] Load-bearing parts cannot be assembled in a wrong orientation — this is a
      [HAZ-001](../03-safety/hazard-analysis.md#haz-001) control, not a convenience
- [ ] Fastener torque specified and verifiable in production
- [ ] Spring pack assembly is repeatable and inspectable
- [ ] Draft angles, wall thickness and tooling feasibility reviewed
- [ ] Markings and labels survive cleaning and product life

## Traceability

- [ ] Serial number scheme defined and applied — a **GPSR requirement**, not optional
- [ ] Batch traceability for load-bearing parts, so a suspect batch can be identified after an
      incident
- [ ] Firmware version recorded per unit and readable in service

## Quality

- [ ] Critical-to-quality characteristics identified from the [DFMEA](../03-safety/fmea-design.md)
- [ ] Incoming inspection defined for load-bearing parts
- [ ] Every safety function has a production test — see [EOL spec](eol-test-spec.md)
