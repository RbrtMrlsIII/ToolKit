#!/usr/bin/env python3
"""Test if findings were distilled to PRODUCT-KNOWLEDGE.md"""
import pathlib, re
root = pathlib.Path.cwd()
pk = root / "PRODUCT-KNOWLEDGE.md"
if not pk.exists():
    pk = root / "agent-repo-template/PRODUCT-KNOWLEDGE.md"
if not pk.exists():
    print("PRODUCT-KNOWLEDGE.md missing")
    exit(1)
text = pk.read_text(encoding="utf-8", errors="ignore")
findings_dir = root / "docs/findings"
if not findings_dir.exists():
    findings_dir = root / "agent-repo-template/docs/findings"
missing = []
for f in findings_dir.glob("*.md"):
    if "TEMPLATE" in f.name.upper():
        continue
    m = re.match(r"(\d{3})-", f.name)
    if m and m.group(1) != "000":
        if m.group(1) not in text:
            missing.append(f.name)
if missing:
    print(f"FAIL: Not distilled: {missing}")
    exit(1)
print("PASS: All findings distilled to PRODUCT-KNOWLEDGE.md")
