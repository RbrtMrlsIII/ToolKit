# 006-team-quality-tool-quality-capability-entitlements

**Field:** Product / Capability Governance
**Phase:** commercial-capability
**Target:** team-quality-tool-quality-capability-entitlements
**Impact:** SYSTEMIC
**Status:** RECORDED — NOT YET ENDORSED OR DISTILLED
**Date:** 2026-09-03

## Generalized lesson
A multi-AI product may need to separate the quality/capacity of AI teamwork from the breadth of tools and integrations that the team can use.

A reusable planning model should distinguish:

- team quality: teamwork mode, seat capacity, model-capability tier, orchestration/resource capacity;
- tool quality: base product capabilities plus optional tools, plugins, MCP servers, and specialist integrations;
- provider entitlement: external provider/account capability, which must not be implied by the consuming product's subscription;
- capability state: available, installed/configured, entitled, provider-compatible, authorized, project-scoped, seat-allowed, usable.

Core product capabilities do not automatically need to be exposed as MCP. The product should keep its own identity, authorization, orchestration, durable-state, approval, and policy authorities above any integration protocol.

A consuming product should also distinguish planning-stage deliberation from working-stage execution and preserve user intent across sequential AI contributions. The latest AI message is not authority merely because it is the newest contribution.

## Why it matters
Without these separations, subscription design, provider capability, tool access, and orchestration can collapse into one ambiguous concept. That creates implementation drift, false entitlement assumptions, and UI designs that expose controls the backend cannot safely honor.

## Source
Validated from TeamAi pre-029 planning discussions and repository architecture reconciliation. TeamAi-specific pricing, provider selections, exact model catalogs, and exact Tool Quality packs remain project-owned and are intentionally excluded from this generalized lesson.

## Distillation status
Recorded for later generalization review. Do not add to permanent Toolkit Product Knowledge until the lesson is validated through implementation/evidence and generalized beyond TeamAi.
