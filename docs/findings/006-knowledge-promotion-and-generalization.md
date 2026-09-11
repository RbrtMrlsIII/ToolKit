# 006 — Knowledge Promotion + Generalization

**XXX:** 006-knowledge-promotion-and-generalization  
**Field:** Foundation / Knowledge  
**Status:** OBSERVED  
**Scope:** Universal Toolkit only

## Baseline

005 is frozen as the validated dynamic skill-resolution and scale-adaptation baseline. ToolKit already distinguishes UNIVERSAL, ADAPTABLE, CONSUMER-SPECIFIC, EPHEMERAL, HISTORICAL, CANDIDATE, and ENDORSED knowledge.

## Objective

Make upstream learning explicit, testable, and non-polluting: a consumer lesson can become a Toolkit candidate only after validation and generalization review, and becomes permanent knowledge only after endorsement.

## Implemented

- Added universal `knowledge-promotion` skill contract.
- Added machine-readable promotion schema.
- Added fail-closed validator.
- Added a TeamAi canonical-integrity generalization fixture.
- Added tests for missing endorsement, consumer-specific leakage, and approved universal promotion.
- Added the 006 execution/evidence continuity packet.

## Generalization decision under test

Generalizable lesson: canonical edits must preserve unrelated knowledge and fail closed on unexplained structural loss; legitimate future migrations must declare their successor or retirement reason.

Non-generalizable TeamAi details remain downstream and are not promoted.

## Boundary

This slice does not modify consumer Product Law, provider/runtime rules, credentials, permissions, or downstream repositories. It does not insert the candidate into `PRODUCT-KNOWLEDGE.md` until explicit endorsement satisfies the permanent-knowledge lifecycle.
