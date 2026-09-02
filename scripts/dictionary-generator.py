#!/usr/bin/env python3
"""
dictionary-generator.py — Generates docs/dictionary/DICTIONARY.md from .agent/dictionary/dictionary.json
Part of machine readable dictionary improvement
"""
import pathlib, json, datetime

root = pathlib.Path(".").resolve()
dict_json_path = root / ".agent/dictionary/dictionary.json"
if not dict_json_path.exists():
    dict_json_path = root / "agent-repo-template/.agent/dictionary/dictionary.json"
if not dict_json_path.exists():
    print("dictionary.json not found")
    exit(1)

data = json.loads(dict_json_path.read_text(encoding="utf-8"))

md = f"""# Dictionary — Human Readable (Auto-Generated)

Last Updated: {data.get('last_updated','')}
Last XXX: {data.get('last_xxx','')}
Total Entities: {data.get('stats',{}).get('total_entities',0)}
Total Terms: {data.get('stats',{}).get('total_terms',0)}
Last Growth: {data.get('stats',{}).get('last_growth','')}

## Terms

| Term | Definition | File | XXX | Created At |
|------|------------|------|-----|------------|
"""

terms = data.get('entities',{}).get('terms',{})
for term, info in terms.items():
    md += f"| {term} | {info.get('definition','')} | {info.get('file','')} | {info.get('xxx','')} | {info.get('created_at','')} |\n"

md += "\n## Entities\n"
for entity_key in ["tabs","ui_screens","ui_components","models_3d","backend_endpoints","data_models"]:
    entity = data.get('entities',{}).get(entity_key, {})
    md += f"\n### {entity_key} ({entity.get('count',0)}) — {entity.get('description','')}\n"
    md += "| ID | Name | File | XXX | Created At |\n|----|------|------|-----|------------|\n"
    for item in entity.get('items',[])[:20]:
        md += f"| {item.get('id','')} | {item.get('name','')} | {item.get('file','')} | {item.get('xxx','')} | {item.get('created_at','')} |\n"
    if not entity.get('items'):
        md += "| - | - | - | - | - |\n"

md += "\n## Relationships\n| From | To | Type | Description |\n|------|----|------|-------------|\n"
for rel in data.get('relationships',[]):
    md += f"| {rel.get('from','')} | {rel.get('to','')} | {rel.get('type','')} | {rel.get('description','')} |\n"

out_path = root / "docs/dictionary/DICTIONARY.md"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(md, encoding="utf-8")
print(f"Generated {out_path}")

# Also in agent-repo-template
alt_path = root / "agent-repo-template/docs/dictionary/DICTIONARY.md"
if alt_path.parent.exists():
    alt_path.write_text(md, encoding="utf-8")
    print(f"Generated {alt_path}")
