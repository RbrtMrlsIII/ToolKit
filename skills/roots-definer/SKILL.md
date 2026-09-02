---
name: roots-definer
description: Define or validate the roots of a program or feature before any coding or phase planning. First checks for an existing root, then walks through core problem, inputs/outputs, scope, dependencies, architecture, data model, success metrics, risks, and breakdown strategy. Use when starting a new product, major feature, when a root may already exist, or when the user asks to define or review roots.
---

# Roots Definer — Define Before You Plan

Use this skill **before** `phase-planner` when the work is still at the problem / architecture level.  
Its output becomes the foundation that later XXXs and the MASTERPLAN fields rest on.

## When to Use

- Brand-new product or major new capability
- User says “define the roots”, “frame the problem”, “what are we actually building?”
- Before the first real Backend / Frontend / Integration phases
- When Source-of-Truth or high-level architecture is still unclear
- When an existing root might already be present (always check first)

---

## 0. Existing Root Check (Mandatory First Step)

Before doing anything else:

1. Search for an existing root in:
   - `PRODUCT-KNOWLEDGE.md`
   - `docs/contracts/`
   - `docs/findings/` (especially Foundation field)
   - `docs/architecture-map.md`
   - `MASTERPLAN.md` vision / Source-of-Truth statement
2. Decision:
   - **Valid root found** → Reuse it. Reference it clearly. Only propose a delta if something is outdated or missing. Then hand off to `phase-planner`.
   - **Incomplete / outdated root** → Run a light review. Update only the broken parts. Record the delta as a finding and distill.
   - **Conflicting roots** → Create an investigation / reconciliation. Do not overwrite. Involve `safety-reporter` if needed.
   - **No adequate root exists** → Proceed with the full 9 steps below.

Never silently re-define a root that already exists.

---

## Nine Root Steps (only if no adequate root exists)

### 1. Identify the Core Problem
State clearly:
- What must the program / feature achieve?
- Why is it needed? (pain, opportunity, constraint)
- Who suffers if it does not exist?

### 2. Determine Inputs and Outputs
- List all inputs (data, events, user actions, external signals)
- List all outputs (results, side-effects, artifacts, API responses, UI states)
- Note format / timing / volume expectations where known

### 3. Establish Scope and Boundaries
- In-scope (what this will do)
- Explicitly out-of-scope (what is left for later or never)
- Non-goals

### 4. Map Dependencies and Resources
- Required libraries, services, 3rd-party APIs
- Data sources
- Existing internal modules or contracts that must be reused
- Team / skill / infrastructure constraints

### 5. Map the Architecture
- Chosen style / patterns (modular monolith, event-driven, clean architecture, etc.)
- Major components and their responsibilities
- How components communicate (sync, async, events, shared DB, etc.)
- High-level diagram description (later becomes / updates `docs/architecture-map.md`)

### 6. Design the Data Model
- Key entities / objects
- Relationships
- Storage approach (tables, documents, files, etc.)
- Ownership of data
- Initial schema sketches or TypeScript/JSON shapes if helpful

### 7. Define Success Metrics
- Quantitative goals (latency, throughput, error rate, test coverage, etc.)
- Qualitative goals (usability, maintainability, continuity)
- How we will know the roots definition itself succeeded

### 8. Identify Risks and Constraints
- Technical limitations
- Security / privacy concerns
- Scale bottlenecks
- Continuity / multi-agent risks
- External dependencies that can fail
- Trigger `safety-reporter` if any risk is SYSTEMIC or destructive

### 9. Create a Break-Down Strategy
- Split into ordered, manageable milestones
- Suggest which Field(s) on MASTERPLAN they belong to (Foundation, Backend, 3rd-Party, Frontend, etc.)
- Propose the first 3–7 concrete XXXs that should be fed into `phase-planner`
- Note any parallel vs sequential work

---

## Output Format

```markdown
# Roots Definition — [Name of Product / Feature]

## 0. Existing Root Check
- Result: Reused existing / Updated delta / Created new
- Location of root used: …

## 1. Core Problem
…

## 2. Inputs and Outputs
…

## 3. Scope and Boundaries
…

## 4. Dependencies and Resources
…

## 5. Architecture
…

## 6. Data Model
…

## 7. Success Metrics
…

## 8. Risks and Constraints
…

## 9. Break-Down Strategy
- Suggested MASTERPLAN Fields: …
- Proposed first XXXs (for phase-planner):
  1. …
  2. …
  3. …
```

---

## After the Roots Are Defined or Validated

1. Present the full output to the user.
2. Once approved, store it (Foundation finding or `docs/contracts/`).
3. Hand the Break-Down Strategy to `phase-planner`.
4. Update PRODUCT-KNOWLEDGE.md if new patterns or anti-patterns emerged.
5. If the root itself changed Source-of-Truth → treat as SYSTEMIC and use `safety-reporter`.

## Rules

- Always perform the Existing Root Check first.
- Do not skip steps when creating a new root.
- Do not start coding or creating XXXs until the (new or validated) root is approved.
- Keep the output dense and scannable.
