#!/usr/bin/env python3
"""Create the next ADR from the template.

    python tools/new_adr.py "MCU selection"

Accepted ADRs are immutable. To change a decision, create a new ADR that
supersedes the old one and set the old one's status accordingly.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date

from reqlib import repo_root

ADR_DIR = "docs/04-decisions"


def slugify(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("title", help="short decision title, e.g. 'MCU selection'")
    args = parser.parse_args()

    adr_dir = repo_root() / ADR_DIR
    used = {
        int(m.group(1))
        for path in adr_dir.glob("ADR-*.md")
        if (m := re.match(r"ADR-(\d{4})", path.name))
    }
    number = max(used, default=0) + 1

    slug = slugify(args.title)
    path = adr_dir / f"ADR-{number:04d}-{slug}.md"
    if path.exists():
        print(f"{path} already exists.")
        return 1

    template = (adr_dir / "template.md").read_text(encoding="utf-8")
    content = (
        template.replace("ADR-XXXX", f"ADR-{number:04d}")
        .replace("<Decision title>", args.title)
        .replace("<YYYY-MM-DD>", date.today().isoformat())
    )
    path.write_text(content, encoding="utf-8")

    rel = path.relative_to(repo_root())
    print(f"Created {rel}")
    print(f"Add to mkdocs.yml nav:\n      - ADR-{number:04d} {args.title}: {path.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
