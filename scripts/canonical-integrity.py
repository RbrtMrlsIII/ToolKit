#!/usr/bin/env python3
"""Fail-closed structural guard for canonical knowledge documents.

The guard protects canonical Markdown structure. It checks for removed headings
between a base and head revision, reports deletion-heavy diffs for review, and
can also inspect staged content during a local pre-commit hook.

Examples:
  python scripts/canonical-integrity.py --base origin/main --head HEAD
  python scripts/canonical-integrity.py --staged
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

CANONICAL_PATHS = {
    "README.md",
    "PRODUCT_LAW.md",
    "POLICY.md",
    "PRODUCT-KNOWLEDGE.md",
    "MASTERPLAN.md",
    "AI_ASSISTANT_READ_ME.md",
    "ENDORSEMENT.md",
    "docs/STRUCTURE.md",
    "docs/SKILL_SCOPE_INDEX.md",
    "skills/SKILLS_INDEX.md",
    "docs/TOOLKIT_ARCHITECTURE.md",
    "docs/CHANGE_CONTRACT.md",
    "docs/WEB_AI_SEAT_FOUNDATION.md",
    "docs/KNOWLEDGE_UPSTREAM_BOUNDARY.md",
    "docs/USER_MANUAL_DEPLOYMENT.md",
}

HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$")


def run_git(*args: str, check: bool = True) -> str:
    result = subprocess.run(["git", *args], check=False, text=True, capture_output=True)
    if check and result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "git command failed")
    return result.stdout


def headings(text: str) -> set[str]:
    return {
        match.group(1).strip()
        for line in text.splitlines()
        if (match := HEADING_RE.match(line))
    }


def diff_name_only(base: str, head: str) -> list[str]:
    return [p for p in run_git("diff", "--name-only", f"{base}...{head}").splitlines() if p]


def staged_name_only() -> list[str]:
    return [p for p in run_git("diff", "--cached", "--name-only").splitlines() if p]


def deletion_counts(base: str, head: str) -> dict[str, tuple[int, int]]:
    output = run_git("diff", "--numstat", f"{base}...{head}")
    return parse_numstat(output)


def staged_deletion_counts() -> dict[str, tuple[int, int]]:
    return parse_numstat(run_git("diff", "--cached", "--numstat"))


def parse_numstat(output: str) -> dict[str, tuple[int, int]]:
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
    return run_git("show", f"{ref}:{path}", check=False)


def staged_file(path: str) -> str:
    # Empty output is ambiguous for an empty file, but canonical Markdown files
    # are expected to be non-empty. Use the index as the staged source.
    return run_git("show", f":{path}", check=False)


def current_file(path: str) -> str:
    file_path = Path(path)
    return file_path.read_text(encoding="utf-8") if file_path.exists() else ""


def inspect(
    changed: list[str],
    counts: dict[str, tuple[int, int]],
    before_reader,
    after_reader,
    allow_removed: set[str],
    large_threshold: int,
) -> int:
    failures: list[str] = []
    warnings: list[str] = []

    for path in changed:
        if path not in CANONICAL_PATHS:
            continue

        before = headings(before_reader(path))
        after = headings(after_reader(path))
        removed = sorted(before - after - allow_removed)
        if removed:
            failures.append(
                f"{path}: removed canonical headings: {', '.join(removed)}"
            )

        added, deleted = counts.get(path, (0, 0))
        if deleted >= large_threshold:
            warnings.append(
                f"{path}: deletion-heavy canonical diff ({added}+/{deleted}-); inspect unrelated content"
            )

    if failures:
        print("CANONICAL-INTEGRITY: FAIL CLOSED")
        for item in failures:
            print(f"- {item}")
        for item in warnings:
            print(f"- WARNING: {item}")
        print("Review the change contract before proceeding.")
        return 1

    print("CANONICAL-INTEGRITY: PASS")
    for item in warnings:
        print(f"WARNING: {item}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--base", help="Base ref to compare")
    mode.add_argument("--staged", action="store_true", help="Compare HEAD to staged index")
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
        help="Deletion count that produces a review warning",
    )
    args = parser.parse_args()

    try:
        if args.staged:
            changed = staged_name_only()
            counts = staged_deletion_counts()
            return inspect(
                changed,
                counts,
                lambda path: file_at("HEAD", path),
                staged_file,
                set(args.allow_removed_heading),
                args.large_deletion_threshold,
            )

        base = args.base or "HEAD^"
        changed = diff_name_only(base, args.head)
        counts = deletion_counts(base, args.head)
        return inspect(
            changed,
            counts,
            lambda path: file_at(base, path),
            current_file,
            set(args.allow_removed_heading),
            args.large_deletion_threshold,
        )
    except RuntimeError as exc:
        print(f"CANONICAL-INTEGRITY: ERROR: {exc}")
        return 2


if __name__ == "__main__":
    sys.exit(main())
