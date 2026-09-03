---
name: phase-planner
description: Propose an execution phase first, then require backend-authority clarification and user approval before planting or implementation.
---

# Phase Planner — Propose → Clarify Backend → Approve → Plant / Branch

MASTERPLAN.md is the structured, expandable planning system for the whole project.

## 1. Propose
For every non-trivial goal, identify:
- Field / Phase
- proposed XXX
- target
- impact
- authority
- consumers
- reason now
- dependencies
- risks
- first finding

## 2. Backend-first clarification
Before implementation begins, use `backend-first-clarifier` when the idea can affect identity, durable state, server execution, commerce, ownership, or delivery. Clarify the backend authority model with the user and record any blocker or explicit deferral.

This is a clarification gate, not permission to silently choose architecture on the user's behalf.

## 3. Approval
Do not plant a new XXX until the user explicitly approves or amends the proposal and backend clarification is recorded where applicable.

## 4. Plant / Branch
After approval:
- Plant a new phase/XXX in MASTERPLAN.md, or
- Branch a continuation under the existing field.

Then update Current Focus.

## Rules
- Never invent an XXX that is not first proposed and approved.
- Never start Observe / coding until the row exists on MASTERPLAN.md.
- Do not allow a UI-first implementation to bypass backend authority clarification.
- Keep MASTERPLAN.md scannable by field.
- Completion of a consuming-project gate requires the target-project handover skill; ToolKit itself does not hand over projects.
