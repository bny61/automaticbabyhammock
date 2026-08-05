# Automatic Baby Hammock — Electronic Control Unit

Product development repository for the **ECU of an automatic baby hammock**: the inline,
motorised drive unit that hangs between a stand and a baby hammock and bounces it vertically on
springs (a motorised *Federwiege*).

Benchmarked against **Competitor A** (A-1 / A-2 / A-3), **Competitor B-1** and **Competitor C**.

> **Safety-critical product.** The unit carries an infant's full weight directly above them.
> Read [`CLAUDE.md`](CLAUDE.md) before contributing — human or agent.

---

## What this repository is

It is the **apparatus for making engineering decisions**, not a finished design. Requirements,
physics modelling and hazard analysis come first; the MCU, actuator, sensors and PCB are chosen
later, in Phase 4, as recorded outcomes of trade studies.

If you are looking for the schematic, it does not exist yet, and that is intentional.

## Scope

| | |
|---|---|
| **In scope** | Electronics, firmware, housing, load path, spring pack, hooks and retention |
| **Out of scope** | The stand / ceiling mount; the hammock textile and mattress |
| **Market** | EU only — CE route |
| **Repository** | Private, proprietary |

Everything the ECU assumes about the out-of-scope parts lives in the
[Interface Control Document](docs/02-architecture/interface-control-document.md) as an `IF-xxx`
assumption with a tolerance band.

## Phase status

| Phase | Content | Status |
|---|---|---|
| 0 | Repository scaffold, tooling, conventions | ✅ complete |
| 1 | Product definition, regulatory positioning, benchmark | ⬜ not started |
| 2 | Interface control document, physics & control modelling | ⬜ not started |
| 3 | Hazard analysis, DFMEA, requirements | ⬜ not started |
| 4 | Architecture and trade studies — **hardware chosen here** | ⬜ not started |
| 5 | Schematic, PCB, firmware, mechanical design | ⬜ not started |

**Next action:** write [`ADR-0001 — product positioning`](docs/04-decisions/ADR-0001-product-positioning.md).
Nothing else should start before it, because it decides which harmonised standard the product is
built to, and therefore what the product physically is.

## Navigating the docs

`docs/` is numbered to follow the V-model, so the flow of information is visible in the tree:

```
00-product        why the product exists, who for, and under which regulation
01-requirements   what it must do          ← IDs start here
02-architecture   how it is structured
03-safety         what can go wrong and what prevents it
04-decisions      ADRs — decisions, once made, immutably
05-trade-studies  the analysis that produces those decisions
06-verification   how we prove each requirement is met
07-manufacturing  how it gets built and certified
```

## Local setup

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

mkdocs serve                              # docs site at http://127.0.0.1:8000
python tools/check_requirements.py        # lint requirement IDs and links
python tools/gen_traceability.py          # regenerate the traceability matrix
python tools/list_open_points.py          # cross-check the open-points register
```

Run the linter before every commit touching `docs/`. The traceability matrix is **generated** —
never edit it by hand.

CI runs the linter, its self-test, the matrix freshness check and a strict docs build on every
push. The built site is downloadable from the run summary as the `site` artifact.

> **Docs site hosting:** GitHub Pages is not available for private repositories on the current
> plan, so the deploy job is skipped. To enable it later: upgrade the plan, set
> *Settings → Pages → Source* to **GitHub Actions**, then `gh variable set ENABLE_PAGES --body true`.
> Until then, read the docs locally with `mkdocs serve`.

## Licence

Proprietary. All rights reserved. See [`LICENSE`](LICENSE).
