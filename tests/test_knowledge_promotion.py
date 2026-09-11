#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts/knowledge-promotion-validator.py"
FIXTURE = ROOT / "validation/knowledge-promotion/006-teamai-canonical-integrity.json"


def run(path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def test_pending_universal_candidate_is_blocked_until_endorsement() -> None:
    result = run(FIXTURE)
    assert result.returncode != 0
    assert "requires endorsement" in result.stderr


def test_consumer_specific_dependency_cannot_be_universal() -> None:
    data = json.loads(FIXTURE.read_text(encoding="utf-8"))
    data["endorsement"] = "APPROVED"
    data["consumer_dependency"] = "EXPLICIT"
    temp = ROOT / "validation/knowledge-promotion/006-invalid-consumer-dependency.json"
    temp.write_text(json.dumps(data), encoding="utf-8")
    try:
        result = run(temp)
        assert result.returncode != 0
        assert "consumer-specific dependency" in result.stderr
    finally:
        temp.unlink()


def test_endorsed_universal_candidate_passes() -> None:
    data = json.loads(FIXTURE.read_text(encoding="utf-8"))
    data["endorsement"] = "APPROVED"
    temp = ROOT / "validation/knowledge-promotion/006-valid-universal.json"
    temp.write_text(json.dumps(data), encoding="utf-8")
    try:
        result = run(temp)
        assert result.returncode == 0
        assert "knowledge-promotion: PASS" in result.stdout
    finally:
        temp.unlink()
