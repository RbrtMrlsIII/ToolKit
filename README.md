# Universal AGENT Toolkit

> **FRONT-DOOR ONLY** — Pure wiring + status. Keep under 80 lines.  
> No findings, no code, no TODOs, no logs.

## What This Is

Reusable operating system for AI-assisted projects. It provides reusable skills, workspace governance, continuity, knowledge discipline, project/field adaptation, and scale adaptation.

ToolKit equips WebAi seats but does **not** own a consuming project's Product Law, domain rules, providers, implementation details, credentials, or authorization.

## Core Principle

```text
USER VISION
  ↓
PRODUCT_LAW.md
  ↓
MASTERPLAN.md
  ↓
skills + PRODUCT-KNOWLEDGE
  ↓
O-R-U-C-A-V-E-A
  ↓
validation + evidence
  ↓
endorsement
  ↓
knowledge / skill evolution
```

The goal is **disciplined capability**: capability grows together with governance, evidence, continuity, and safe adaptation.

## Universal vs Consumer Boundary

Toolkit knowledge is promoted only after validation + generalization. Consumer-specific product law and implementation remain downstream.

## Hierarchy of Authority

1. **User / project owner intent**
2. [`PRODUCT_LAW.md`](./PRODUCT_LAW.md)
3. [`POLICY.md`](./POLICY.md)
4. [`PRODUCT-KNOWLEDGE.md`](./PRODUCT-KNOWLEDGE.md)
5. [`MASTERPLAN.md`](./MASTERPLAN.md) + endorsed contracts
6. Current checkpoint + machine state
7. Everything else

## Layer Separation

- **Governance / Canonical** → 7 root canonical files + `.agent/` + `docs/` + `skills/` + `scripts/` + `validation/` + `builds/`
- **Project-Development** → consuming project's declared product-code layer only

## Start Here

- Humans → [`QUICKSTART.md`](./QUICKSTART.md)
- Product authority → [`PRODUCT_LAW.md`](./PRODUCT_LAW.md)
- Architecture → [`docs/TOOLKIT_ARCHITECTURE.md`](./docs/TOOLKIT_ARCHITECTURE.md)
- Seat / scaling → [`docs/WEB_AI_SEAT_FOUNDATION.md`](./docs/WEB_AI_SEAT_FOUNDATION.md)
- Full wiring → [`docs/STRUCTURE.md`](./docs/STRUCTURE.md)
- Manual deployment → [`docs/USER_MANUAL_DEPLOYMENT.md`](./docs/USER_MANUAL_DEPLOYMENT.md)

## Key Tools

| Tool | Path | Purpose |
|------|------|---------|
| Census | `scripts/census.py` | Inventory + cleanliness |
| Canonical Integrity | `scripts/canonical-integrity.py` | Fail-closed structural guard |
| Skills | `skills/*/SKILL.md` | Reusable execution procedures |
| Knowledge Search | `scripts/knowledge-search.py` | Anti-pattern check |
| New XXX | `scripts/new-xxx.py` | Scaffold next finding |

## Status

- Current focus: self-protecting universal foundation, XXX 003 RECORDED
- Skills: living catalog, expanded when validated baselines justify new reusable procedures
- Learning: TeamAi lesson generalized upstream without importing TeamAi product rules

## What NEVER goes in this README

Findings • logs • code • raw knowledge • patch notes • product-specific details
