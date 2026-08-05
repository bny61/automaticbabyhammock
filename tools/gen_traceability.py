#!/usr/bin/env python3
"""Generate ``docs/01-requirements/traceability-matrix.md`` from the requirements.

The matrix is derived, never hand-maintained. If it looks wrong, the requirements
are wrong. Output is fully sorted so re-running produces no diff.

    python tools/gen_traceability.py            # write the matrix
    python tools/gen_traceability.py --check    # fail if the matrix is stale (CI)
"""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path

from reqlib import Requirement, collect, index, repo_root

OUTPUT = Path("docs/01-requirements/traceability-matrix.md")

HEADER = """# Traceability matrix

!!! danger "Generated file — do not edit"
    Produced by `python tools/gen_traceability.py` from the requirement blocks in
    `docs/`. Hand edits are overwritten. If something here is wrong, fix the
    requirement that produced it.

"""

# Requirement types that a system requirement is expected to decompose into.
DOWNSTREAM = ("HW", "SW", "MEC", "IF", "SAF")


def _sort_key(req_id: str) -> tuple[str, int]:
    prefix, _, number = req_id.partition("-")
    return prefix, int(number) if number.isdigit() else 0


def _children(reqs: list[Requirement]) -> dict[str, list[str]]:
    children: dict[str, list[str]] = defaultdict(list)
    for req in reqs:
        for parent in req.parents:
            children[parent].append(req.id)
    return {k: sorted(v, key=_sort_key) for k, v in children.items()}


def _verified_by(reqs: list[Requirement]) -> dict[str, list[str]]:
    covers: dict[str, list[str]] = defaultdict(list)
    for req in reqs:
        if req.prefix != "TC":
            continue
        targets = req.meta.get("verifies")
        targets = targets if isinstance(targets, list) else ([targets] if targets else [])
        for target in targets:
            covers[str(target)].append(req.id)
    return {k: sorted(v, key=_sort_key) for k, v in covers.items()}


def _link(req: Requirement, by_id: dict[str, Requirement]) -> str:
    """Render an ID as a link into the page that defines it."""
    rel = req.path.relative_to(repo_root() / "docs")
    target = Path("..") / rel
    return f"[{req.id}]({target.as_posix()}#{req.id.lower()})"


def _cell(ids: list[str], by_id: dict[str, Requirement]) -> str:
    if not ids:
        return "— *none*"
    return "<br>".join(_link(by_id[i], by_id) if i in by_id else f"`{i}` ⚠️" for i in ids)


def render(reqs: list[Requirement]) -> str:
    by_id = index(reqs)
    children = _children(reqs)
    covers = _verified_by(reqs)
    by_prefix: dict[str, list[Requirement]] = defaultdict(list)
    for req in reqs:
        by_prefix[req.prefix].append(req)

    out = [HEADER]

    # --- summary -------------------------------------------------------------
    out.append("## Summary\n")
    out.append("| Type | Count | Approved | Draft |")
    out.append("|---|---:|---:|---:|")
    for prefix in ("UN", "HAZ", "SYS", "HW", "SW", "MEC", "IF", "SAF", "TC"):
        items = by_prefix.get(prefix, [])
        approved = sum(1 for r in items if r.status == "approved")
        draft = sum(1 for r in items if r.status == "draft")
        out.append(f"| `{prefix}` | {len(items)} | {approved} | {draft} |")
    out.append(f"\n**Total:** {len(reqs)} requirement(s).\n")

    # --- user needs downward -------------------------------------------------
    out.append("## User needs → system requirements\n")
    needs = sorted(by_prefix.get("UN", []), key=lambda r: _sort_key(r.id))
    if not needs:
        out.append("*No user needs defined yet.*\n")
    else:
        out.append("| User need | Title | Derived requirements |")
        out.append("|---|---|---|")
        for need in needs:
            out.append(
                f"| {_link(need, by_id)} | {need.title} | "
                f"{_cell(children.get(need.id, []), by_id)} |"
            )
        out.append("")

    # --- hazards downward ----------------------------------------------------
    out.append("## Hazards → safety requirements\n")
    hazards = sorted(by_prefix.get("HAZ", []), key=lambda r: _sort_key(r.id))
    mitigations: dict[str, list[str]] = defaultdict(list)
    for req in reqs:
        if req.prefix != "SAF":
            continue
        targets = req.meta.get("mitigates")
        targets = targets if isinstance(targets, list) else ([targets] if targets else [])
        for target in targets:
            mitigations[str(target)].append(req.id)

    if not hazards:
        out.append("*No hazards identified yet.*\n")
    else:
        out.append("| Hazard | Title | Severity | Mitigated by | Verified by |")
        out.append("|---|---|---|---|---|")
        for hazard in hazards:
            mitigated = sorted(mitigations.get(hazard.id, []), key=_sort_key)
            tests = sorted(
                {tc for saf in mitigated for tc in covers.get(saf, [])}, key=_sort_key
            )
            severity = str(hazard.meta.get("severity", "—"))
            out.append(
                f"| {_link(hazard, by_id)} | {hazard.title} | {severity} | "
                f"{_cell(mitigated, by_id)} | {_cell(tests, by_id)} |"
            )
        out.append("")

    # --- full matrix ---------------------------------------------------------
    out.append("## Full matrix\n")
    out.append("| ID | Title | Status | Parent | Verif. | Verified by |")
    out.append("|---|---|---|---|---|---|")
    for req in sorted(reqs, key=lambda r: _sort_key(r.id)):
        if req.prefix == "TC":
            continue
        parents = _cell(sorted(req.parents, key=_sort_key), by_id) if req.parents else "*root*"
        method = str(req.meta.get("verification", "—"))
        out.append(
            f"| {_link(req, by_id)} | {req.title} | `{req.status or '?'}` | {parents} | "
            f"{method} | {_cell(covers.get(req.id, []), by_id)} |"
        )
    out.append("")

    # --- gaps ----------------------------------------------------------------
    out.append("## Coverage gaps\n")
    gaps: list[str] = []

    uncovered = [
        r
        for r in sorted(reqs, key=lambda r: _sort_key(r.id))
        if r.prefix in ("SYS", "HW", "SW", "MEC", "SAF")
        and r.status == "approved"
        and not covers.get(r.id)
    ]
    if uncovered:
        gaps.append(
            "**Approved requirements with no test case:**<br>"
            + ", ".join(f"`{r.id}`" for r in uncovered)
        )

    unmitigated = [h for h in hazards if not mitigations.get(h.id)]
    if unmitigated:
        gaps.append(
            "**Hazards with no safety requirement:**<br>"
            + ", ".join(f"`{h.id}`" for h in unmitigated)
        )

    childless = [
        r
        for r in sorted(reqs, key=lambda r: _sort_key(r.id))
        if r.prefix == "SYS" and not any(c.startswith(DOWNSTREAM) for c in children.get(r.id, []))
    ]
    if childless:
        gaps.append(
            "**System requirements not yet decomposed:**<br>"
            + ", ".join(f"`{r.id}`" for r in childless)
        )

    out.append("\n\n".join(gaps) if gaps else "*No gaps detected.*")
    out.append("")

    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if the matrix is out of date")
    args = parser.parse_args()

    root = repo_root()
    reqs = collect(root / "docs")
    content = render(reqs)
    target = root / OUTPUT

    if args.check:
        current = target.read_text(encoding="utf-8") if target.exists() else ""
        if current != content:
            print(f"{OUTPUT} is out of date. Run: python tools/gen_traceability.py")
            return 1
        print(f"{OUTPUT} is up to date.")
        return 0

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    print(f"Wrote {OUTPUT} from {len(reqs)} requirement(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
