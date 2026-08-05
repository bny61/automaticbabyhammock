#!/usr/bin/env python3
"""Allocate the next free requirement ID and print a ready-to-paste block.

IDs are never invented by hand and never reused. This scans every requirement in
``docs/`` and returns the next free number for the prefix.

    python tools/new_req.py SYS
    python tools/new_req.py SAF --title "Stop within 2 s on loss of occupancy" \\
        --parent SYS-004 --mitigates HAZ-002
"""

from __future__ import annotations

import argparse
import sys

from reqlib import PREFIXES, collect, repo_root


def next_id(prefix: str) -> str:
    used = {
        int(r.id.split("-")[1])
        for r in collect(repo_root() / "docs")
        if r.prefix == prefix and r.id.split("-")[1].isdigit()
    }
    number = 1
    while number in used:
        number += 1
    return f"{prefix}-{number:03d}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prefix", choices=sorted(PREFIXES), help="requirement type")
    parser.add_argument("--title", default="TODO: one-line title")
    parser.add_argument("--parent", default=None)
    parser.add_argument("--verification", default="T", choices=list("AITD"))
    parser.add_argument("--mitigates", default=None, help="HAZ-xxx, for SAF requirements")
    parser.add_argument("--verifies", default=None, help="target IDs, for TC test cases")
    args = parser.parse_args()

    req_id = next_id(args.prefix)
    is_root = PREFIXES[args.prefix]

    meta = [f"id: {req_id}", "status: draft"]
    if not is_root:
        meta.append(f"parent: {args.parent or 'TODO'}")
    if args.prefix not in ("HAZ", "TC"):
        meta.append(f"verification: {args.verification}")
    if args.prefix == "SAF":
        meta.append(f"mitigates: {args.mitigates or 'TODO-HAZ'}")
    if args.prefix == "IF":
        meta.append("tolerance: TODO")
    if args.prefix == "TC":
        meta.append(f"verifies: {args.verifies or 'TODO'}")
    if args.prefix == "HAZ":
        meta += ["severity: TODO", "probability: TODO"]

    body = {
        "UN": "As a <persona>, I need <capability> so that <outcome>.",
        "HAZ": "**Hazardous situation:** TODO\n\n**Harm:** TODO\n\n**Cause:** TODO",
        "TC": "**Setup:** TODO\n\n**Steps:** TODO\n\n**Pass criteria:** TODO",
    }.get(args.prefix, "The ECU shall TODO.")

    print(f"### {req_id} — {args.title}\n")
    print("```yaml")
    print("\n".join(meta))
    print("```\n")
    print(body + "\n")
    print("**Rationale:** TODO\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
