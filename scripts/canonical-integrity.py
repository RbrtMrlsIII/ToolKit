#!/usr/bin/env python3
"""Fail-closed structural guard for canonical knowledge documents.

Canonical shape remains protected by default. Authorized MIGRATE/RETIRE records
may explain structural evolution while preserving evidence and lineage.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

CANONICAL_PATHS = {
    "PRODUCT_LAW.md", "POLICY.md", "PRODUCT-KNOWLEDGE.md", "MASTERPLAN.md",
    "AI_ASSISTANT_READ_ME.md", "ENDORSEMENT.md", "README.md",
    "docs/STRUCTURE.md", "docs/SKILL_SCOPE_INDEX.md", "skills/SKILLS_INDEX.md",
}
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$")


def git(*args: str) -> str:
    result = subprocess.run(["git", *args], check=False, text=True, capture_output=True)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "git command failed")
    return result.stdout


def headings(text: str) -> set[str]:
    return {m.group(1).strip() for line in text.splitlines() if (m := HEADING_RE.match(line))}


def changed_paths(base: str, head: str) -> list[str]:
    return [p for p in git("diff", "--name-only", f"{base}...{head}").splitlines() if p]


def deletion_counts(base: str, head: str) -> dict[str, tuple[int, int]]:
    counts: dict[str, tuple[int, int]] = {}
    for row in git("diff", "--numstat", f"{base}...{head}").splitlines():
        parts = row.split("\t", 2)
        if len(parts) == 3 and parts[0].isdigit() and parts[1].isdigit():
            counts[parts[2]] = (int(parts[0]), int(parts[1]))
    return counts


def file_at(ref: str, path: str) -> str:
    result = subprocess.run(["git", "show", f"{ref}:{path}"], check=False, text=True, capture_output=True)
    return result.stdout if result.returncode == 0 else ""


def current_file(path: str) -> str:
    return Path(path).read_text(encoding="utf-8") if Path(path).exists() else ""


def load_evolution(path: str) -> dict[str, dict]:
    record_path = Path(path)
    if not record_path.exists():
        return {}
    data = json.loads(record_path.read_text(encoding="utf-8"))
    changes = data.get("changes")
    if not isinstance(changes, list):
        raise ValueError("canonical evolution record requires changes list")
    result: dict[str, dict] = {}
    for item in changes:
        required = ("path", "mode", "removed_headings", "authority", "scope", "evidence")
        if any(not item.get(k) for k in required):
            raise ValueError("canonical evolution record has missing required field")
        if item["mode"] not in {"MIGRATE", "RETIRE"}:
            raise ValueError("canonical evolution mode must be MIGRATE or RETIRE")
        if item["mode"] == "MIGRATE" and not item.get("successor"):
            raise ValueError("MIGRATE requires successor")
        if item["mode"] == "RETIRE" and not item.get("retirement_reason"):
            raise ValueError("RETIRE requires retirement_reason")
        result[item["path"]] = item
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="HEAD^")
    parser.add_argument("--head", default="HEAD")
    parser.add_argument("--allow-removed-heading", action="append", default=[])
    parser.add_argument("--evolution-record", default="validation/canonical-evolution/007-record.json")
    parser.add_argument("--large-deletion-threshold", type=int, default=40)
    args = parser.parse_args()

    try:
        paths = changed_paths(args.base, args.head)
        nums = deletion_counts(args.base, args.head)
        evolution = load_evolution(args.evolution_record)
    except (RuntimeError, ValueError, json.JSONDecodeError) as exc:
        print(f"CANONICAL-INTEGRITY: ERROR: {exc}")
        return 2

    failures: list[str] = []
    warnings: list[str] = []
    explicit = set(args.allow_removed_heading)

    for path in paths:
        if path not in CANONICAL_PATHS and not path.startswith("docs/"):
            continue
        before = headings(file_at(args.base, path))
        after = headings(current_file(path))
        removed = sorted(before - after)
        authorized = evolution.get(path, {})
        authorized_headings = set(authorized.get("removed_headings", [])) | explicit
        unexplained = [heading for heading in removed if heading not in authorized_headings]
        if unexplained:
            failures.append(f"{path}: removed canonical headings without authorized evolution: {', '.join(unexplained)}")

        added, deleted = nums.get(path, (0, 0))
        if deleted >= args.large_deletion_threshold and path not in evolution:
            failures.append(f"{path}: {deleted} lines deleted; structural review/evolution record required")
        elif deleted > 0 and deleted > max(20, added * 2) and path not in evolution:
            warnings.append(f"{path}: deletion-heavy diff ({added}+/{deleted}-); inspect unrelated content")

    if failures:
        print("CANONICAL-INTEGRITY: FAIL CLOSED")
        for item in failures:
            print(f"- {item}")
        for item in warnings:
            print(f"- WARNING: {item}")
        print("Review docs/CHANGE_CONTRACT.md and canonical-evolution records before proceeding.")
        return 1

    print("CANONICAL-INTEGRITY: PASS")
    for item in warnings:
        print(f"WARNING: {item}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
