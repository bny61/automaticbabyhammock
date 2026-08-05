# Part selection matrix

**No part may appear in a schematic or BOM without a row here.**

This is not bureaucracy. A part chosen without checking lifecycle and second source becomes an
end-of-life crisis two years after launch, and for a product with
[no OTA update path](../../docs/04-decisions/ADR-0003-connectivity-stance.md) a forced part change
can mean a firmware change that cannot be deployed to units already sold.

## Columns

| Column | Meaning |
|---|---|
| Ref | Schematic reference or function |
| Function | What it does in this design |
| Part | Manufacturer part number |
| Requirement | The `HW-xxx` it implements |
| Decision | The `ADR-xxxx` that selected it, if applicable |
| Cost @1k | Unit cost at volume |
| Lifecycle | Active / NRND / EOL — **NRND or EOL is disqualifying** |
| 2nd source | Alternate part, or documented reason none exists |
| Stock | Availability and lead time at the time of selection |
| RoHS/REACH | Compliance status and declaration on file |
| Notes | Derating, thermal, safety relevance |

## Matrix

*Empty — populated in Phase 5, after the trade studies close.*

| Ref | Function | Part | Requirement | Decision | Cost @1k | Lifecycle | 2nd source | Stock | RoHS/REACH | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | |

## Safety-relevant parts

Parts in the load path or in the safety functions
([SAF-001](../../docs/01-requirements/safety-requirements.md#saf-001) …
[SAF-008](../../docs/01-requirements/safety-requirements.md#saf-008)) are marked in Notes and
require: a documented derating analysis, batch traceability through production, and a change
process that treats substitution as a design change requiring re-verification — not as a
purchasing decision.
