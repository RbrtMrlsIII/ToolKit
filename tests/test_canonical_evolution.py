import importlib.util
import json
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("canonical_evolution", ROOT / "scripts/canonical-evolution-validator.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_migrate_requires_successor():
    record = {"changes": [{"path": "MASTERPLAN.md", "mode": "MIGRATE", "removed_headings": ["Old"], "authority": "approved", "scope": "section", "evidence": "evidence.md"}]}
    try:
        module.validate(record)
    except ValueError as exc:
        assert "successor" in str(exc)
    else:
        raise AssertionError("missing successor must fail")


def test_retire_requires_reason():
    record = {"changes": [{"path": "MASTERPLAN.md", "mode": "RETIRE", "removed_headings": ["Old"], "authority": "approved", "scope": "section", "evidence": "evidence.md"}]}
    try:
        module.validate(record)
    except ValueError as exc:
        assert "retirement_reason" in str(exc)
    else:
        raise AssertionError("missing retirement reason must fail")


def test_authorized_migration_passes():
    record = {"changes": [{"path": "MASTERPLAN.md", "mode": "MIGRATE", "removed_headings": ["Old"], "authority": "PRODUCT_LAW approved", "scope": "replace old section", "evidence": "validation/evidence/007.md", "successor": "PRODUCT-KNOWLEDGE.md §1"}]}
    module.validate(record)


def test_unknown_mode_fails():
    record = {"changes": [{"path": "MASTERPLAN.md", "mode": "DELETE", "removed_headings": ["Old"], "authority": "approved", "scope": "section", "evidence": "evidence.md"}]}
    try:
        module.validate(record)
    except ValueError as exc:
        assert "MIGRATE or RETIRE" in str(exc)
    else:
        raise AssertionError("unknown mode must fail")


if __name__ == "__main__":
    test_migrate_requires_successor()
    test_retire_requires_reason()
    test_authorized_migration_passes()
    test_unknown_mode_fails()
    print("canonical-evolution: PASS")
