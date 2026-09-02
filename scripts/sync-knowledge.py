#!/usr/bin/env python3
"""
sync-knowledge.py — Copy relevant Validated Patterns / Anti-Patterns from old project to new
Part of bright improvement #4
Usage:
  python scripts/sync-knowledge.py --from ../old-project --to ./
  python scripts/sync-knowledge.py --from ../old-project --to ./ --all
"""
import pathlib, argparse, re

def extract_sections(pk_text):
    # Extract Validated Patterns and Anti-Patterns tables
    validated = re.findall(r"## 1\. Validated Patterns.*?\n(\|.*\n)+", pk_text, re.DOTALL)
    anti = re.findall(r"## 2\. Anti-Patterns.*?\n(\|.*\n)+", pk_text, re.DOTALL)
    return pk_text  # for simplicity, return full but we will copy rows

def sync_knowledge(from_path, to_path, copy_all=False):
    from_pk = pathlib.Path(from_path) / "PRODUCT-KNOWLEDGE.md"
    if not from_pk.exists():
        from_pk = pathlib.Path(from_path) / "agent-repo-template/PRODUCT-KNOWLEDGE.md"
    to_pk = pathlib.Path(to_path) / "PRODUCT-KNOWLEDGE.md"
    if not to_pk.exists():
        to_pk = pathlib.Path(to_path) / "agent-repo-template/PRODUCT-KNOWLEDGE.md"

    if not from_pk.exists():
        print(f"From PRODUCT-KNOWLEDGE.md not found: {from_pk}")
        return
    if not to_pk.exists():
        print(f"To PRODUCT-KNOWLEDGE.md not found: {to_pk}")
        return

    from_text = from_pk.read_text(encoding="utf-8", errors="ignore")
    to_text = to_pk.read_text(encoding="utf-8", errors="ignore")

    # Extract rows from from_text that are not in to_text
    from_lines = [l for l in from_text.splitlines() if l.startswith("|") and "XXX" not in l and "Pattern" not in l and "---" not in l]
    to_lines_set = set(to_text.splitlines())

    new_rows = [l for l in from_lines if l not in to_lines_set]

    if not new_rows:
        print("No new knowledge rows to sync — already synced")
        return

    # Append to to_pk in appropriate sections — simple append to end with marker
    with open(to_pk, "a", encoding="utf-8") as f:
        f.write("\n\n## Synced from {} (Cross-Project Sync)\n".format(from_path))
        f.write("\n".join(new_rows[:50]))  # limit 50
        f.write("\n")

    print(f"Synced {len(new_rows[:50])} knowledge rows from {from_path} to {to_path}")
    print("Rows: Validated Patterns + Anti-Patterns that prevent repeat errors in new project")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--from", dest="from_path", required=True, help="Old project path")
    parser.add_argument("--to", dest="to_path", required=True, help="New project path")
    parser.add_argument("--all", action="store_true", help="Copy all rows")
    args = parser.parse_args()
    sync_knowledge(args.from_path, args.to_path, args.all)
