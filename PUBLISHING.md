# Before publishing this repository

The working tree is anonymised. **The git history is not.**

## What is in the history

Everything committed before 2026-08-05 contains:

- **Competitor brand and product names**, in documents *and in commit messages*
- **Teardown photographs** of a competitor's internals — roughly 16 MB of images, committed between
  2026-08-05 and their untracking later the same day
- Verbatim German marketing copy, which identifies a company as surely as its name

Anonymising the working tree does not remove any of this. `git log`, `git show` and every GitHub
commit page still expose it, and rewriting published history is far harder than avoiding the
problem.

## Publishing safely

**Do not make this repository public.** Publish a fresh one instead:

```bash
# 1. Verify the working tree is clean of identifiers
grep -rniE 'Competitor A|Competitor B|Competitor C|A-1|A-2|A-3|B-1' \
     --include='*.md' --include='*.yml' . | grep -v '^./site/' | grep -v '^./.venv/'
#    (should print nothing; note "maly" also matches "anomaly" - check hits by eye)

# 2. Teardown images are already gitignored, so they will not be exported.
#    Confirm anyway:  ls ../abh-public/brainstorming/teardown/competitor-a/

# 3. Export the current tree with no history at all
git checkout-index -a -f --prefix=../abh-public/
cd ../abh-public
git init -b main
git add -A
git commit -m "Initial public release"
```

`COMPETITOR-KEY.md` is gitignored and will not be carried across. Confirm that before pushing.

## The teardown photographs

**Untracked as of 2026-08-05.** They remain on the owner's disk, are gitignored, and will not appear
in any future commit or in a `git checkout-index` export.

They are, however, **still in the history** of commits made before that date. See below.

Buying a product and examining it is normal and generally lawful, and factual technical description
is ordinary engineering practice. Publishing photographs of a competitor's internals is a different
act, and it invites a complaint even where it is defensible — which is why they are no longer
tracked. The engineering value is in `brainstorming/teardown/competitor-a/findings.md`: the part
numbers, the architecture, the parallel load path. None of that needs the images.

## What to keep checking

- **No brand names** in documents, file names, or commit messages
- **No verbatim marketing copy**, in any language
- **No claim that a competitor's product is unsafe, non-compliant or defective.** Describe what was
  observed, state the limits of the evidence, leave the conclusion unstated. These are shipped
  products that have been through conformity assessment; our observations are uncontrolled and
  untested. This matters more than the names do
- **No implied endorsement** — nothing suggesting a competitor is associated with this project

## A note on what this does and does not achieve

Anonymisation reduces the chance of a complaint and makes the project harder to read as an attack
on a specific company. It does not make the content unattributable: anyone in the industry will
recognise the product category, and a determined reader could identify the units from the
specifications alone.

If the intention is genuine publication — an article, a talk, an open-source release — the durable
protections are accuracy, restraint in what is claimed, and not publishing another company's
internals. Anonymity is the weakest of the three.

**This is engineering hygiene, not legal advice.** If publication matters commercially, take proper
advice on comparative claims and on reverse-engineering rules in your target market before you
publish.
