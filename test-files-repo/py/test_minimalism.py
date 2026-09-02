#!/usr/bin/env python3
"""Minimalism: findings <=10, no forbidden"""
import pathlib, fnmatch
root = pathlib.Path.cwd()
findings = list((root / "docs/findings").glob("*.md")) if (root / "docs/findings").exists() else list((root / "agent-repo-template/docs/findings").glob("*.md"))
findings = [f for f in findings if "TEMPLATE" not in f.name.upper()]
print(f"Findings count: {len(findings)} / 10 max")
if len(findings) > 10:
    print("FAIL: Too many findings, need archive")
    exit(1)
forbidden = ["patch*", "final*.md", "fix*.md"]
bad = []
for p in root.rglob("*"):
    if p.is_file() and not p.name.lower().startswith("template-"):
        for pat in forbidden:
            if fnmatch.fnmatch(p.name.lower(), pat):
                bad.append(str(p))
                break
if bad:
    print(f"FAIL: Forbidden files: {bad[:5]}")
    exit(1)
print("PASS: Minimalism OK")
