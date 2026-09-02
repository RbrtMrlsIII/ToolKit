#!/usr/bin/env python3
"""
Fast census test — universal, applicable to all project types
Counts tabs, UI, 3D, plus cleanliness
"""
import pathlib, sys, json
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent / "agent-repo-template" / "scripts"))
# Try import census
try:
    import subprocess
    base = pathlib.Path.cwd()
    # Look for census.py in multiple locations
    candidates = [base / "scripts/census.py", base / ".agent/census/census.py", base / "agent-repo-template/scripts/census.py"]
    census_path = next((c for c in candidates if c.exists()), None)
    if not census_path:
        print("census.py not found, using inventory only")
        # simple inventory
        tabs = list(base.rglob("*tabs*"))
        ui = list((base / "src").rglob("*")) if (base / "src").exists() else []
        print(f"Tabs files: {len(tabs)}, UI files: {len(ui)}")
    else:
        result = subprocess.run([sys.executable, str(census_path), "--base", str(base), "--write"], capture_output=True, text=True)
        print(result.stdout)
        if result.returncode != 0:
            print("CENSUS FAIL")
            sys.exit(1)
        print("CENSUS PASS - Fast test OK")
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
