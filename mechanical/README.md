# Mechanical

**In scope**, and safety-critical: the drive unit housing, spring pack, actuator mounting, hooks
and the load path between them.

The stand and the hammock textile are [out of scope](../docs/00-product/project-scope.md);
assumptions about them are
[`IF-xxx` interface assumptions](../docs/01-requirements/frame-interface-assumptions.md).

## This is structure, not enclosure

The assembly carries an infant's full weight, directly above them, under continuous cyclic loading,
for the product's life. [HAZ-001](../docs/03-safety/hazard-analysis.md#haz-001) — load-path failure
— is the only catastrophic hazard, and **fatigue rather than ultimate strength is the governing
failure mode**.

Two requirements drive the design more than any others:

- [MEC-002](../docs/01-requirements/srs-mechanical.md#mec-002) — the structure retains the load
  after **any single element fails**, and holds long enough for the fault to be noticed
- [MEC-003](../docs/01-requirements/srs-mechanical.md#mec-003) — no accessible spring coil gap at
  any point in travel, since the pack extends substantially under load directly above the infant

## Directories

`cad/` — housing, spring pack, mounts, load path · `drawings/` — manufacturing drawings, GD&T,
inspection dimensions

## Verification

See the [load path test plan](../docs/06-verification/load-path-test-plan.md). Single-fault
tolerance is verified by **introducing the fault**, not by analysis.
