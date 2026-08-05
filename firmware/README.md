# Firmware

**Blocked.** The platform is not chosen — see
[TS-002](../docs/05-trade-studies/TS-002-mcu-selection.md), which is itself blocked on
[TS-001](../docs/05-trade-studies/TS-001-actuation-concept.md).

Do not write platform-specific code, choose an RTOS, or add a build system before ADR-0005 exists.

## Intended structure

| Directory | Contents |
|---|---|
| `app/` | Operating modes, user interface, fault handling |
| `drivers/` | Device drivers |
| `hal/` | Hardware abstraction — the only layer that knows the platform |
| `safety/` | **Independent monitor**: amplitude limit, anomaly detection, drive disable |
| `tests/` | Host-side unit tests against the [Phase 2 models](../models/) |
| `tools/` | Build and flashing utilities |

## Two rules that predate the platform choice

**`safety/` is not a layer in the control stack.** Per
[SW-003](../docs/01-requirements/srs-software.md#sw-003) it must share no state, timing or sensor
processing with the control loop it constrains, and must be able to remove drive on its own. A
monitor that consumes the controller's estimates is not a monitor.

**Control and safety logic stay free of platform types.** They must be testable on a host machine
against the Phase 2 models. This matters more than usual here because
[ADR-0003](../docs/04-decisions/ADR-0003-connectivity-stance.md) rules out OTA updates — a field
defect cannot be fixed remotely, so verification carries the load.
