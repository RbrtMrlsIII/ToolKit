#!/usr/bin/env python3
"""Deterministic, auditable smallest-sufficient skill resolver for Toolkit 005."""
from __future__ import annotations
import argparse, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "skills/foundation/dynamic-skill-resolution/catalog.json"


def norm(values):
    return {str(v).strip().lower() for v in values if str(v).strip()}


def resolve(context: dict) -> dict:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    project_type = str(context.get("project_type", "GENERIC")).upper()
    field = str(context.get("field", "Foundation")).lower()
    task = norm(context.get("tasks", []))
    if not task:
        task = norm([context.get("task", "")])

    selected = []
    for skill in catalog["skills"]:
        types = norm(skill["project_types"])
        fields = norm(skill["fields"])
        tasks = norm(skill["tasks"])
        type_ok = "all" in types or project_type.lower() in types
        field_ok = "all" in fields or field in fields
        task_ok = not task or bool(task & tasks)
        if type_ok and field_ok and task_ok:
            selected.append(skill["id"])

    capacity = int(context.get("agent_count", 2))
    if capacity not in (2, 4, 8):
        raise ValueError("agent_count must be one of 2, 4, or 8 for the validated baseline")

    return {
        "schema": "toolkit.skill-resolution.v1",
        "inputs": context,
        "skills": sorted(set(selected)),
        "allocation_profile": catalog["allocation_profiles"][str(capacity)],
        "authorization": "unchanged-by-resolution",
        "authority": "Product Law / policy / permissions / consuming-project authority",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("context_json")
    args = parser.parse_args()
    context = json.loads(args.context_json)
    print(json.dumps(resolve(context), indent=2, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
