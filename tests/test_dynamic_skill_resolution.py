#!/usr/bin/env python3
import json
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("resolver", ROOT / "scripts/dynamic-skill-resolver.py")
resolver = importlib.util.module_from_spec(spec)
spec.loader.exec_module(resolver)

CONTEXT = {
    "project_type": "WEB",
    "field": "Foundation",
    "phase": "005",
    "task": "allocation",
    "provider_runtime": "none",
    "tools_plugins": [],
    "project_guidance": "universal-toolkit",
    "permissions_policy": "explicit",
}


def test_agent_count_does_not_change_skill_set():
    outputs = [resolver.resolve({**CONTEXT, "agent_count": n}) for n in (2, 4, 8)]
    assert outputs[0]["skills"] == outputs[1]["skills"] == outputs[2]["skills"]
    assert outputs[0]["authorization"] == outputs[1]["authorization"] == outputs[2]["authorization"]
    assert outputs[0]["authority"] == outputs[1]["authority"] == outputs[2]["authority"]
    assert outputs[0]["allocation_profile"] != outputs[1]["allocation_profile"]
    assert outputs[1]["allocation_profile"] != outputs[2]["allocation_profile"]


def test_resolution_is_deterministic():
    a = resolver.resolve({**CONTEXT, "agent_count": 4})
    b = resolver.resolve({**CONTEXT, "agent_count": 4})
    assert a == b


def test_unknown_capacity_is_rejected():
    try:
        resolver.resolve({**CONTEXT, "agent_count": 3})
    except ValueError as exc:
        assert "agent_count" in str(exc)
    else:
        raise AssertionError("unsupported capacity must fail closed")
