# Brainstorming

Raw thinking: ideas, sketches, meeting notes, calculations on the back of an envelope, and
**dead ends**.

## Running a session

```
/brainstorm
```

Interviews you about the product, generates ideas and sketches with you, and captures the result
here. The skill reads the repository first, so its questions target the project's **actual** open
questions — the `TBD` markers in `docs/`, the "What we still do not know" section of the
[competitive benchmark](../docs/00-product/competitive-benchmark.md), and whatever the last session
left unanswered.

Defined in `.claude/skills/brainstorm/`.

## Structure

| | |
|---|---|
| `sessions/` | Interview notes, dated — [index](sessions/index.md) |
| `ideas/` | One file per idea, `IDEA-nnn` — [index](ideas/index.md) |
| `sketches/` | Diagrams and visual thinking — [README](sketches/README.md) |

Allocate an idea ID with `python tools/new_idea.py "Title"`.

## Why dead ends are kept

An idea that was considered and rejected is valuable information. Without a record it gets
proposed again in six months and re-evaluated from scratch — or worse, adopted by someone who does
not know why it was rejected the first time. Write down what was tried and why it failed.

## What belongs here

Anything not yet ready to be a requirement, a decision or a design. Half-formed thoughts are
welcome; that is the point of the directory.

## What does not

If it becomes a decision, it moves to an [ADR](../docs/04-decisions/index.md). If it becomes a
comparison, it moves to a [trade study](../docs/05-trade-studies/index.md). If it becomes an
obligation, it moves to a [requirement](../docs/01-requirements/index.md). If it is a way this
product could hurt a baby, it goes **straight** to the
[hazard analysis](../docs/03-safety/hazard-analysis.md) without waiting for the end of a session.

**Nothing in this directory may be cited as the basis for a design.** No "shall", no requirement
IDs, no decisions.
