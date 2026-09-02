---
name: agent-census
description: Run and interpret the universal census inventory tool that counts tabs, UI screens, components, 3D models, routes, endpoints, data models and cleanliness metrics. Use when the user asks for project inventory, how many tabs or screens exist, before converting UI to 3D, checking findings count, or mentions census, inventory, or dashboard-latest.html.
---

# Agent Census — Universal Inventory Tool

Census is both a cleanliness enforcer and a project inventory tool usable on any stack (web, mobile, backend, 3D, game, generic).

## What It Counts

- **tabs** — navigation tabs + related config entries
- **ui_screens** — pages / screens before 3D conversion
- **ui_components** — reusable components
- **routes** / **backend_endpoints**
- **models_3d** — glb, gltf, obj, fbx, usd, stl, blend, etc.
- **textures_materials** / **data_models**
- **conversion tracking** — total UI before 3D, models total, progress percentage

## Cleanliness Checks

Census fails (or warns) when:

- Forbidden filenames exist (patch*.md, final.md, temp.md, etc.)
- Active findings > 10
- Missing distillation for completed findings
- Registry out of sync with filesystem
- PRODUCT-KNOWLEDGE.md missing required sections
- Session logs incomplete

## How to Run

```bash
python scripts/census.py --base . --write
```

Produces:

- `docs/census/census-YYYY-MM-DD.json` (full machine data)
- `docs/census/census-report-YYYY-MM-DD.md` (human summary)
- `docs/census/inventory-YYYY-MM-DD.json` (inventory only)
- `docs/census/dashboard-latest.html` (visual dashboard)

Always run census before creating a checkpoint and at the end of a session.

## Config

Edit `.agent/census/census.config.json` to match the stack. File patterns determine what is counted for each category.

## Typical Usage Patterns

- Before any UI → 3D conversion decision → run census to know current counts
- After adding tabs / screens / models → run census to update inventory
- Before endorsement / advance → run census to prove cleanliness
- At session end → run census and include results in complete_trace

## Integration with Other Skills

- Called by file-update protocol (agent-continuity)
- Results feed dictionary-manager and architecture-map
- Cleanliness failures trigger reconciliation-manager style investigation
