# Architecture Map — Auto-Generated

Date: 2026-09-01

## Project Inventory (from Census)

- Tabs: Counts how many tabs do we have (files + entries in tabs config) — before converting to 3D
- UI Screens: How many UI screens/pages before converting to 3D
- UI Components: Reusable components
- Routes: Navigation entries
- Backend Endpoints: API routes
- 3D Models: glb/gltf/obj/fbx/usd before/after conversion
- Data Models: schemas/tables

Conversion Summary: Before 3D: UI items + Tabs, After: 3D Models, Progress % tracked

## Authority → Consumers

```
Authority (Source of Truth)
  ├── docs/contracts/ — API contract, schema, spec
  ├── PRODUCT-KNOWLEDGE.md — Permanent brain (Validated Patterns, Anti-Patterns)
  └── .agent/continuity/registry.json — Machine truth (current_xxx, knowledge_index)

Consumers
  ├── src/frontend/ — UI Screens + Components + Tabs (counted by census)
  ├── src/backend/ — Endpoints + Data Models (supabase, firebase, wowsql)
  ├── 3D Layer — Models converted from UI (tracked by census inventory)
  └── Mobile Clients — Consume via API contract
```

## Dependency Map

| Authority | Consumers | Contract File |
|-----------|-----------|---------------|
| api-v1.yaml | frontend, mobile | docs/contracts/api-v1.yaml |
| supabase schema | backend, frontend | backend-integrations-repo/supabase/schema.sql |
| PRODUCT-KNOWLEDGE.md | all agents | PRODUCT-KNOWLEDGE.md |

## Conversion Flow UI → 3D

```
UI Screens + Tabs (census counts before conversion)
  ↓ census: how many tabs, how many UI
UI Components
  ↓ conversion tracking in census.config.json
3D Models (glb/gltf/obj/fbx) — docs/census/dashboard-latest.html shows progress
  ↓ storage/upload-3d.ts
Storage (Supabase/Firebase/WowSQL)
```

## Execution Flow

Observe → Record → Understand → Classify → Align → Validate → Endorse → Advance
+ Distill to PRODUCT-KNOWLEDGE.md + Census Dashboard + Checkpoint + Archive

Quadruple + Knowledge = 5 evidences

## Backend Integrations

- Supabase: client.ts, schema.sql, auth, policies, backups/ for cloud sync
- Firebase: config, firestore, auth, storage
- WowSQL: schema.sql with tabs table, census_inventory table
- GitHub: workflows/auto-distill-census.yml (auto census + dashboard)
- PayPal/Stripe: clients + webhooks
- Storage: upload-3d.ts for 3D asset conversion tracking
- Auth: middleware, jwt, session

## Skills + Prompts + Tools

- Skills: 16 skills as MD files in skills/ + .agent/skills/
- Prompts: prompts/ (7 ready-to-paste for mobile AI)
- Tools: census.py (inventory + cleanliness), knowledge-search.py, sync-knowledge.py, new-xxx.py, sync-cloud.py, skills-loader.mjs, architecture-map-generator.py
- Hooks: scripts/pre-commit blocks commit if FAIL, scripts/auto-distill.py auto-distills

## How to Use This Map on Mobile (30 sec overview)

1. Read this map
2. Read PRODUCT-KNOWLEDGE.md Anti-Patterns (prevent repeat errors)
3. Run census: python scripts/census.py --base . --write
4. Check dashboard: docs/census/dashboard-latest.html
5. Load skill: node skills-loader.mjs → tells you current XXX + skill to load
6. Execute phase per skill
7. Distill to PRODUCT-KNOWLEDGE.md before archiving
