#!/usr/bin/env python3
"""Allocate the next brainstorming idea ID and create the file from the template.

    python tools/new_idea.py "Drive the spring pack with a linear voice coil"

Ideas live in `brainstorming/` and are deliberately NOT requirements: they carry no
authority, and nothing in them may be cited as the basis for a design. They graduate
by becoming an ADR, a trade study, a requirement or a hazard.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date

from reqlib import repo_root

IDEA_DIR = "brainstorming/ideas"


def slugify(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:60]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("title", help="short idea title")
    parser.add_argument(
        "--topic",
        default="other",
        choices=["actuation", "control", "safety", "mechanical", "interface", "business", "other"],
    )
    parser.add_argument("--source", default="brainstorming session")
    args = parser.parse_args()

    root = repo_root()
    idea_dir = root / IDEA_DIR
    idea_dir.mkdir(parents=True, exist_ok=True)

    used = {
        int(m.group(1))
        for path in idea_dir.glob("IDEA-*.md")
        if (m := re.match(r"IDEA-(\d{3})", path.name))
    }
    number = max(used, default=0) + 1

    path = idea_dir / f"IDEA-{number:03d}-{slugify(args.title)}.md"
    if path.exists():
        print(f"{path} already exists.")
        return 1

    template = (root / ".claude/skills/brainstorm/templates/idea.md").read_text(encoding="utf-8")
    content = (
        template.replace("IDEA-nnn", f"IDEA-{number:03d}")
        .replace("<title>", args.title)
        .replace("<YYYY-MM-DD>", date.today().isoformat())
        .replace(
            "<session note, or who suggested it>",
            args.source,
        )
        .replace(
            "<actuation | control | safety | mechanical | interface | business | other>",
            args.topic,
        )
    )
    path.write_text(content, encoding="utf-8")

    rel = path.relative_to(root)
    print(f"Created {rel}")
    print(f"Now add to {IDEA_DIR}/index.md:")
    print(f"  | [IDEA-{number:03d}]({path.name}) | {args.title} | {args.topic} | raw |")
    return 0


if __name__ == "__main__":
    sys.exit(main())
