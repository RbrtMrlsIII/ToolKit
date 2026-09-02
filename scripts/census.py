#!/usr/bin/env python3
"""
census.py — Universal Project Inventory + Cleanliness Tool
Applicable to ALL project types: web, mobile, backend, 3d, game, generic

Counts:
- Project structure cleanliness: forbidden files, findings count, knowledge distillation
- Project inventory: how many tabs, how many UI screens, UI components, routes, endpoints, 3D assets before converting to 3D
- Conversion progress: UI -> 3D

Usage:
  python scripts/census.py --base . --write
  python scripts/census.py --base . --write --inventory-only

Outputs:
  .agent/census/census-YYYY-MM-DD.json (machine-readable)
  docs/census/census-report-YYYY-MM-DD.md (human-readable)
  docs/census/inventory-YYYY-MM-DD.json (inventory only)

Config: .agent/census/census.config.json — edit patterns to match your stack
"""

import pathlib, json, re, sys, datetime, fnmatch, argparse, os

DEFAULT_MAX_FINDINGS = 10
DEFAULT_MAX_KNOWLEDGE_LINES = 500
DEFAULT_FORBIDDEN = ["patch*", "final*.md", "final-*.md", "fix*.md", "dd*.md", "temp*", "backup*", "old*", "new*.md", "copy*", "v1*", "test2*"]

def load_config(root: pathlib.Path):
    config_path = root / ".agent/census/census.config.json"
    if not config_path.exists():
        config_path = root / "docs/census/census.config.json"
    if config_path.exists():
        try:
            return json.loads(config_path.read_text(encoding="utf-8"))
        except:
            pass
    # fallback default
    return {
        "forbidden_patterns": DEFAULT_FORBIDDEN,
        "max_findings": DEFAULT_MAX_FINDINGS,
        "max_knowledge_lines": DEFAULT_MAX_KNOWLEDGE_LINES,
        "inventory": {
            "tabs": {"file_patterns": ["**/tabs.*", "**/*Tabs.*", "**/tabBar.*"]},
            "ui_screens": {"file_patterns": ["src/screens/**/*.*", "src/pages/**/*.*", "src/views/**/*.*"]},
            "ui_components": {"file_patterns": ["src/components/**/*.*", "components/**/*.*"]},
            "models_3d": {"file_patterns": ["**/*.glb", "**/*.gltf", "**/*.obj", "**/*.fbx"]}
        }
    }

def find_forbidden(root: pathlib.Path, patterns):
    forbidden = []
    for p in root.rglob("*"):
        if p.is_file():
            name = p.name.lower()
            rel = str(p.relative_to(root))
            if ".git" in rel or "node_modules" in rel or "__pycache__" in rel or ".agent/census" in rel:
                continue
            if name.startswith("template-"):
                continue
            for pat in patterns:
                if fnmatch.fnmatch(name, pat.lower()):
                    forbidden.append(rel)
                    break
    return forbidden

def count_findings(root: pathlib.Path):
    findings_dir = root / "docs/findings"
    if not findings_dir.exists():
        return 0, []
    files = [f for f in findings_dir.glob("*.md") if "TEMPLATE" not in f.name.upper()]
    return len(files), [f.name for f in files]

def count_inventory(root: pathlib.Path, inventory_config):
    results = {}
    for key, cfg in inventory_config.items():
        patterns = cfg.get("file_patterns", [])
        exclude_substr = cfg.get("exclude", [])
        files_matched = set()
        for pat in patterns:
            # Use rglob with pattern handling ** 
            # Simplify: use pathlib glob
            try:
                for f in root.glob(pat):
                    if f.is_file():
                        rel = str(f.relative_to(root))
                        if any(ex in rel for ex in exclude_substr):
                            continue
                        if "node_modules" in rel or ".git" in rel or "dist" in rel or ".next" in rel:
                            continue
                        files_matched.add(rel)
            except Exception:
                # fallback fnmatch scan
                for p in root.rglob("*"):
                    if p.is_file():
                        rel = str(p.relative_to(root))
                        if fnmatch.fnmatch(rel, pat) or fnmatch.fnmatch(p.name, pat):
                            files_matched.add(rel)
        results[key] = {
            "count": len(files_matched),
            "description": cfg.get("description", ""),
            "files": sorted(list(files_matched))[:50],  # limit list to 50 for readability
            "total_matched": len(files_matched)
        }
        # Special: for tabs, try to count entries inside files that define tabs array
        if key == "tabs":
            tab_entries = 0
            for rel_path in files_matched:
                try:
                    fp = root / rel_path
                    if fp.suffix in [".json", ".js", ".ts", ".tsx", ".jsx"]:
                        txt = fp.read_text(encoding="utf-8", errors="ignore")
                        # crude count: occurrences of '"name":' or 'path:' in tabs config, or count array items
                        # Look for tabs: [ or Tab entries
                        m = re.findall(r'"tabs"\s*:\s*\[', txt)
                        if m:
                            # try to count objects in array by counting { in that section (approx)
                            tab_entries += txt.count('"path"') + txt.count('"name"') 
                except:
                    pass
            results[key]["estimated_tab_entries"] = tab_entries

    # Conversion tracking
    ui_total = results.get("ui_screens", {}).get("count", 0) + results.get("ui_components", {}).get("count", 0)
    models_total = results.get("models_3d", {}).get("count", 0)
    tabs_total = results.get("tabs", {}).get("count", 0)
    conversion_progress = {
        "tabs_total": tabs_total,
        "ui_screens_total": results.get("ui_screens", {}).get("count", 0),
        "ui_components_total": results.get("ui_components", {}).get("count", 0),
        "models_3d_total": models_total,
        "total_ui_before_3d": ui_total,
        "conversion_note": f"You have {tabs_total} tabs, {ui_total} UI items (screens+components), {models_total} 3D models. Before converting to 3D, census shows inventory. After conversion, track models_3d converted vs UI remaining."
    }
    results["_conversion_summary"] = conversion_progress
    return results

def check_knowledge_distillation(root: pathlib.Path):
    findings_dir = root / "docs/findings"
    pk_path = root / "PRODUCT-KNOWLEDGE.md"
    registry_path = root / ".agent/continuity/registry.json"
    if not pk_path.exists():
        return {"error": "PRODUCT-KNOWLEDGE.md missing"}, []
    pk_text = pk_path.read_text(encoding="utf-8", errors="ignore")
    missing = []
    if findings_dir.exists():
        for f in findings_dir.glob("*.md"):
            if "TEMPLATE" in f.name.upper():
                continue
            m = re.match(r"(\d{3})-", f.name)
            if not m:
                continue
            xxx = m.group(1)
            if xxx == "000":
                continue
            if xxx not in pk_text:
                missing.append({"file": f.name, "xxx": xxx, "reason": f"XXX {xxx} not in PRODUCT-KNOWLEDGE.md"})
    try:
        reg = json.loads(registry_path.read_text()) if registry_path.exists() else {}
        knowledge_index = reg.get("knowledge_index", {})
    except:
        knowledge_index = {}
    return {"knowledge_index": knowledge_index}, missing

def check_pk_size(root: pathlib.Path):
    pk_path = root / "PRODUCT-KNOWLEDGE.md"
    if not pk_path.exists():
        return 0
    return len(pk_path.read_text(encoding="utf-8", errors="ignore").splitlines())

def check_registry(root: pathlib.Path):
    reg_path = root / ".agent/continuity/registry.json"
    if not reg_path.exists():
        return False, "registry.json missing"
    try:
        reg = json.loads(reg_path.read_text())
        current = reg.get("current_xxx", "")
        todo = reg.get("registry", {}).get("todo", []) or reg.get("todo", [])
        return True, f"current_xxx={current}, todo={len(todo) if isinstance(todo,list) else 0}"
    except Exception as e:
        return False, str(e)

def main():
    parser = argparse.ArgumentParser(description="Universal Project Census — tabs, UI, 3D inventory + cleanliness")
    parser.add_argument("--base", default=".", help="Repo base")
    parser.add_argument("--write", action="store_true", help="Write census files")
    parser.add_argument("--inventory-only", action="store_true", help="Only inventory, no cleanliness")
    args = parser.parse_args()
    root = pathlib.Path(args.base).resolve()
    config = load_config(root)
    forbidden_patterns = config.get("forbidden_patterns", DEFAULT_FORBIDDEN)
    max_findings = config.get("max_findings", DEFAULT_MAX_FINDINGS)
    max_pk = config.get("max_knowledge_lines", DEFAULT_MAX_KNOWLEDGE_LINES)
    inventory_cfg = config.get("inventory", {})
    
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    datetime_str = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # Cleanliness
    forbidden = [] if args.inventory_only else find_forbidden(root, forbidden_patterns)
    findings_count, findings_list = (0, []) if args.inventory_only else count_findings(root)
    knowledge_meta, missing_distill = ({}, []) if args.inventory_only else check_knowledge_distillation(root)
    pk_lines = 0 if args.inventory_only else check_pk_size(root)
    reg_ok, reg_msg = (True, "skipped") if args.inventory_only else check_registry(root)
    
    # Inventory (always)
    inventory = count_inventory(root, inventory_cfg)
    
    # Status
    status = "PASS"
    fails = []
    warns = []
    if not args.inventory_only:
        if forbidden:
            status = "FAIL"
            fails.append(f"Forbidden files: {forbidden[:3]}")
        if findings_count > max_findings:
            status = "FAIL"
            fails.append(f"Findings {findings_count} > {max_findings}")
        if missing_distill:
            status = "FAIL"
            fails.append(f"Missing distillation: {missing_distill}")
        if pk_lines > max_pk:
            warns.append(f"PK {pk_lines} > {max_pk}")
        if not reg_ok:
            status = "FAIL"
            fails.append(f"Registry: {reg_msg}")
    
    result = {
        "date": date_str,
        "datetime": datetime_str,
        "root": str(root),
        "status": status if not args.inventory_only else "INVENTORY",
        "project_types": config.get("project_types", []),
        "cleanliness": {
            "forbidden_files": {"count": len(forbidden), "files": forbidden},
            "findings": {"count": findings_count, "max": max_findings, "files": findings_list},
            "knowledge": {"pk_lines": pk_lines, "max_lines": max_pk, "missing_distillation": missing_distill, "meta": knowledge_meta},
            "registry": {"ok": reg_ok, "msg": reg_msg},
            "fails": fails,
            "warns": warns
        },
        "inventory": inventory
    }
    
    print(json.dumps(result, indent=2))
    
    if args.write:
        census_dir = root / ".agent/census"
        census_dir.mkdir(parents=True, exist_ok=True)
        (census_dir / f"census-{date_str}.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
        
        report_dir = root / "docs/census"
        report_dir.mkdir(parents=True, exist_ok=True)
        inv = inventory
        conv = inv.get("_conversion_summary", {})
        report_md = f"""# Census Report {date_str} — Universal Inventory + Cleanliness

**Status:** {status}
**Date:** {datetime_str}
**Project Types Supported:** {', '.join(config.get('project_types', []))}

## Project Inventory (All Project Types) — Tabs, UI, 3D Before Conversion

This is the project tool: how many tabs, how many UI before converting to 3D.

- **Tabs:** {inv.get('tabs', {}).get('count', 0)} tab files, estimated entries {inv.get('tabs', {}).get('estimated_tab_entries', 0)}
  - Files: {', '.join(inv.get('tabs', {}).get('files', [])[:5])}
- **UI Screens/Pages:** {inv.get('ui_screens', {}).get('count', 0)}
  - Files: {', '.join(inv.get('ui_screens', {}).get('files', [])[:5])}
- **UI Components:** {inv.get('ui_components', {}).get('count', 0)}
- **Routes:** {inv.get('routes', {}).get('count', 0)}
- **Backend Endpoints:** {inv.get('backend_endpoints', {}).get('count', 0)}
- **3D Models:** {inv.get('models_3d', {}).get('count', 0)} (glb, gltf, obj, fbx, usd)
- **Textures/Materials:** {inv.get('textures_materials', {}).get('count', 0)}
- **Data Models:** {inv.get('data_models', {}).get('count', 0)}

### Conversion Tracking (UI -> 3D)
- Tabs total: {conv.get('tabs_total', 0)}
- UI total before 3D: {conv.get('total_ui_before_3d', 0)} (screens + components)
- UI Screens: {conv.get('ui_screens_total', 0)}
- 3D Models total: {conv.get('models_3d_total', 0)}
- Note: {conv.get('conversion_note', '')}
- Progress: You have {conv.get('total_ui_before_3d', 0)} UI items to consider for 3D conversion. Track converted vs remaining in next census.

## Cleanliness (Minimalism + Knowledge)

- Forbidden files: {len(forbidden)} {'PASS' if not forbidden else 'FAIL'} — {forbidden[:3]}
- Findings: {findings_count}/{max_findings} {'PASS' if findings_count <= max_findings else 'FAIL'}
- Missing distillation: {len(missing_distill)} {'PASS' if not missing_distill else 'FAIL'} — {missing_distill[:2]}
- PK lines: {pk_lines}/{max_pk} {'PASS' if pk_lines <= max_pk else 'WARN'}
- Registry: {reg_msg}

### Fails
{chr(10).join(f'- {f}' for f in fails) if fails else '- None'}

### Warns
{chr(10).join(f'- {w}' for w in warns) if warns else '- None'}

## Next Actions
- If FAIL cleanliness: Fix forbidden, distill findings to PRODUCT-KNOWLEDGE.md, archive, re-run census
- For inventory: Use counts above to plan conversion to 3D. Update census.config.json patterns to match your stack (web/mobile/backend/3d/game/generic)
- Re-run census after each XXX: `python scripts/census.py --base . --write`
"""
        (report_dir / f"census-report-{date_str}.md").write_text(report_md, encoding="utf-8")
        (report_dir / f"inventory-{date_str}.json").write_text(json.dumps(inventory, indent=2), encoding="utf-8")
        print(f"\nWrote: .agent/census/census-{date_str}.json")
        print(f"Wrote: docs/census/census-report-{date_str}.md")
        print(f"Wrote: docs/census/inventory-{date_str}.json")
    
    sys.exit(0 if status in ["PASS", "INVENTORY"] else 1)

if __name__ == "__main__":
    main()
