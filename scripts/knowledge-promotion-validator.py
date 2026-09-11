#!/usr/bin/env python3
"""Fail-closed validation for Toolkit 006 knowledge-promotion records."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ALLOWED = {"UNIVERSAL", "ADAPTABLE", "CONSUMER-SPECIFIC", "EPHEMERAL"}


def validate(path: Path) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    required = [
        "source_project", "source_finding", "source_evidence",
        "classification", "proposed_claim", "validation",
        "endorsement", "promotion_target",
    ]
    missing = [k for k in required if not data.get(k)]
    if missing:
        raise ValueError(f"missing required fields: {', '.join(missing)}")
    classification = data["classification"]
    if classification not in ALLOWED:
        raise ValueError(f"invalid classification: {classification}")
    if data["validation"] != "PASS":
        raise ValueError("promotion requires validation=PASS")
    if classification in {"UNIVERSAL", "ADAPTABLE"}:
        if data.get("consumer_dependency") not in (None, "NONE"):
            raise ValueError("universal/adaptable promotion cannot carry consumer-specific dependency")
        if data.get("endorsement") != "APPROVED":
            raise ValueError("universal/adaptable promotion requires endorsement=APPROVED")
    if not str(data["source_evidence"]).strip():
        raise ValueError("source_evidence is required")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("record", type=Path)
    args = parser.parse_args()
    validate(args.record)
    print("knowledge-promotion: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
