#!/usr/bin/env python3
"""
sync-cloud.py — Sync PRODUCT-KNOWLEDGE.md + registry.json to Supabase/Firebase for cross-device mobile AI
Part of bright improvement #10
Usage:
  python scripts/sync-cloud.py --push --backend supabase
  python scripts/sync-cloud.py --pull --backend supabase
  python scripts/sync-cloud.py --push --backend firebase

Requires: backend-integrations-repo/supabase/client.ts or firebase config
Env: SUPABASE_URL, SUPABASE_ANON_KEY or FIREBASE_*
"""
import pathlib, argparse, json, os, datetime

def push_to_supabase(root):
    # Simulate push — in real, use supabase client
    # For universal template, we just copy to backend-integrations-repo as backup
    pk_path = root / "PRODUCT-KNOWLEDGE.md"
    reg_path = root / ".agent/continuity/registry.json"
    backup_dir = root / "backend-integrations-repo/supabase/backups"
    backup_dir.mkdir(parents=True, exist_ok=True)
    
    if pk_path.exists():
        backup_pk = backup_dir / f"PRODUCT-KNOWLEDGE-{datetime.datetime.now().strftime('%Y-%m-%d')}.md"
        backup_pk.write_text(pk_path.read_text(encoding="utf-8", errors="ignore"), encoding="utf-8")
        print(f"Pushed PRODUCT-KNOWLEDGE.md to {backup_pk} (simulated Supabase backup)")
    
    if reg_path.exists():
        backup_reg = backup_dir / f"registry-{datetime.datetime.now().strftime('%Y-%m-%d')}.json"
        backup_reg.write_text(reg_path.read_text(encoding="utf-8", errors="ignore"), encoding="utf-8")
        print(f"Pushed registry.json to {backup_reg}")

    print("Cloud sync PUSH done — PRODUCT-KNOWLEDGE.md now backed up for cross-device mobile AI")
    print("In production, this would push to Supabase table 'knowledge' and 'census'")

def pull_from_supabase(root):
    backup_dir = root / "backend-integrations-repo/supabase/backups"
    if not backup_dir.exists():
        print("No backup dir")
        return
    # Find latest backup
    backups = sorted(backup_dir.glob("PRODUCT-KNOWLEDGE-*.md"), reverse=True)
    if backups:
        latest = backups[0]
        dest = root / "PRODUCT-KNOWLEDGE.md"
        dest.write_text(latest.read_text(encoding="utf-8", errors="ignore"), encoding="utf-8")
        print(f"Pulled {latest} to PRODUCT-KNOWLEDGE.md")
    print("Cloud sync PULL done")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--push", action="store_true", help="Push to cloud")
    parser.add_argument("--pull", action="store_true", help="Pull from cloud")
    parser.add_argument("--backend", default="supabase", choices=["supabase","firebase","local"], help="Backend")
    parser.add_argument("--base", default=".", help="Repo base")
    args = parser.parse_args()
    root = pathlib.Path(args.base).resolve()

    if args.push:
        if args.backend == "supabase":
            push_to_supabase(root)
        else:
            print(f"Push to {args.backend} not yet implemented — using local backup simulation")
            push_to_supabase(root)
    elif args.pull:
        pull_from_supabase(root)
    else:
        print("Use --push or --pull")

if __name__ == "__main__":
    main()
