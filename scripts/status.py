#!/usr/bin/env python3
"""
status.py — Project Health & Status Command

Usage:
    python scripts/status.py
    python scripts/status.py --base /path/to/project
"""

import argparse
import json
import re
from pathlib import Path
from datetime import datetime


def read_json(path: Path):
    try:
        return json.loads(path.read_text())
    except Exception:
        return None


def count_findings(findings_dir: Path) -> int:
    if not findings_dir.exists():
        return 0
    return len([f for f in findings_dir.glob("*.md") if f.name != "TEMPLATE-XXX-findings.md"])


def has_root_indicators(base: Path) -> str:
    """Heuristic check whether a root definition seems to exist."""
    indicators = []
    contracts = base / "docs" / "contracts"
    if contracts.exists() and any(contracts.iterdir()):
        indicators.append("contracts/")
    pk = base / "PRODUCT-KNOWLEDGE.md"
    if pk.exists():
        text = pk.read_text()
        if "Core Problem" in text or "Validated Patterns" in text:
            indicators.append("PRODUCT-KNOWLEDGE")
    arch = base / "docs" / "architecture-map.md"
    if arch.exists() and arch.stat().st_size > 100:
        indicators.append("architecture-map")
    findings = base / "docs" / "findings"
    if findings.exists():
        for f in findings.glob("*root*"):
            indicators.append(f.name)
            break
        for f in findings.glob("*foundation*"):
            indicators.append(f.name)
            break
    if indicators:
        return "Yes (" + ", ".join(indicators[:3]) + ")"
    return "No clear root found"


def get_masterplan_focus(base: Path) -> dict:
    mp = base / "MASTERPLAN.md"
    if not mp.exists():
        return {}
    text = mp.read_text()
    result = {}
    # Simple extraction from Current Focus table
    for line in text.splitlines():
        if "**Current XXX**" in line:
            result["current_xxx"] = line.split("|")[-2].strip() if "|" in line else ""
        if "**Status**" in line and "current_xxx" in result:
            result["status"] = line.split("|")[-2].strip() if "|" in line else ""
        if "**Current Field**" in line:
            result["field"] = line.split("|")[-2].strip() if "|" in line else ""
        if "**Open Investigations**" in line:
            result["investigations"] = line.split("|")[-2].strip() if "|" in line else ""
        if "**Last Checkpoint**" in line:
            result["checkpoint"] = line.split("|")[-2].strip() if "|" in line else ""
        if "**Active Findings**" in line:
            result["active_findings_note"] = line.split("|")[-2].strip() if "|" in line else ""
    return result


def get_latest_session(base: Path) -> str:
    sessions = base / ".agent" / "sessions"
    if not sessions.exists():
        return "None"
    files = sorted(sessions.glob("session-*.json"), reverse=True)
    if not files:
        return "None"
    data = read_json(files[0])
    if data:
        return f"{files[0].name} ({data.get('agent_id', '?')})"
    return files[0].name


def get_census_summary(base: Path) -> str:
    census_dir = base / "docs" / "census"
    if not census_dir.exists():
        return "No census run yet"
    reports = sorted(census_dir.glob("census-report-*.md"), reverse=True)
    if not reports:
        return "No census report found"
    # Just show the latest filename
    return f"Latest: {reports[0].name}"


def health_score(findings_count: int, has_root: bool, has_registry: bool) -> str:
    score = 100
    issues = []
    if findings_count > 10:
        score -= 30
        issues.append("too many findings")
    elif findings_count > 7:
        score -= 10
        issues.append("findings getting high")
    if not has_root:
        score -= 15
        issues.append("no clear root")
    if not has_registry:
        score -= 25
        issues.append("missing registry")
    if score >= 85:
        return f"🟢 Healthy ({score}/100)"
    if score >= 60:
        return f"🟡 Needs attention ({score}/100) — {', '.join(issues)}"
    return f"🔴 Unhealthy ({score}/100) — {', '.join(issues)}"


def main():
    parser = argparse.ArgumentParser(description="Show project health and status")
    parser.add_argument("--base", default=".", help="Project root (default: current directory)")
    args = parser.parse_args()
    base = Path(args.base).resolve()

    if not (base / "POLICY.md").exists() and not (base / "MASTERPLAN.md").exists():
        print(f"Does not look like an AGENT Toolkit project: {base}")
        return

    print("=" * 64)
    print("  PROJECT STATUS")
    print("=" * 64)

    # Project name
    registry = read_json(base / ".agent" / "continuity" / "registry.json")
    project_name = "Unknown"
    if registry and "project_name" in registry:
        project_name = registry["project_name"]
    else:
        project_name = base.name
    print(f"  Project        : {project_name}")
    print(f"  Path           : {base}")
    print()

    # Current focus from MASTERPLAN
    focus = get_masterplan_focus(base)
    print("  CURRENT FOCUS")
    print(f"  XXX            : {focus.get('current_xxx', '—')}")
    print(f"  Status         : {focus.get('status', '—')}")
    print(f"  Field          : {focus.get('field', '—')}")
    print(f"  Investigations : {focus.get('investigations', 'none')}")
    print(f"  Last Checkpoint: {focus.get('checkpoint', '—')}")
    print()

    # Findings
    findings_count = count_findings(base / "docs" / "findings")
    print("  WORKING MEMORY")
    print(f"  Active findings: {findings_count}  {'⚠️  (max 10)' if findings_count > 10 else ''}")
    print()

    # Root
    root_status = has_root_indicators(base)
    print("  ROOTS")
    print(f"  Root defined   : {root_status}")
    print()

    # Continuity
    has_registry = (base / ".agent" / "continuity" / "registry.json").exists()
    print("  CONTINUITY")
    print(f"  Registry       : {'✓' if has_registry else '✗ missing'}")
    print(f"  Latest session : {get_latest_session(base)}")
    print()

    # Census
    print("  CENSUS")
    print(f"  {get_census_summary(base)}")
    print()

    # Health
    print("  HEALTH")
    print(f"  {health_score(findings_count, 'Yes' in root_status, has_registry)}")
    print("=" * 64)
    print()
    print("Tips:")
    print("  python scripts/census.py --base . --write   # refresh inventory")
    print("  cat MASTERPLAN.md                           # full plan")
    print("  cat docs/STRUCTURE.md                       # full wiring")
    print("  cat docs/templates/ROOTS-DEFINITION.md      # roots template")
    print()


if __name__ == "__main__":
    main()
