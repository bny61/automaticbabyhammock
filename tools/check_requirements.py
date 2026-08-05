#!/usr/bin/env python3
"""Lint requirement blocks in ``docs/``.

Run before every commit that touches ``docs/``:

    python tools/check_requirements.py

Self-test the linter itself against known-bad fixtures:

    python tools/check_requirements.py --self-test

Exit status is 0 when clean, 1 when any error is found.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from reqlib import (
    ID_RE,
    OBLIGATION_TYPES,
    PREFIXES,
    STATUSES,
    VERIFICATION_METHODS,
    Requirement,
    collect,
    repo_root,
)


class Error:
    def __init__(self, code: str, req: Requirement, message: str) -> None:
        self.code = code
        self.req = req
        self.message = message

    def render(self, root: Path) -> str:
        return f"  [{self.code}] {self.req.id} ({self.req.where(root)})\n      {self.message}"


def validate(requirements: list[Requirement]) -> list[Error]:
    errors: list[Error] = []
    seen: dict[str, Requirement] = {}
    known: set[str] = {r.id for r in requirements}

    for req in requirements:
        meta = req.meta

        # --- identity -------------------------------------------------------
        if not ID_RE.match(req.id) or req.prefix not in PREFIXES:
            errors.append(Error("ID-FORMAT", req, f"'{req.id}' is not a valid requirement ID."))
            continue

        if req.id in seen:
            first = seen[req.id]
            errors.append(
                Error("ID-DUPLICATE", req, f"already defined at {first.where(repo_root())}.")
            )
        else:
            seen[req.id] = req

        meta_id = str(meta.get("id", ""))
        if not meta_id:
            errors.append(Error("META-MISSING", req, "no `id:` in the metadata block."))
        elif meta_id != req.id:
            errors.append(
                Error("ID-MISMATCH", req, f"heading says {req.id}, metadata says {meta_id}.")
            )

        # --- lifecycle ------------------------------------------------------
        status = req.status
        if not status:
            errors.append(Error("STATUS-MISSING", req, "no `status:` field."))
        elif status not in STATUSES:
            errors.append(
                Error("STATUS-INVALID", req, f"'{status}' is not one of {sorted(STATUSES)}.")
            )

        # --- traceability ---------------------------------------------------
        if req.is_root:
            if req.parents:
                errors.append(
                    Error("PARENT-UNEXPECTED", req, f"{req.prefix} is a root type; drop `parent:`.")
                )
        else:
            if not req.parents:
                errors.append(Error("PARENT-MISSING", req, "no `parent:` — this is an orphan."))
            for parent in req.parents:
                if parent not in known:
                    errors.append(
                        Error("PARENT-UNKNOWN", req, f"parent '{parent}' does not exist.")
                    )

        # --- verification ---------------------------------------------------
        # User needs are *validated* (does it solve the problem?) rather than
        # verified, and hazards and test cases are not requirements themselves.
        if req.prefix not in {"UN", "HAZ", "TC"}:
            method = str(meta.get("verification", ""))
            if not method:
                errors.append(
                    Error(
                        "VERIF-MISSING",
                        req,
                        "no `verification:` — if you cannot say how it is proven, "
                        "it is not yet a requirement.",
                    )
                )
            elif method not in VERIFICATION_METHODS:
                errors.append(
                    Error(
                        "VERIF-INVALID",
                        req,
                        f"'{method}' is not one of A(nalysis) I(nspection) T(est) D(emonstration).",
                    )
                )

        # --- type-specific rules --------------------------------------------
        if req.prefix == "SAF":
            mitigates = [str(m) for m in _listify(meta.get("mitigates"))]
            if not mitigates:
                errors.append(
                    Error("SAF-NO-HAZARD", req, "safety requirements must cite `mitigates: HAZ-xxx`.")
                )
            for hazard in mitigates:
                if not hazard.startswith("HAZ-"):
                    errors.append(Error("SAF-BAD-HAZARD", req, f"'{hazard}' is not a hazard ID."))
                elif hazard not in known:
                    errors.append(Error("SAF-NO-HAZARD", req, f"hazard '{hazard}' does not exist."))

        if req.prefix == "IF" and not str(meta.get("tolerance", "")):
            errors.append(
                Error(
                    "IF-NO-TOLERANCE",
                    req,
                    "assumptions about the out-of-scope stand/hammock need a `tolerance:` band.",
                )
            )

        if req.prefix == "TC":
            verifies = [str(v) for v in _listify(meta.get("verifies"))]
            if not verifies:
                errors.append(Error("TC-NO-TARGET", req, "test cases must list `verifies:` IDs."))
            for target in verifies:
                if target not in known:
                    errors.append(Error("TC-NO-TARGET", req, f"'{target}' does not exist."))

        # --- prose ----------------------------------------------------------
        if not req.body:
            errors.append(Error("BODY-EMPTY", req, "has no statement text."))
        elif req.prefix in OBLIGATION_TYPES and "shall" not in req.body.lower():
            errors.append(
                Error("NO-SHALL", req, "binding requirements must be written with 'shall'.")
            )

    return errors


def _listify(value: object) -> list[object]:
    if value is None or value == "":
        return []
    return value if isinstance(value, list) else [value]


def run(docs_dir: Path, root: Path, quiet: bool = False) -> int:
    requirements = collect(docs_dir)
    errors = validate(requirements)

    if not quiet:
        counts: dict[str, int] = {}
        for req in requirements:
            counts[req.prefix] = counts.get(req.prefix, 0) + 1
        summary = ", ".join(f"{k} {v}" for k, v in sorted(counts.items())) or "none"
        print(f"Parsed {len(requirements)} requirement(s): {summary}")

        if errors:
            print(f"\n{len(errors)} error(s):\n")
            for err in errors:
                print(err.render(root))
            print()
        else:
            print("No errors.")

    return 1 if errors else 0


def self_test(root: Path) -> int:
    """Prove the linter actually rejects malformed input, not merely that it runs."""
    fixtures = root / "tools" / "testdata"
    expected = {
        "ID-MISMATCH",
        "STATUS-INVALID",
        "PARENT-UNKNOWN",
        "VERIF-INVALID",
        "SAF-NO-HAZARD",
        "IF-NO-TOLERANCE",
        "NO-SHALL",
        "PARENT-MISSING",
    }

    found = {err.code for err in validate(collect(fixtures))}
    missing = sorted(expected - found)

    print(f"Self-test fixtures: {fixtures}")
    print(f"Detected codes: {', '.join(sorted(found)) or 'none'}")

    if missing:
        print(f"\nSELF-TEST FAILED — the linter did not detect: {', '.join(missing)}")
        return 1

    # The good fixture must stay clean, or the linter is over-eager.
    good_errors = validate(collect(fixtures / "good"))
    if good_errors:
        print("\nSELF-TEST FAILED — valid fixtures were rejected:")
        for err in good_errors:
            print(err.render(root))
        return 1

    print("\nSelf-test passed: bad fixtures rejected, good fixtures accepted.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true", help="validate the linter itself")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    root = repo_root()
    if args.self_test:
        return self_test(root)
    return run(root / "docs", root, quiet=args.quiet)


if __name__ == "__main__":
    sys.exit(main())
