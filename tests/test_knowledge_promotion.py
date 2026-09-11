#!/usr/bin/env python3
"""Executable tests for Toolkit 006 knowledge-promotion boundaries."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts/knowledge-promotion-validator.py"
FIXTURE = ROOT / "validation/knowledge-promotion/006-teamai-canonical-integrity.json"


def run(record: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATOR), str(record)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def main() -> int:
    # Pending universal candidate must not become permanent without endorsement.
    result = run(FIXTURE)
    assert result.returncode != 0, "pending universal promotion unexpectedly passed"
    assert "requires endorsement" in result.stderr, result.stderr

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        data = json.loads(FIXTURE.read_text(encoding="utf-8"))

        # Consumer-specific dependency may not be promoted as universal.
        invalid = tmp_path / "invalid-consumer-dependency.json"
        invalid_data = {**data, "endorsement": "APPROVED", "consumer_dependency": "EXPLICIT"}
        invalid.write_text(json.dumps(invalid_data), encoding="utf-8")
        result = run(invalid)
        assert result.returncode != 0, "consumer-specific universal promotion unexpectedly passed"
        assert "consumer-specific dependency" in result.stderr, result.stderr

        # Fully validated and endorsed universal candidate passes.
        valid = tmp_path / "valid-universal.json"
        valid.write_text(json.dumps({**data, "endorsement": "APPROVED"}), encoding="utf-8")
        result = run(valid)
        assert result.returncode == 0, result.stderr
        assert "knowledge-promotion: PASS" in result.stdout, result.stdout

    print("knowledge-promotion tests: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
