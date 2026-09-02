#!/usr/bin/env python3
"""
new-xxx.py — Template Generator CLI
Part of bright improvement #6
Creates new XXX finding, handover, checkpoint from templates with correct naming
Usage:
  python scripts/new-xxx.py --phase backend --target auth-api
  python scripts/new-xxx.py --phase frontend --target checkout-ui --impact BOUNDED
"""
import pathlib, argparse, datetime, json, os

def get_next_xxx(root):
    reg_path = root / ".agent/continuity/registry.json"
    if not reg_path.exists():
        reg_path = root / "agent-repo-template/.agent/continuity/registry.json"
    if reg_path.exists():
        try:
            reg = json.loads(reg_path.read_text(encoding="utf-8"))
            current = reg.get("current_xxx", "000")
            # Next is current + 1 if current is TODO? For simplicity, increment
            nxt = int(current) + 1
            return f"{nxt:03d}"
        except:
            pass
    # Fallback: count existing findings
    findings_dir = root / "docs/findings"
    if not findings_dir.exists():
        findings_dir = root / "agent-repo-template/docs/findings"
    max_xxx = 0
    if findings_dir.exists():
        for f in findings_dir.glob("*.md"):
            try:
                num = int(f.name.split("-")[0])
                if num > max_xxx:
                    max_xxx = num
            except: pass
    return f"{max_xxx+1:03d}"

def main():
    parser = argparse.ArgumentParser(description="Generate new XXX templates")
    parser.add_argument("--phase", required=True, help="Phase: scaffold, backend, frontend, contract, knowledge, etc.")
    parser.add_argument("--target", required=True, help="Target: auth-api, checkout-ui, etc.")
    parser.add_argument("--impact", default="BOUNDED", help="LOCAL|BOUNDED|SYSTEMIC")
    parser.add_argument("--base", default=".", help="Repo base")
    args = parser.parse_args()

    root = pathlib.Path(args.base).resolve()
    xxx = get_next_xxx(root)
    filename_base = f"{xxx}-{args.phase}-{args.target}"

    # Create finding from template
    template_path = root / "docs/findings/TEMPLATE-XXX-findings.md"
    if not template_path.exists():
        template_path = root / "agent-repo-template/docs/findings/TEMPLATE-XXX-findings.md"
    
    findings_dir = root / "docs/findings"
    findings_dir.mkdir(parents=True, exist_ok=True)
    
    if template_path.exists():
        content = template_path.read_text(encoding="utf-8")
        content = content.replace("XXX", xxx).replace("phase-target", f"{args.phase}-{args.target}")
        content += f"\n\n### Auto-generated\n- Phase: {args.phase}\n- Target: {args.target}\n- Impact: {args.impact}\n- Date: {datetime.datetime.now()}\n"
        (findings_dir / f"{filename_base}.md").write_text(content, encoding="utf-8")
        print(f"Created: docs/findings/{filename_base}.md")
    else:
        # Minimal
        (findings_dir / f"{filename_base}.md").write_text(f"# Findings: {filename_base}\nPhase: {args.phase}\nTarget: {args.target}\nImpact: {args.impact}\n", encoding="utf-8")
        print(f"Created minimal: docs/findings/{filename_base}.md")

    # Create evidence file
    evidence_dir = root / "validation/evidence"
    evidence_dir.mkdir(parents=True, exist_ok=True)
    (evidence_dir / f"{filename_base}.md").write_text(f"# Validation Evidence: {filename_base}\n\nSource Validation: TODO\nConsumer Validation: TODO\n", encoding="utf-8")
    print(f"Created: validation/evidence/{filename_base}.md")

    # Create handover file
    handover_dir = root / "docs/handover"
    handover_dir.mkdir(parents=True, exist_ok=True)
    (handover_dir / f"{filename_base}-handover.md").write_text(f"# Handover: {filename_base}\nNext: {int(xxx)+1:03d}\n", encoding="utf-8")
    print(f"Created: docs/handover/{filename_base}-handover.md")

    # Update registry.json todo
    reg_path = root / ".agent/continuity/registry.json"
    if reg_path.exists():
        try:
            reg = json.loads(reg_path.read_text())
            if "registry" in reg and "todo" in reg["registry"]:
                if filename_base not in reg["registry"]["todo"]:
                    reg["registry"]["todo"].append(filename_base)
            reg["current_xxx"] = xxx
            reg_path.write_text(json.dumps(reg, indent=2), encoding="utf-8")
            print(f"Updated registry.json current_xxx={xxx}")
        except Exception as e:
            print(f"Registry update failed: {e}")

    print(f"\nNext: Read PRODUCT-KNOWLEDGE.md Anti-Patterns, then execute {args.phase} phase for {filename_base}")

if __name__ == "__main__":
    main()
