# Universal AGENT Toolkit

> **FRONT-DOOR ONLY** — Pure wiring + status. Keep under 80 lines.  
> No findings, no code, no TODOs, no logs.

## What This Is

Reusable agent operating system for any future large project.  
Enforces continuity, anti-repeat knowledge, minimalism, and O-R-U-C-A-V-E-A discipline.

## Hierarchy of Authority (Read in this order)

1. **Source-of-Truth** (Product Law) — defined in [`POLICY.md`](./POLICY.md) §1  
2. [`POLICY.md`](./POLICY.md) — Constitution  
3. [`PRODUCT-KNOWLEDGE.md`](./PRODUCT-KNOWLEDGE.md) — Permanent brain (especially Anti-Patterns)  
4. [`MASTERPLAN.md`](./MASTERPLAN.md) — Conceptual map + current XXX  
5. [`AI_ASSISTANT_READ_ME.md`](./AI_ASSISTANT_READ_ME.md) — Agent OS (reading order + gates)  
6. [`ENDORSEMENT.md`](./ENDORSEMENT.md) — What is already approved  

## Layer Separation

- **Governance / Canonical Layer** → the 6 files above + `.agent/` + `docs/` + `skills/` + `scripts/`
- **Project-Development Layer** → `src/` only (code). Nothing else belongs there.

## Quick Start

```bash
cp -r agent-toolkit my-new-project
cd my-new-project
# 1. Define Source-of-Truth + fill the 6 canonical files
# 2. python scripts/census.py --base . --write
# 3. Start session log + first checkpoint
```

## Start Here

- Humans & first-time explorers → [`QUICKSTART.md`](./QUICKSTART.md)
- Full wiring → [`docs/STRUCTURE.md`](./docs/STRUCTURE.md)

## Full Repo Map

See [`docs/STRUCTURE.md`](./docs/STRUCTURE.md) for complete wiring and descriptions of every folder.

## Key Tools (no code yet)

| Tool | Path | Purpose |
|------|------|---------|
| Census | `scripts/census.py` | Inventory + cleanliness |
| Skills | `skills/*/SKILL.md` | Phase skills (incl. canonical-build) |
| Knowledge Search | `scripts/knowledge-search.py` | Anti-pattern check |
| New XXX | `scripts/new-xxx.py` | Scaffold next finding |

## Status

- Current focus: Toolkit baseline (no product code yet)
- Registry: `.agent/continuity/registry.json`
- Skills: 20 available (including `canonical-build`)

## What NEVER goes in this README

Findings • logs • code • TODOs • patch notes • product details
