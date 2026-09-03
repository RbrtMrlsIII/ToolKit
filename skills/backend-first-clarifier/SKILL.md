---
name: backend-first-clarifier
description: Universal gate requiring backend authority clarification before a project moves from idea into implementation.
---

# Backend-First Clarifier

Use after a user presents or materially changes a product idea and before implementation begins.

## Required clarification
Establish, at the level applicable to the idea:

1. identity/authentication authority;
2. durable domain/application state authority;
3. trusted server/runtime authority;
4. payment/commerce authority when applicable;
5. delivery/browser/verification surfaces;
6. ownership root and server-side correlation rules;
7. known blockers and evidence needed before implementation.

Do not require needless detail. Clarify enough to prevent a UI-first implementation from silently creating a parallel authority path.

## Decision rule
Implementation may proceed only after the backend authority model is clarified and recorded, or the user explicitly accepts a documented backend deferral with its blocker preserved.

## Boundary
This skill does not choose a project's architecture for the user. It makes the authority questions explicit so the project can decide and record them.

## Output
Produce or update the target project's finding/contract before implementation. ToolKit does not become the target project's authority and does not produce its handover package.
