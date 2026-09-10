# TeamAi Case Study — Canonical Structure Preservation Failure

**Classification:** HISTORICAL / UPSTREAM LEARNING CASE
**Consumer:** TeamAi
**Purpose:** Preserve the reusable lesson without importing TeamAi product law or implementation details into Toolkit.

## Observed failure

A consuming-project governance change correctly attempted to update a current execution frontier and its canonical indexes. The governance gate later detected that one of the canonical indexes had been changed without synchronized updates. A follow-up documentation PR then exposed a second failure class: the PR made the intended frontier update but also removed a large, unrelated canonical planning section.

The important failure was not that one phrase disappeared. The failure was that a narrow semantic request was able to cause unrelated canonical knowledge loss while still looking superficially plausible as a documentation change.

## Evidence

- TeamAi governance gate reported spatial implementation drift when canonical indexes were not updated.
- TeamAi PR #253 subsequently showed unrelated deletion inside `MASTERPLAN.md` while performing a frontier synchronization change.
- TeamAi's existing governance model therefore demonstrated both semantic consistency checking and the need for structural preservation checking.

## Generalized lesson

A governance system must protect the **integrity of the knowledge structure itself**, not merely verify that expected new strings or claims are present.

## Reusable Toolkit rule

For canonical documents:

```text
requested semantic scope
       ↓
protected unrelated structure
       ↓
structural diff validation
       ↓
fail closed on unexplained section loss
```

A validator should detect unexpected heading removal, suspicious large canonical deletions, and changes outside the declared semantic scope.

## What does NOT move upstream

Do not copy TeamAi-specific product law, Firebase/PayPal/GitHub details, 029 terminology, repository policy, domain schemas, or implementation claims into Toolkit.

Only the generalized governance lesson moves upstream.
