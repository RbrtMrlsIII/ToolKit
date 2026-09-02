#!/usr/bin/env python3
"""Test registry.json valid and knowledge_index"""
import json, pathlib
root = pathlib.Path.cwd()
reg_path = root / ".agent/continuity/registry.json"
if not reg_path.exists():
    reg_path = root / "agent-repo-template/.agent/continuity/registry.json"
reg = json.loads(reg_path.read_text())
assert "current_xxx" in reg
assert "knowledge_index" in reg
print(f"PASS: Registry OK current_xxx={reg.get('current_xxx')}, knowledge rows={reg.get('knowledge_index',{}).get('total_rows')}")
