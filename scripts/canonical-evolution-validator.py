#!/usr/bin/env python3
"""Validate authorized canonical migration/retirement records."""
from __future__ import annotations
import argparse, json
from pathlib import Path

MODES = {"MIGRATE", "RETIRE"}

def validate(record: dict) -> None:
    changes = record.get("changes")
    if not isinstance(changes, list) or not changes:
        raise ValueError("changes must be a non-empty list")
    for item in changes:
        for key in ("path", "mode", "removed_headings", "authority", "scope", "evidence"):
            if not item.get(key):
                raise ValueError(f"missing required field: {key}")
        if item["mode"] not in MODES:
            raise ValueError(f"invalid mode: {item['mode']}")
        if not isinstance(item["removed_headings"], list) or not all(item["removed_headings"]):
            raise ValueError("removed_headings must be a non-empty list")
        if item["mode"] == "MIGRATE" and not item.get("successor"):
            raise ValueError("MIGRATE requires successor")
        if item["mode"] == "RETIRE" and not item.get("retirement_reason"):
            raise ValueError("RETIRE requires retirement_reason")

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("record", type=Path)
    args = parser.parse_args()
    validate(json.loads(args.record.read_text(encoding="utf-8")))
    print("canonical-evolution: PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
