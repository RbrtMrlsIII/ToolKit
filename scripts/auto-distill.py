#!/usr/bin/env python3
"""
auto-distill.py — Auto-distill archived findings without PRODUCT-KNOWLEDGE row
Part of bright improvement #2
"""
import pathlib, re, json, datetime
root = pathlib.Path(".").resolve()
pk_path = root / "PRODUCT-KNOWLEDGE.md"
if not pk_path.exists():
    pk_path = root / "agent-repo-template/PRODUCT-KNOWLEDGE.md"
if not pk_path.exists():
    print("No PRODUCT-KNOWLEDGE.md")
    exit(0)

pk_text = pk_path.read_text(encoding="utf-8", errors="ignore")
findings_dir = root / "docs/findings"
archive_dir = root / "docs/archive"
if not findings_dir.exists():
    findings_dir = root / "agent-repo-template/docs/findings"

auto_added = 0
for f in list(findings_dir.glob("*.md")) + list((archive_dir if archive_dir.exists() else findings_dir).glob("*.md")):
    if "TEMPLATE" in f.name.upper():
        continue
    m = re.match(r"(\d{3})-", f.name)
    if not m or m.group(1)=="000":
        continue
    xxx = m.group(1)
    if xxx not in pk_text:
        # Auto-add minimal row to PRODUCT-KNOWLEDGE.md Minimalism Log
        log_entry = f"| {datetime.datetime.now().strftime('%Y-%m-%d')} | {f.name} | Auto-distilled by bot | {f} | {xxx} |"
        print(f"Auto-distilling {f.name} XXX {xxx}")
        # Append to Minimalism Log section
        if "## 5. Minimalism Log" in pk_text or "Minimalism Log" in pk_text:
            # Simple append
            with open(pk_path, "a", encoding="utf-8") as out:
                out.write(f"\n{log_entry}\n")
            auto_added += 1

print(f"Auto-distilled {auto_added} findings")
