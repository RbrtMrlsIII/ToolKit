# 003-canonical-backend-extension

**Field:** Foundation
**Phase:** architecture
**Target:** canonical-backend-extension
**Impact:** SYSTEMIC
**Status:** RECORDED
**Date:** 2026-09-03

## Observation
A mature backend architecture can contain multiple canonical authorities and flows without becoming a single endpoint or single wire.

## Generalized lesson
Product growth should extend existing authority boundaries instead of creating parallel ownership paths.

- Additional authentication methods should converge on the existing identity authority and stable domain identity root.
- Additional payment buttons, subscription products, plans, promotions, and provider-facing flows should extend the existing commerce authority/correlation boundary.
- Additional tasks, events, providers, and runtime capabilities should extend durable-state and trusted-execution contracts.
- Browser and verification surfaces should remain non-authoritative for identity, payment, entitlement, and durable domain state.
- Replacing an authority boundary is an architecture change, not an ordinary feature extension.

## Why it matters
Without an explicit extension rule, feature growth can quietly create a second identity, payment, database, or browser-owned state path even when each individual feature appears locally correct.

## Evidence source
TeamAi TEAM-BACKEND-001 backend authority reconciliation and Gate-3 persistence work, including `PRODUCT_LAW.md`, `MASTERPLAN.md`, and the canonical backend extension invariant.

## Distillation status
Recorded as a generalized ToolKit finding. It is intentionally not yet added to permanent endorsed `PRODUCT-KNOWLEDGE.md`; distillation requires the ToolKit lifecycle and endorsement rules to be satisfied.
