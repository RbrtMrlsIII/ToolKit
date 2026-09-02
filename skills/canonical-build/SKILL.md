# SKILL: Canonical Build — Where to Put Builds

> Universal skill — canonical building skill and where to put those builds. Applicable to all project types: web, mobile, backend, 3d, game, generic.

### Metadata
- ID: canonical-build
- Phase: Build (after Validate, before Advance)
- Type: core
- Applies To: All projects (web, mobile, backend, 3d)

### When To Use
- When project is buildable (has build script, needs conversion to 3D, needs packaging)
- After Validate PASS, before Advance
- When MASTERPLAN XXX is build-related

### Prerequisites
- Source files changed and validated
- POLICY.md section 9 (Canonical Build Locations)
- builds/ and .agent/builds/ folders exist

### Steps

1. **Determine Build Type from Project:**
   - web: `npm run build` or `yarn build` → output `dist/`, `build/`, `.next/`
   - mobile: `expo build` or `gradle build` → apk, ipa
   - backend: `docker build` or `npm run build:backend`
   - 3d: conversion `obj→glb`, `fbx→glb` via `scripts/convert-3d.py` or similar
   - generic: copy files to builds/

2. **Create Build Directory:**
   - `builds/XXX-phase-target/` — e.g., `builds/006-backend-auth-api/`
   - Inside: `web/`, `mobile/`, `backend/`, `3d/`, `artifacts/` subfolders per type
   - Example: `builds/006-backend-auth-api/web/` contains web build, `3d/` contains converted glb

3. **Run Build:**
   - Execute build command, capture logs
   - Place output in `builds/XXX-phase-target/<type>/`

4. **Create Build Log with Timestamp:**
   - `builds/XXX-phase-target/build-log-YYYY-MM-DD-HHMMSS.json` — machine:
     ```json
     {
       "xxx": "006",
       "phase": "backend",
       "target": "auth-api",
       "start_timestamp": "2026-09-01T10:40:00+08:00",
       "end_timestamp": "2026-09-01T10:41:00+08:00",
       "duration_seconds": 60,
       "agent_id": "AgentMobile1",
       "status": "PASS",
       "artifacts": ["builds/006-backend-auth-api/backend/auth.js"],
       "build_type": "backend"
     }
     ```
   - `builds/XXX-phase-target/build-log-YYYY-MM-DD-HHMMSS.md` — human readable

5. **Update Latest:**
   - Copy or symlink `builds/XXX-phase-target/` → `builds/latest/` (latest successful build)
   - `builds/latest/` must always point to latest PASS build

6. **Machine-Readable Build State:**
   - `.agent/builds/builds.json`:
     ```json
     {
       "current_build": "006-backend-auth-api",
       "latest_xxx": "006",
       "latest_timestamp": "2026-09-01T10:41:00+08:00",
       "builds": [
         {"xxx": "006", "phase": "backend", "target": "auth-api", "timestamp": "2026-09-01T10:41:00+08:00", "status": "PASS", "artifacts": [...]}
       ]
     }
     ```
   - `.agent/builds/build-XXX.json` — per XXX build state

7. **Build Evidence:**
   - `validation/build-evidence/XXX-build-evidence.md` — did build pass tests, inventory check, artifacts exist

8. **Archive After 2 Checkpoints:**
   - After 2 checkpoints, compress `builds/XXX/` → `builds/archive/ARCHIVE-XXX-YYYY-MM-DD.tar.gz`
   - Update `.agent/builds/builds.json` archive entry

9. **Census Counts Builds:**
   - Census inventory now includes builds count, latest build XXX, build status

### Output Template

```
builds/
  latest/ → symlink to 006-backend-auth-api/
  006-backend-auth-api/
    web/
    backend/
    3d/
    artifacts/
    build-log-2026-09-01-104100.json
    build-log-2026-09-01-104100.md
  archive/
    ARCHIVE-005-2026-08-30.tar.gz

.agent/builds/
  builds.json
  build-006.json

validation/build-evidence/
  006-build-evidence.md
```

### Validation Checklist
- [ ] Build directory `builds/XXX-phase-target/` created, not in src/ or docs/
- [ ] Build output placed in correct subfolder per type (web/mobile/backend/3d)
- [ ] Build log JSON + MD with start/end timestamp, duration, agent_id, status
- [ ] `builds/latest/` updated to latest PASS build
- [ ] `.agent/builds/builds.json` updated with current_build, latest_xxx, timestamp
- [ ] `.agent/builds/build-XXX.json` created
- [ ] Build evidence file created
- [ ] Census counts builds
- [ ] No builds in src/, docs/ — only builds/ and .agent/builds/

### Anti-Patterns
- Putting builds in src/ or docs/ — violates POLICY
- No build log with timestamp — build invalid
- Not updating builds/latest/ — latest not tracked
- Forgetting .agent/builds/builds.json — machine state lost

### Distillation
Validated Pattern: "Canonical builds/XXX + builds/latest + .agent/builds/builds.json with timestamp ensures traceability"
