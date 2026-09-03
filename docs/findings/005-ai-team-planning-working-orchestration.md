# 005-ai-team-planning-working-orchestration

**Field:** Foundation / Governance
**Phase:** AI team orchestration
**Target:** planning-working-team-orchestration
**Impact:** SYSTEMIC
**Status:** RECORDED
**Date:** 2026-09-03

## Generalized lesson
A reusable AI project toolkit needs to distinguish the **planning team** from the **working/coding team** while preserving one coherent team/seat/capability model.

### Planning Team

Planning is deliberation, not implementation.

A user may configure participating AI seats, fixed sequential turns, turns-per-AI, and a selected summarizer/team lead. Each AI receives minimal relevant context for its turn. One authorized document-authoring path may record the agreed decision while the remaining participants stay advisory and continue field-specific analysis, challenges, pros/cons, risk checks, or alternative proposals. The selected summarizer converts discussion into a structured handoff, but durable document or project mutation requires explicit user approval.

### Working Team

Execution consumes the approved planning result rather than the raw discussion transcript as its only source. AI work produces durable task/result/event/handoff state. The scheduler, not an AI provider, selects the next eligible worker. Human approvals, permissions, budgets, provider capability, connection health, and recovery policies remain authoritative boundaries.

### Cross-provider orchestration

The generalized mechanism is:

`AI result/action → durable event → task/state transition → scheduler eligibility → next AI/tool/human → new event`

The previous AI does not directly control or invoke the next AI provider. This avoids provider coupling and keeps orchestration explainable and recoverable.

### External AI application connection and equipment

Users may need to create/configure provider accounts or agent applications outside the consuming project's web UI. The consuming project should therefore support connection activation/import rather than assuming every provider can be fully provisioned in-app.

An AI seat should be configurable as:

`provider + service/runtime + exact model/variant + skills + plugins/tools/MCP + workstation + scopes + permissions + approval gates + limits + compliance state`

Model selection alone is not sufficient to describe an operational agent.

### Plugin/tool/MCP boundary

Plugins are capabilities, not intelligence. A reusable product should model:

`AI seat → authorized tool intent → policy engine → project-scoped plugin/connection → tool invocation → result/artifact → durable event`

The AI receives authorized capabilities, not raw credentials. Plugin scopes are granted by the user/project. Tool results do not silently grant additional authority. MCP can provide a standardized tool/context integration surface, but does not replace the consuming project's scheduler, identity, permissions, durable state, or human approval model. MCP's current 2026-07-28 specification makes Tasks an extension and continues to evolve authorization and transport semantics, so reusable skills should be compatibility/profile aware rather than encoding one permanent MCP assumption.

### Shared chat vs model context

A rich team chat may visually expose the whole conversation, but each AI should receive an explicit context packet chosen by relevance and authorization:

`visible conversation → message/event records → relevance/context selector → authorized context packet → receiving AI`

Receiving AIs may consume explicitly included prior contributions, human interventions, structured handoffs, relevant task/event state, and authorized artifacts. They should not automatically receive private provider/model state, unrelated project data, credentials, or unrestricted repository contents.

## Why it matters

Without these distinctions a product can accidentally build a dashboard around isolated model calls instead of a durable AI-team operating environment. It can also create hidden provider-to-provider coupling, duplicate permission systems, uncontrolled context duplication, or frontend authority over execution.

## Source
Validated from TeamAi pre-029 planning discussion and existing TeamAi Product Law / specification contracts.

## Distillation status
Recorded for generalized ToolKit learning. **Not yet promoted to permanent endorsed PRODUCT-KNOWLEDGE.md.** Promotion should occur only after the consuming-project implementation and validation demonstrate that the lesson is reusable beyond TeamAi.
