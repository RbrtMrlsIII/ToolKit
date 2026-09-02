#!/usr/bin/env python3
"""
new-project.py — Scaffold a new project from the Universal AGENT Toolkit

Usage:
    python scripts/new-project.py <project-name> [--with-integrations] [--with-tests]

Example:
    python scripts/new-project.py my-awesome-app
    python scripts/new-project.py my-app --with-integrations --with-tests
"""

import argparse
import os
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path


def get_timestamp():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def get_session_id():
    return datetime.now().strftime("%Y-%m-%d-%H%M%S")


def main():
    parser = argparse.ArgumentParser(
        description="Scaffold a new project from the Universal AGENT Toolkit"
    )
    parser.add_argument("name", help="Name of the new project (folder name)")
    parser.add_argument(
        "--with-integrations",
        action="store_true",
        help="Also copy backend-integrations-repo",
    )
    parser.add_argument(
        "--with-tests",
        action="store_true",
        help="Also copy test-files-repo",
    )
    parser.add_argument(
        "--target-dir",
        default=".",
        help="Directory in which to create the project (default: current directory)",
    )
    args = parser.parse_args()

    project_name = args.name.strip().replace(" ", "-").lower()
    if not project_name:
        print("Error: project name cannot be empty")
        sys.exit(1)

    # Locate the toolkit root (this script lives in toolkit/scripts/)
    script_path = Path(__file__).resolve()
    toolkit_root = script_path.parent.parent

    target_root = Path(args.target_dir).resolve() / project_name

    if target_root.exists():
        print(f"Error: target directory already exists → {target_root}")
        sys.exit(1)

    print(f"Scaffolding new project: {project_name}")
    print(f"Target: {target_root}")
    print()

    # 1. Copy core toolkit (exclude heavy optional modules by default)
    ignore = shutil.ignore_patterns(
        "__pycache__",
        "*.pyc",
        ".git",
        ".DS_Store",
        "backend-integrations-repo",
        "test-files-repo",
        "agent-toolkit-*.zip",
        "*.bak",
    )
    shutil.copytree(toolkit_root, target_root, ignore=ignore)

    # 2. Optionally bring integrations / tests
    if args.with_integrations:
        src = toolkit_root / "backend-integrations-repo"
        if src.exists():
            shutil.copytree(src, target_root / "backend-integrations-repo")
            print("✓ backend-integrations-repo included")

    if args.with_tests:
        src = toolkit_root / "test-files-repo"
        if src.exists():
            shutil.copytree(src, target_root / "test-files-repo")
            print("✓ test-files-repo included")

    # 3. Create empty src/ with README
    src_dir = target_root / "src"
    src_dir.mkdir(exist_ok=True)
    (src_dir / "README.md").write_text(
        f"""# src/ — Project-Development Layer

This is where the **product code** for **{project_name}** lives.

Rules (from POLICY.md):
- Only product code belongs here
- No findings, knowledge, session logs, or canonical rules
- No build outputs (those go in /builds)

Start building here.
"""
    )
    print("✓ src/ created")

    # 4. Update README.md with project name
    readme = target_root / "README.md"
    if readme.exists():
        content = readme.read_text()
        content = content.replace("Universal AGENT Toolkit", f"{project_name} (from AGENT Toolkit)")
        content = content.replace(
            "Current focus: Toolkit baseline (no product code yet)",
            f"Current focus: New project `{project_name}` — ready for roots-definer / phase-planner",
        )
        readme.write_text(content)
        print("✓ README.md updated")

    # 5. Initialize registry + state
    continuity = target_root / ".agent" / "continuity"
    continuity.mkdir(parents=True, exist_ok=True)

    ts = get_timestamp()
    registry = {
        "version": "1.0",
        "last_updated": ts,
        "current_xxx": "000-scaffold-initial",
        "todo": [],
        "completed": ["000-scaffold-initial"],
        "knowledge_index": [],
        "project_name": project_name,
    }
    import json
    (continuity / "registry.json").write_text(json.dumps(registry, indent=2))
    (continuity / "state.json").write_text(
        json.dumps(
            {
                "version": "1.0",
                "last_updated": ts,
                "last_good_state": "000-scaffold-initial",
                "active_findings": 0,
                "status": "ready",
                "project_name": project_name,
            },
            indent=2,
        )
    )
    print("✓ .agent/continuity initialized")

    # 6. Create first session log
    session_id = get_session_id()
    sessions_dir = target_root / ".agent" / "sessions"
    sessions_dir.mkdir(parents=True, exist_ok=True)
    docs_sessions = target_root / "docs" / "sessions"
    docs_sessions.mkdir(parents=True, exist_ok=True)

    session_data = {
        "session_id": f"{session_id}-scaffold",
        "start_timestamp": ts,
        "end_timestamp": ts,
        "agent_id": "new-project-scaffold",
        "previous_checkpoint": None,
        "current_xxx": "000-scaffold-initial",
        "actions": [
            {"timestamp": ts, "action": "Scaffold", "details": f"Created project {project_name}"}
        ],
        "files_changed": [],
        "complete_trace": f"Scaffolded new project {project_name} from AGENT Toolkit",
        "duration_seconds": 0,
    }
    (sessions_dir / f"session-{session_id}.json").write_text(json.dumps(session_data, indent=2))
    (docs_sessions / f"session-{session_id}.md").write_text(
        f"""# Session {session_id}-scaffold

**Project:** {project_name}  
**Start:** {ts}  
**Agent:** new-project-scaffold

## Actions
- Scaffolded new project from Universal AGENT Toolkit

## Next Steps
1. Open the project
2. Run `roots-definer` if this is a new product
3. Or start with `phase-planner` if roots already exist
"""
    )
    print("✓ First session log created")

    # 7. Create a simple initial finding
    findings = target_root / "docs" / "findings"
    findings.mkdir(parents=True, exist_ok=True)
    (findings / "000-scaffold-initial.md").write_text(
        f"""# 000-scaffold-initial

**Project:** {project_name}  
**Status:** ADVANCED  
**Date:** {ts[:10]}

## Summary
Project scaffolded from the Universal AGENT Toolkit.

## Next
- Decide whether to run `roots-definer` or go straight to `phase-planner`
"""
    )

    # 8. Final message
    print()
    print("=" * 60)
    print(f"✅ Project '{project_name}' created successfully!")
    print("=" * 60)
    print()
    print("Next steps:")
    print(f"  cd {target_root}")
    print("  # 1. Read the front-door")
    print("  cat README.md")
    print()
    print("  # 2. If this is a brand-new product:")
    print("  #    → use roots-definer skill")
    print("  # 3. If roots already exist:")
    print("  #    → use phase-planner skill")
    print()
    print("  # 4. Run census anytime:")
    print("  python scripts/census.py --base . --write")
    print()


if __name__ == "__main__":
    main()
