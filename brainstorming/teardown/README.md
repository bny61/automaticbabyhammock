# Teardowns

Photographs and findings from examining competitor units.

**This is the highest-value evidence in the project.** The
[competitive benchmark](../../docs/00-product/competitive-benchmark.md) currently rests on vendor
marketing claims, all flagged as unverified. A teardown replaces them with fact — and answers the
question [TS-001](../../docs/05-trade-studies/TS-001-actuation-concept.md) calls its largest
avoidable gap: how the incumbents achieve quiet actuation.

## Before opening anything

- **Unplug it and leave it unplugged.**
- This is a **load-bearing product that carries an infant**. If the unit will go back into service,
  reassembly must restore the load path exactly — correct fasteners, correct torque, nothing
  omitted or substituted. Photograph each step so reassembly is checkable against the disassembly.
- If anything in the load path is disturbed, damaged or does not go back as it came apart, retire
  the unit from service rather than trusting it.
- Opening it will likely void any warranty.

## Findings route into

| Finding | Destination |
|---|---|
| Confirmed specification | `docs/00-product/competitive-benchmark.md`, attribution changed from *(vendor)* to *(measured)* |
| Actuator type | [TS-001](../../docs/05-trade-studies/TS-001-actuation-concept.md) |
| Motor driver, MCU | [TS-002](../../docs/05-trade-studies/TS-002-mcu-selection.md), [TS-003](../../docs/05-trade-studies/TS-003-motor-driver.md) |
| Sensing approach | [TS-004](../../docs/05-trade-studies/TS-004-sensing-approach.md) |
| Load path and redundancy | [MEC-002](../../docs/01-requirements/srs-mechanical.md#mec-002), [SAF-001](../../docs/01-requirements/safety-requirements.md#saf-001) |
| A way it could fail dangerously | **Straight to the [hazard analysis](../../docs/03-safety/hazard-analysis.md)** |

Findings are evidence about a competitor, not decisions about our product. They inform trade
studies; they do not shortcut them.
