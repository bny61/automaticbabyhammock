"""Shared parsing for requirement blocks in the docs tree.

A requirement is a level-3 heading whose text starts with an ID, immediately
followed by a fenced ``yaml`` block of flat key/value metadata, then free prose:

    ### SYS-014 - Continuous operation without thermal derating

    ```yaml
    id: SYS-014
    status: draft
    parent: UN-006
    verification: T
    ```

    The ECU shall operate continuously ...

The metadata schema is deliberately flat (scalars and simple ``[a, b]`` lists),
so this module parses it directly rather than depending on PyYAML. Keeping the
linter dependency-free means it runs in a bare checkout and in CI without a venv.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

# Prefixes and whether the requirement type is a traceability root (needs no parent).
PREFIXES: dict[str, bool] = {
    "UN": True,  # user need
    "HAZ": True,  # hazard
    "SYS": False,  # system requirement
    "HW": False,  # electrical requirement
    "SW": False,  # software requirement
    "MEC": False,  # mechanical requirement (in scope)
    "IF": False,  # assumption about the out-of-scope stand / hammock
    "SAF": False,  # safety requirement
    "TC": False,  # test case
}

STATUSES = {"draft", "review", "approved", "obsolete"}
VERIFICATION_METHODS = {"A", "I", "T", "D"}

#: Types that state a binding obligation and must therefore use "shall".
OBLIGATION_TYPES = {"SYS", "HW", "SW", "MEC", "SAF"}

ID_PATTERN = r"(?:UN|HAZ|SYS|HW|SW|MEC|IF|SAF|TC)-\d{3}"
ID_RE = re.compile(rf"^{ID_PATTERN}$")
# Requirement headings carry an explicit `{#sys-001}` anchor so that cross-document
# links can target the ID directly instead of a slug of the whole title.
HEADING_RE = re.compile(rf"^###\s+({ID_PATTERN})\s*[-–—]\s*(.+?)\s*(?:\{{#[\w-]+\}})?\s*$")
ANY_ID_RE = re.compile(ID_PATTERN)
FENCE_RE = re.compile(r"^\s*(`{3,})\s*(\w*)\s*$")


def _fence(line: str) -> tuple[int, str] | None:
    """Return (backtick count, language) if the line is a fence delimiter."""
    match = FENCE_RE.match(line)
    if not match:
        return None
    return len(match.group(1)), match.group(2)


@dataclass
class Requirement:
    id: str
    title: str
    path: Path
    line: int
    meta: dict[str, object] = field(default_factory=dict)
    body: str = ""

    @property
    def prefix(self) -> str:
        return self.id.split("-", 1)[0]

    @property
    def is_root(self) -> bool:
        return PREFIXES.get(self.prefix, False)

    @property
    def parents(self) -> list[str]:
        return _as_list(self.meta.get("parent"))

    @property
    def status(self) -> str:
        return str(self.meta.get("status", ""))

    def where(self, repo_root: Path) -> str:
        try:
            rel = self.path.relative_to(repo_root)
        except ValueError:
            rel = self.path
        return f"{rel}:{self.line}"


def _as_list(value: object) -> list[str]:
    """Normalise a scalar, list or empty metadata value to a list of strings."""
    if value is None or value == "":
        return []
    if isinstance(value, list):
        return [str(v) for v in value]
    return [str(value)]


def _parse_scalar(raw: str) -> object:
    raw = raw.strip()
    if raw.startswith("[") and raw.endswith("]"):
        inner = raw[1:-1].strip()
        if not inner:
            return []
        return [item.strip().strip("\"'") for item in inner.split(",") if item.strip()]
    return raw.strip("\"'")


def parse_meta_block(lines: list[str]) -> dict[str, object]:
    """Parse the flat key/value subset of YAML used in requirement blocks."""
    meta: dict[str, object] = {}
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if ":" not in stripped:
            continue
        key, _, raw = stripped.partition(":")
        meta[key.strip()] = _parse_scalar(raw)
    return meta


def parse_file(path: Path) -> list[Requirement]:
    """Extract every requirement block from one Markdown file."""
    requirements: list[Requirement] = []
    lines = path.read_text(encoding="utf-8").splitlines()

    i = 0
    open_fence: int | None = None  # backtick count of the currently open fence
    while i < len(lines):
        line = lines[i]

        # Track fences so headings inside illustrative code samples are not
        # mistaken for real requirements. Fences nest: a ````-delimited example
        # may itself contain a ```yaml block, so only a delimiter at least as
        # long as the opening one closes it.
        fence = _fence(line)
        if fence:
            ticks, _lang = fence
            if open_fence is None:
                open_fence = ticks
            elif ticks >= open_fence:
                open_fence = None
            i += 1
            continue
        if open_fence is not None:
            i += 1
            continue

        heading = HEADING_RE.match(line)
        if not heading:
            i += 1
            continue

        req_id, title = heading.group(1), heading.group(2)
        heading_line = i + 1
        i += 1

        # Find the metadata fence, allowing blank lines between it and the heading.
        while i < len(lines) and not lines[i].strip():
            i += 1

        meta: dict[str, object] = {}
        if i < len(lines):
            fence = _fence(lines[i])
            if fence and fence[1] == "yaml":
                opener = fence[0]
                i += 1
                block: list[str] = []
                while i < len(lines):
                    closing = _fence(lines[i])
                    if closing and closing[0] >= opener:
                        break
                    block.append(lines[i])
                    i += 1
                i += 1  # consume closing fence
                meta = parse_meta_block(block)

        # Body runs until the next heading of level <= 3, ignoring headings that
        # appear inside fenced blocks (shell comments, example Markdown, ...).
        body_lines: list[str] = []
        body_fence: int | None = None
        while i < len(lines):
            fence = _fence(lines[i])
            if fence:
                ticks, _lang = fence
                if body_fence is None:
                    body_fence = ticks
                elif ticks >= body_fence:
                    body_fence = None
            elif body_fence is None and re.match(r"^#{1,3}\s", lines[i]):
                break
            body_lines.append(lines[i])
            i += 1

        requirements.append(
            Requirement(
                id=req_id,
                title=title,
                path=path,
                line=heading_line,
                meta=meta,
                body="\n".join(body_lines).strip(),
            )
        )

    return requirements


def collect(docs_dir: Path) -> list[Requirement]:
    """Collect every requirement under ``docs_dir``, in deterministic order."""
    requirements: list[Requirement] = []
    for path in sorted(docs_dir.rglob("*.md")):
        # The traceability matrix is generated from requirements; it never defines any.
        if path.name == "traceability-matrix.md":
            continue
        requirements.extend(parse_file(path))
    return requirements


def index(requirements: list[Requirement]) -> dict[str, Requirement]:
    """Map ID to requirement, keeping the first definition of a duplicated ID."""
    out: dict[str, Requirement] = {}
    for req in requirements:
        out.setdefault(req.id, req)
    return out


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent
