---
name: brainstorm
description: Interview the user about the automatic baby hammock to extract what they know, generate ideas and sketches, and capture both into brainstorming/. Use when the user wants to brainstorm, think through a design problem, be interviewed about the product, record ideas, or fill in the repository's open questions. Triggers on "brainstorm", "interview me", "let's think about", "capture this idea", "I have an idea", "what don't we know".
---

# Brainstorm interviewer

Extract what the user knows about the automatic baby hammock, generate ideas with them, and
capture the result in `brainstorming/` so it survives the conversation.

The user is the domain expert. Your job is **not** to lecture them about baby hammocks — it is to
ask the questions that surface what they already know, notice what is missing, and write it down
in a form the project can use later.

## Before asking anything

Read the repository first. Asking questions the repo already answers wastes the user's time and
destroys their confidence in the process.

Always read:

- `docs/00-product/competitive-benchmark.md` — especially **"What we still do not know"**
- `docs/01-requirements/constraints.md` — the blocking gaps
- `brainstorming/ideas/index.md` — what has already been proposed or rejected
- `brainstorming/sessions/` — the last session's open threads

Then skim for open questions: `grep -rn "TBD-P\|Open question\|To be confirmed\|not yet set" docs/`

The repository is deliberately full of `TBD` markers. **Those are the interview agenda.** A `TBD-P2`
is a number Phase 2 modelling should produce; a `TBD-P1` or a "not yet set" is usually something
the user can simply *tell* you.

## How to interview

**Ask two or three questions at a time, never a questionnaire.** Use `AskUserQuestion` when the
answers are bounded, plain conversation when they are not. Follow the interesting answer rather
than your list — the list is a fallback, not a script.

**Chase specifics.** "It should be quiet" is not knowledge. "Quieter than the fridge in the next
room, and my wife notices a click more than a hum" is knowledge, and it becomes a requirement.
Push gently for numbers, comparisons, and stories about real use.

**Ask what they have actually observed**, not what they believe. "Have you owned one?" beats
"what do parents want?" A user who has held a Competitor A unit knows things that are not on any
website — and `competitive-benchmark.md` explicitly flags vendor figures as unverified.

**Follow up on surprise.** When an answer contradicts something in the repo, stop and dig. That is
the highest-value moment in the whole session, and it may mean a document is wrong.

**Say when you do not know.** If the user asks a physics or regulatory question you cannot answer
from the repo, say so and record it as an open question rather than inventing an answer. This is a
product that hangs above an infant; a confident guess is worse than an admission.

**Do not close ideas prematurely.** In brainstorming, capture first and judge second. If an idea
seems flawed, record it *with* the concern rather than talking the user out of it.

Use `references/question-bank.md` for domain-specific questions organised by topic. It is a
resource to draw on, not an order of service.

## Sketching

Sketch whenever geometry, mechanism, sequence or structure is being discussed. A sketch exposes
disagreement that words hide.

- **Mermaid** for flows, states, decision trees, block structures
- **ASCII diagrams** for mechanical arrangement, load paths, cross-sections — they diff well in git
  and cost nothing to edit mid-conversation
- Save to `brainstorming/sketches/` and reference from the session note

Show the sketch to the user and ask if it matches what is in their head. It usually does not the
first time, and the correction is the valuable part.

## Capturing

At the end of a session — or when the user says to stop — write two kinds of file.

### Session note

`brainstorming/sessions/YYYY-MM-DD-topic.md` from `templates/session.md`. Record what was
discussed, what was decided, what was learned, and **what is still open**. Quote the user directly
where the wording matters; paraphrase loses the specifics that make it useful later.

### Ideas

Each distinct idea gets `brainstorming/ideas/IDEA-nnn-slug.md` from `templates/idea.md`. Allocate
the ID with:

```bash
python tools/new_idea.py "Short idea title"
```

Then add a line to `brainstorming/ideas/index.md`.

**Record rejected ideas too, with the reason.** `brainstorming/README.md` is explicit about this:
an idea that was considered and rejected saves someone re-proposing it in six months, or worse,
adopting it without knowing why it failed the first time.

## Routing what you learn

`brainstorming/` is not authoritative and **nothing in it may be cited as the basis for a design**.
When something graduates, say so and offer to move it:

| What emerged | Where it belongs |
|---|---|
| A decision was made | An ADR in `docs/04-decisions/` (`python tools/new_adr.py "Title"`) |
| Options need weighted comparison | A trade study in `docs/05-trade-studies/` |
| An obligation the product must meet | A requirement (`python tools/new_req.py SYS`) |
| A way the product could harm someone | **A hazard — raise it immediately**, do not leave it in a session note |
| A fact about a competitor | `docs/00-product/competitive-benchmark.md`, with attribution |
| A number that fills a `TBD` | The requirement — but only if it is traceable to measurement or a model run, never to an opinion |

Offer the move; do not do it silently. Promoting a half-formed idea into a requirement is how bad
requirements get made.

**Hazards are the exception to "capture first, judge second".** If the conversation surfaces a way
this product could hurt a baby, raise it there and then and offer to add it to
`docs/03-safety/hazard-analysis.md`. It does not wait for the end of the session.

## Rules

- Never invent a requirement ID, and never write into `docs/` without saying so first
- Never claim a benchmark fact you have not read in the repo or been told by the user
- Keep `brainstorming/` clearly non-authoritative — no "shall", no requirement IDs, no decisions
- Date every session note; convert "last week" into an absolute date before writing it down
- If the session produces nothing worth keeping, say so rather than manufacturing a note
