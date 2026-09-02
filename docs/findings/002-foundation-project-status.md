# 002-foundation-project-status

**Field:** Foundation  
**Phase:** foundation  
**Target:** project-status  
**Impact:** BOUNDED  
**Status:** VALIDATED  
**Date:** 2026-09-01

## Goal
Create `scripts/status.py` — a fast project health / status command so any agent or human can instantly see the state of a project without opening many files.

## What it should report
- Project name
- Current XXX + Status + Field
- Active findings count (and warn if > 10)
- Whether a root appears to exist
- Last checkpoint / session
- Open investigations
- Quick census summary if available
- Overall health indicator
