---
name: knowledge-promotion
description: Classify and promote validated lessons into reusable Toolkit knowledge without importing consumer-specific authority.
---

# Knowledge Promotion + Generalization

## Contract

A lesson may move upstream only through an explicit lifecycle:

```text
OBSERVED
  ↓
RECORDED
  ↓
VALIDATED
  ↓
GENERALIZATION REVIEW
  ├─ reusable → CANDIDATE → ENDORSED
  └─ specific  → CONSUMER-SPECIFIC (stay downstream)
```

## Inputs

- source finding and evidence
- source project / consumer
- affected responsibility, skill, or governance surface
- proposed reusable claim
- proof that the claim is not dependent on consumer-specific authority

## Rules

1. Never promote an unvalidated guess.
2. Never promote consumer-specific Product Law, credentials, provider decisions, runtime behavior, or domain semantics into Toolkit core.
3. A generalized claim must state the reusable mechanism, not the story of one consumer.
4. Promotion requires explicit validation and endorsement.
5. Rejection is a valid outcome and must preserve the downstream lesson without polluting Toolkit.
6. Promotion must identify the source evidence and target knowledge section.

## Required promotion record

```yaml
source_project: <consumer>
source_finding: <path>
source_evidence: <path>
classification: UNIVERSAL | ADAPTABLE | CONSUMER-SPECIFIC | EPHEMERAL
proposed_claim: <generalized lesson>
consumer_dependency: NONE | EXPLICIT
validation: PASS | FAIL
endorsement: PENDING | APPROVED | REJECTED
promotion_target: PRODUCT-KNOWLEDGE.md §<section>
```

## TeamAi test lesson

The TeamAi canonical-section-loss incident generalizes to: canonical changes must protect unrelated knowledge and fail closed on unexplained structural loss. TeamAi-specific document names, product law, and implementation details remain downstream.

## Verification

The validator must reject a promotion record with consumer-specific dependencies declared as UNIVERSAL, or with missing validation/evidence.
