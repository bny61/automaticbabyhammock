#!/usr/bin/env python3
"""Cross-check the open-points register against what is actually open in the tree.

    python tools/list_open_points.py            # summary
    python tools/list_open_points.py --detail   # every marker, with location

The register at `docs/open-points.md` is maintained by hand, because the interesting
column — which artefacts must be fixed when a question is answered — cannot be derived.
This script exists to stop it drifting: it reports the `TBD` markers and inline open
questions that are really present, so a register that has gone stale is visible.

Exit status is 0 always. This is a report, not a gate.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

from reqlib import repo_root

TBD_RE = re.compile(r"TBD-P(\d)")
INLINE_Q_RE = re.compile(r"^\s*\*\*\?\s*(.+?)\.?\*\*", re.MULTILINE)
OP_ID_RE = re.compile(r"\bOP-(\d{3})\b")

PHASE_MEANING = {
    "1": "Phase 1 — product definition",
    "2": "Phase 2 — modelling",
    "3": "Phase 3 — safety and requirements",
    "4": "Phase 4 — architecture and trade studies",
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--detail", action="store_true", help="list every marker")
    args = parser.parse_args()

    root = repo_root()
    docs = root / "docs"
    register = docs / "open-points.md"

    tbds: dict[str, list[tuple[Path, int, str]]] = defaultdict(list)
    questions: list[tuple[Path, int, str]] = []

    for path in sorted(docs.rglob("*.md")):
        if path.name in ("open-points.md", "traceability-matrix.md"):
            continue
        for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for phase in TBD_RE.findall(line):
                tbds[phase].append((path, n, line.strip()))
        text = path.read_text(encoding="utf-8")
        for m in INLINE_Q_RE.finditer(text):
            if m.group(1).startswith("~~"):
                continue  # struck through - already settled
            line_no = text[: m.start()].count("\n") + 1
            questions.append((path, line_no, m.group(1)))

    total = sum(len(v) for v in tbds.values())
    print(f"TBD markers: {total}")
    for phase in sorted(tbds):
        print(f"  TBD-P{phase}  {len(tbds[phase]):>3}   {PHASE_MEANING.get(phase, '?')}")

    by_file: dict[Path, int] = defaultdict(int)
    for items in tbds.values():
        for path, _, _ in items:
            by_file[path] += 1
    print("\nHeaviest files:")
    for path, count in sorted(by_file.items(), key=lambda kv: -kv[1])[:6]:
        print(f"  {count:>3}  {path.relative_to(root)}")

    print(f"\nUnresolved inline questions (**? ...): {len(questions)}")
    for path, line, q in questions:
        print(f"  {path.relative_to(root)}:{line}  {q[:76]}")

    # --- register health ----------------------------------------------------
    if register.exists():
        ids = sorted({int(i) for i in OP_ID_RE.findall(register.read_text(encoding="utf-8"))})
        gaps = [n for n in range(1, max(ids, default=0) + 1) if n not in ids]
        print(f"\nRegister: {len(ids)} open points (OP-001..OP-{max(ids, default=0):03d})")
        if gaps:
            print(f"  gaps in numbering: {', '.join(f'OP-{g:03d}' for g in gaps)}")
        if total and len(ids) < 10:
            print("  WARNING: many TBDs but few registered open points — register may be stale")
    else:
        print("\nWARNING: docs/open-points.md not found")

    if args.detail:
        print("\n--- every TBD ---")
        for phase in sorted(tbds):
            for path, line, text in tbds[phase]:
                print(f"  P{phase}  {path.relative_to(root)}:{line}\n       {text[:100]}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
