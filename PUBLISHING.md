# Before publishing this repository

The working tree is anonymised. **The git history is not.**

## History was rewritten on 2026-08-05

The original history contained brand names — in documents *and in commit messages* — plus about
16 MB of teardown photographs. All of it was removed with `git-filter-repo`, and the GitHub
repository was **deleted and recreated from scratch**, so no unreferenced objects remain
server-side. This is the strong form: a force-push alone would have left the old objects reachable
by SHA until GitHub garbage-collected them.

Verified after the rewrite:

| Check | Result |
|---|---|
| Image blobs in any commit | 0 |
| Brand names in any historical file version | 0 |
| Brand names in any commit message | 0 |
| Pack size | 16.22 MiB → 197 KiB |
| Commit history | intact, not squashed |

A caution learned the hard way: replacing a short model name across history can corrupt ordinary
words — one of them is a substring of *anomaly* and *normally*. Replace the exact literal string,
not the bare name, and check afterwards.

**A full backup of the original history exists as a git bundle** outside the repository. If the
codename mapping is ever needed against the original record, it is there. Keep it private.

Do not undo this by committing a file that contains the names — including a helpful "check for the
names" script. That mistake was made once already: the check command below deliberately builds its
pattern from the gitignored key rather than hard-coding the brands.

## Publishing safely

**Do not make this repository public.** Publish a fresh one instead:

```bash
# 1. Verify the working tree is clean of identifiers.
#    The brand names live only in COMPETITOR-KEY.md, which is gitignored - so build
#    the pattern from it rather than writing the names into a tracked file.
PATTERN=$(awk -F'|' '/^\| (Competitor|A-|B-|Other)/ {gsub(/ /,"",$3); print $3}' \
          COMPETITOR-KEY.md | grep -v '^$' | paste -sd'|' -)
grep -rniE "$PATTERN" --include='*.md' --include='*.yml' . \
     | grep -v '^./site/' | grep -v '^./.venv/'
#    (should print nothing; beware short names that are substrings of ordinary words)

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
