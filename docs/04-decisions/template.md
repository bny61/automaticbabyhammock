# ADR-XXXX — &lt;Decision title&gt;

```
Status:      proposed | accepted | rejected | superseded by ADR-YYYY
Date:        <YYYY-MM-DD>
Deciders:    <who>
Trade study: <TS-xxx, or "none">
Affects:     <requirement IDs>
```

## Context

What situation forces a decision? What is true today, what constraints apply, and what happens if
nothing is decided? State facts and cite sources — benchmark data, regulation, model results.

## Options considered

### Option A — <name>

Description. **Pros:** … **Cons:** …

### Option B — <name>

Description. **Pros:** … **Cons:** …

*(A decision with only one option considered is not a decision. If there is genuinely no
alternative, say why explicitly.)*

## Decision

The single option chosen, stated plainly.

## Rationale

Why this option beats the others **against the criteria that matter here**. If a trade study
produced a score, reference it rather than repeating it.

## Consequences

**Positive:** what this makes possible or cheaper.

**Negative:** what this costs or forecloses. *Be honest — an ADR with no negative consequences is
an advertisement, not a decision record.*

**Requirements affected:** which IDs are created, changed or constrained.

**Follow-on work:** what must now happen.

## Revisiting

Under what circumstances would this decision be wrong? What evidence would justify superseding it?

---

!!! warning "Accepted ADRs are immutable"
    Once `accepted`, this file is never edited. To change the decision, write a new ADR that
    supersedes it and set this one's status to `superseded by ADR-YYYY`.
