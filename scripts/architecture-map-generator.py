#!/usr/bin/env python3
"""
architecture-map-generator.py — Generates docs/architecture-map.md from census + dependency-map + contracts
Part of bright improvement #8
"""
import pathlib, json

root = pathlib.Path(".").resolve()
census_path = None
for p in [root / ".agent/census/census-latest.json", root / ".agent/census/census-2026-08-31.json", root / "docs/census/inventory-latest.json"]:
    if p.exists():
        census_path = p
        break
# Try find latest census json
if not census_path:
    for p in (root / ".agent/census").glob("census-*.json") if (root / ".agent/census").exists() else []:
        census_path = p
        break

inventory = {}
if census_path and census_path.exists():
    try:
        data = json.loads(census_path.read_text())
        inventory = data.get("inventory", data)
    except: pass

# Dependency map
dep_path = root / "docs/dependencies/dependency-map.md"
if not dep_path.exists():
    dep_path = root / "agent-repo-template/docs/dependencies/dependency-map.md"
dep_text = dep_path.read_text(encoding="utf-8", errors="ignore") if dep_path.exists() else "No dependency map"

# Contracts
contracts_dir = root / "docs/contracts"
if not contracts_dir.exists():
    contracts_dir = root / "agent-repo-template/docs/contracts"
contracts = list(contracts_dir.glob("*")) if contracts_dir.exists() else []

arch_md = f"""# Architecture Map — Auto-Generated

Date: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Project Inventory (from Census)

- Tabs: {inventory.get('tabs',{}).get('count',0)} — {inventory.get('tabs',{}).get('description','')}
- UI Screens: {inventory.get('ui_screens',{}).get('count',0)}
- UI Components: {inventory.get('ui_components',{}).get('count',0)}
- Routes: {inventory.get('routes',{}).get('count',0)}
- Backend Endpoints: {inventory.get('backend_endpoints',{}).get('count',0)}
- 3D Models: {inventory.get('models_3d',{}).get('count',0)}
- Data Models: {inventory.get('data_models',{}).get('count',0)}

Conversion Summary: {inventory.get('_conversion_summary',{{}}).get('note','')}

## Authority → Consumers

```
Authority (Source of Truth)
  ├── docs/contracts/ — {len(contracts)} contracts: {', '.join([c.name for c in contracts][:3])}
  ├── PRODUCT-KNOWLEDGE.md — Permanent brain (Validated Patterns, Anti-Patterns)
  └── .agent/continuity/registry.json — Machine truth

Consumers
  ├── src/frontend/ — UI Screens ({inventory.get('ui_screens',{}).get('count',0)}) + Components ({inventory.get('ui_components',{}).get('count',0)}) + Tabs ({inventory.get('tabs',{}).get('count',0)})
  ├── src/backend/ — Endpoints ({inventory.get('backend_endpoints',{}).get('count',0)}) + Data Models ({inventory.get('data_models',{}).get('count',0)})
  ├── 3D Layer — Models ({inventory.get('models_3d',{}).get('count',0)}) converted from UI
  └── Mobile Clients — Consume via API contract
```

## Dependency Map

{dep_text[:2000]}

## Conversion Flow UI → 3D

```
UI Screens ({inventory.get('ui_screens',{}).get('count',0)}) + Tabs ({inventory.get('tabs',{}).get('count',0)})
  ↓ census counts before conversion
UI Components ({inventory.get('ui_components',{}).get('count',0)})
  ↓ conversion tracking
3D Models ({inventory.get('models_3d',{}).get('count',0)}) — glb/gltf/obj/fbx
  ↓ storage/upload-3d.ts
Storage (Supabase/Firebase)
```

## Execution Flow

Observe → Record → Understand → Classify → Align → Validate → Endorse → Advance
+ Distill to PRODUCT-KNOWLEDGE.md + Census + Checkpoint

## Backend Integrations

- Supabase: schema.sql, client.ts, auth, policies
- Firebase: config, firestore, auth, storage
- WowSQL: schema.sql, connection.py/.mjs, tabs table, census_inventory table
- GitHub: workflows/census.yml (auto census + dashboard)
- PayPal/Stripe: paypal-client.ts, stripe-client.ts
- Storage: upload-3d.ts for 3D asset conversion tracking

## How to Use This Map on Mobile

1. Read this map (30 sec overview)
2. Read PRODUCT-KNOWLEDGE.md Anti-Patterns
3. Run census: python scripts/census.py --base . --write
4. Check dashboard: docs/census/dashboard-latest.html
5. Load skill for current XXX: skills/<phase>/SKILL.md
"""

out_path = root / "docs/architecture-map.md"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(arch_md, encoding="utf-8")
print(f"Wrote architecture map: {out_path}")

# Also write to agent-repo-template
alt_path = root / "agent-repo-template/docs/architecture-map.md"
alt_path.parent.mkdir(parents=True, exist_ok=True)
alt_path.write_text(arch_md, encoding="utf-8")
print(f"Wrote: {alt_path}")
