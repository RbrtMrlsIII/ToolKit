#!/usr/bin/env python3
"""Fail-closed structural guard for canonical knowledge documents.

Usage:
  python scripts/canonical-integrity.py --base origin/main --head HEAD

The guard is intentionally conservative. Canonical headings removed by a change
are treated as failures unless the removed heading is explicitly listed with
--allow-removed-heading. Large canonical deletions are also reported for review.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

CANONICAL_PATHS = {
    "PRODUCT_LAW.md",
    "POLICY.md",
    "PRODUCT-KNOWLEDGE.md",
    "MASTERPLAN.md",
    "AI_ASSISTANT_READ_ME.md",
    "ENDORSEMENT.md",
    "README.md",
    "docs/STRUCTURE.md",
    "docs/SKILL_SCOPE_INDEX.md",
    "skills/SKILLS_INDEX.md",
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
    output = git("diff", "--name-only", f"{base}...{head}")
    return [p for p in output.splitlines() if p]


def deletion_counts(base: str, head: str) -> dict[str, tuple[int, int]]:
    output = git("diff", "--numstat", f"{base}...{head}")
    counts: dict[str, tuple[int, int]] = {}
    for row in output.splitlines():
        parts = row.split("\t", 2)
        if len(parts) != 3:
            continue
        added, deleted, path = parts
        if added.isdigit() and deleted.isdigit():
            counts[path] = (int(added), int(deleted))
    return counts


def file_at(ref: str, path: str) -> str:
    result = subprocess.run(["git", "show", f"{ref}:{path}"], check=False, text=True, capture_output=True)
    if result.returncode != 0:
        return ""
    return result.stdout


def current_file(path: str) -> str:
    return Path(path).read_text(encoding="utf-8") if Path(path).exists() else ""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="HEAD^", help="Base ref to compare")
    parser.add_argument("--head", default="HEAD", help="Head ref to compare")
    parser.add_argument(
        "--allow-removed-heading",
        action="append",
        default=[],
        help="Explicit canonical heading that may be removed; repeatable",
    )
    parser.add_argument(
        "--large-deletion-threshold",
        type=int,
        default=40,
        help="Deleted lines in one canonical file that trigger a blocking warning",
    )
    args = parser.parse_args()

    try:
        paths = changed_paths(args.base, args.head)
        nums = deletion_counts(args.base, args.head)
    except RuntimeError as exc:
        print(f"CANONICAL-INTEGRITY: ERROR: {exc}")
        return 2

    failures: list[str] = []
    warnings: list[str] = []

    for path in paths:
        if path not in CANONICAL_PATHS and not path.startswith("docs/"):
            continue

        before = headings(file_at(args.base, path))
        after = headings(current_file(path))
        removed = sorted(before - after - set(args.allow_removed_heading))
        if removed:
            failures.append(f"{path}: removed canonical headings: {', '.join(removed)}")

        added, deleted = nums.get(path, (0, 0))
        if deleted >= args.large_deletion_threshold:
            failures.append(
                f"{path}: {deleted} lines deleted in canonical/knowledge file; structural review required"
            )

        if deleted > 0 and deleted > max(20, added * 2) and not removed:
            warnings.append(
                f"{path}: deletion-heavy diff ({added}+/{deleted}-); inspect unrelated content"
            )

    if failures:
        print("CANONICAL-INTEGRITY: FAIL CLOSED")
        for item in failures:
            print(f"- {item}")
        for item in warnings:
            print(f"- WARNING: {item}")
        print("Review docs/CHANGE_CONTRACT.md before proceeding.")
        return 1

    print("CANONICAL-INTEGRITY: PASS")
    for item in warnings:
        print(f"WARNING: {item}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
