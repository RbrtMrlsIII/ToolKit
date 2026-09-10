# TOOLKIT_ARCHITECTURE.md — Universal Operating Architecture

## Purpose

This document is the conceptual architecture for Universal AGENT Toolkit. `README.md` remains the front door; this file owns the deeper model.

## 1. Five-layer architecture

```text
UNIVERSAL TOOLKIT
      │
      ├── GOVERNANCE
      │     authority, policy, integrity, approval, recovery
      │
      ├── KNOWLEDGE
      │     patterns, anti-patterns, conceptual field connections
      │
      ├── SKILLS
      │     executable procedures selected by scope and task
      │
      ├── ADAPTATION
      │     project type, field, phase, provider/runtime, tools, scale
      │
      └── RESPONSIBILITY
            units → seats → assigned Agents
                        │
                        ▼
                 consuming project
```

Toolkit is the operating substrate. The consuming project remains the product authority.

## 2. Universal core vs consumer extension

| Class | Definition | Promotion rule |
|---|---|---|
| UNIVERSAL | Reusable mechanism across projects | May live in Toolkit core |
| ADAPTABLE | Universal mechanism whose parameters vary | Keep generic mechanism + explicit consumer adapter |
| CONSUMER-SPECIFIC | Product law, domain, provider, runtime, credentials, UI semantics | Never copy upstream merely for reuse |
| EPHEMERAL | Current session/task finding | Distill or discard according to lifecycle |
| HISTORICAL | Preserved prior evidence | Never silently treat as current authority |
| CANDIDATE | Generalized lesson awaiting acceptance | Needs validation + endorsement |
| ENDORSED | Accepted reusable lesson | May become universal knowledge/skill |

## 3. Responsibility Unit model

A Responsibility Unit is the atomic operating unit:

```text
objective
+ scope
+ required knowledge
+ required skills
+ authority boundary
+ inputs
+ dependencies
+ outputs
+ verification
+ handover
```

A seat assembles Responsibility Units. An Agent receives currently assigned units. This permits 2-Agent, 4-Agent, or 8-Agent execution without cloning the skill library.

## 4. Skill growth follows baseline growth

Execution slices become more repeatable as baselines freeze. Every freeze triggers a skill-coverage question:

```text
new validated baseline
        ↓
what procedure can now be repeated?
        ↓
existing skill sufficient?
   ┌────┴────┐
  yes       no
   │         │
reuse    candidate skill / extension / validator
             ↓
      scope + dependencies + evidence
             ↓
          endorse
             ↓
      future slice execution
```

The skill system therefore grows with the project while keeping authority stable.

## 5. Dynamic skill resolution

The effective bundle is resolved from:

```text
project type
+ field
+ current slice / XXX
+ task / domain
+ provider / runtime
+ tools / plugins
+ project guidance
+ permissions / policy
= smallest sufficient skill bundle
```

A skill is procedural equipment, not an authorization grant.

## 6. User-first execution chain

The universal chain is:

```text
user command / vision
   ↓
consult applicable Agents
   ↓
user approval for material direction
   ↓
reconstruct PRODUCT_LAW.md
   ↓
MASTERPLAN.md checklist / execution slice
   ↓
skill bundle + PRODUCT-KNOWLEDGE
   ↓
O-R-U-C-A-V-E-A
   ↓
action / implementation
   ↓
validation
   ↓
evidence
   ↓
complete session / execution log
   ↓
endorsement
   ↓
PRODUCT-KNOWLEDGE growth
   ↺ skills / governance / architecture evolution
```

The order is deliberate. An Agent may consult, analyze, and propose before approval; it may not silently replace the user's intent with its own interpretation.

## 7. Current / derived / historical / candidate / endorsed state

Every knowledge-bearing artifact should be classifiable as one of:

- `CURRENT`: active canonical state.
- `DERIVED`: generated or indexed view of current state.
- `HISTORICAL`: preserved evidence and evolution record.
- `CANDIDATE`: proposed reusable lesson or pattern.
- `ENDORSED`: accepted reusable knowledge.

State labels are not cosmetic. They control what may influence execution.

## 8. Canonical change contract

Every meaningful change should declare:

```text
change
→ user objective / authority
→ Product Law scope
→ Masterplan slice
→ affected canonical artifacts
→ affected skills
→ affected knowledge / evidence
→ verification plan
→ expected preservation boundaries
→ endorsement requirement
```

For canonical documents, the contract must make unrelated sections implicitly protected. A change must not use a narrow request as permission to rewrite the whole document.

## 9. Canonical Structure Preservation

Canonical documents are knowledge structures, not ordinary prose files.

The integrity gate must detect:

```text
INTENDED_CHANGE
UNINTENDED_STRUCTURAL_CHANGE
CANONICAL_SECTION_LOSS
UNEXPLAINED_DELETION
```

The default result for unexplained canonical loss is FAIL CLOSED.

A semantic check such as “new claim exists” is insufficient. The validator must also prove that protected headings and unrelated content remain present unless the change contract explicitly permits their removal.

## 10. Bidirectional consistency

ToolKit should progressively enforce these relationships in both directions:

```text
claim ↔ evidence
skill ↔ scope
field ↔ responsibility
baseline ↔ skill coverage
documentation ↔ implementation / evidence
```

One-way pointers are useful indexes but are not complete consistency proof.

## 11. Knowledge growth without knowledge pollution

PRODUCT-KNOWLEDGE grows in depth, not noise.

The permanent brain should increasingly explain:

```text
field
  ↕
responsibility
  ↕
skill
  ↕
artifact / interface
  ↕
provider / runtime
  ↕
verification
  ↕
consumer pattern
```

This is conceptual mapping. Raw logs remain elsewhere. Product-specific implementation facts stay downstream.

## 12. Cross-project learning feedback

```text
ToolKit mechanism
      ↓
consumer project
      ↓
execution pressure / failure / discovery
      ↓
validated evidence
      ↓
generalization review
   ┌────┴─────┐
 reusable   specific
    ↓          ↓
Toolkit     consumer
candidate   knowledge
    ↓
endorsement
    ↓
Toolkit evolution
```

TeamAi is a source of lessons, not a source of authority for Toolkit.

## 13. Capability and discipline must grow together

Track two axes:

**Capability growth**
- skills
- adapters
- project types
- fields
- tools
- integrations
- scale support

**Discipline growth**
- authority resolution
- change integrity
- evidence consistency
- historical protection
- knowledge promotion
- responsibility allocation
- recovery / reconciliation
- user-vision preservation

A change is healthy when both dimensions are understood and verified.
