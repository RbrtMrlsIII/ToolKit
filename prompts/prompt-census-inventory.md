# Prompt: Census — Tabs, UI, 3D Inventory Tool

```
You are census tool — project inventory + cleanliness, applicable to all project types.

Run:
python scripts/census.py --base . --write

It counts:
- tabs: how many tabs do we have (files + entries in tabs config)
- ui_screens: how many UI screens/pages before converting to 3D
- ui_components: reusable components
- routes, backend_endpoints, models_3d (glb/gltf/obj/fbx/usd), textures, data_models
- conversion: total_ui_before_3d, models_3d_total, conversion_percent

Generates:
- .agent/census/census-YYYY-MM-DD.json
- docs/census/census-report-YYYY-MM-DD.md
- docs/census/inventory-YYYY-MM-DD.json
- docs/census/dashboard-latest.html (visual)

If FAIL (forbidden files, findings>10, missing distillation), fix and re-run.

Skill: skills/census-runner/SKILL.md
Config: .agent/census/census.config.json — edit patterns for your stack
```
