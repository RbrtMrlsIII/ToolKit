---
name: phase-planner
description: Propose an execution phase first, wait for user approval, then plant (new) or branch (continuation) it onto MASTERPLAN.md. Use when starting any non-trivial task, when the user gives a new goal, before creating a new XXX, or when the user mentions planning, propose phase, plant on masterplan, or branch plan.
---

# Phase Planner — Propose → Approve → Plant / Branch

MASTERPLAN.md is the structured, expandable planning system for the whole project.  
It must remain the single checklist that both humans and machines can open to see exactly where development stopped, organized by field (Foundation, Backend, 3rd-Party, Frontend, Integration, etc.).

## When to Use

- Before starting any non-trivial work
- When the user states a new goal or feature
- Before creating a new XXX row
- When continuing from an existing baseline

## Core Workflow

### 1. Propose (do this first — never plant without approval)

Produce a clear proposal containing:

- **Proposed Phase / Field** (e.g. Backend, Frontend, 3rd-Party, Integration, Foundation)
- **Proposed XXX number** (next available or continuation)
- **Target** (short name)
- **Impact** (LOCAL | BOUNDED | SYSTEMIC)
- **Authority** (what owns this)
- **Consumers** (what will be affected)
- **Why this phase / why now**
- **Dependencies** (what must already be done)
- **Risks / open questions**
- **Suggested first finding title**

Present the proposal to the user and **stop**. Do not write to MASTERPLAN.md yet.

### 2. Wait for User Approval

Only after the user explicitly approves (or amends) the proposal may you proceed.

### 3. Plant or Branch on MASTERPLAN.md

**Plant** (first time / new phase):
- Add a new section under the Conceptual Map if needed
- Add the new row(s) to the Execution Checklist
- Update Current Focus

**Branch** (continuation / has existing baseline):
- Add the new XXX under the existing phase/field
- Clearly show it continues from a previous XXX
- Update Current Focus

Always keep the checklist ordered and easy to scan by field so anyone can instantly see progress and where work stopped.

## Output Format for Proposal

```markdown
## Phase Proposal

**Field / Phase:** Backend
**Proposed XXX:** 014
**Target:** auth-refresh-token
**Impact:** BOUNDED
**Authority:** docs/contracts/auth-v1.yaml
**Consumers:** src/backend/auth/, src/frontend/auth/
**Why now:** …
**Depends on:** 011, 012
**Risks:** …
**First finding:** 014-backend-auth-refresh-token.md

Awaiting your approval to plant/branch this on MASTERPLAN.md.
```

## Rules

- Never invent an XXX that is not first proposed and approved.
- Never start Observe / coding until the row exists on MASTERPLAN.md.
- Keep MASTERPLAN.md scannable by field (Foundation → Backend → 3rd-Party → Frontend → Integration → …).
- After planting, update the Current Focus block.
