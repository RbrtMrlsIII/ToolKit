# 004 — Responsibility Unit + Seat Model

**XXX:** 004-responsibility-unit-seat-model  
**Field:** Foundation  
**Status:** OBSERVED  
**Scope:** Universal Toolkit only

## Purpose

Define the smallest reusable unit of accountable work and the boundary that equips an Agent to perform it. The model must scale across consuming projects without copying the skill system or importing consumer-specific authority.

## Responsibility Unit

A Responsibility Unit is the atomic accountable work definition:

```text
Responsibility Unit
= objective
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

Every unit must have an explicit authority boundary. A unit can describe work, but it cannot grant permission to perform work.

## Seat

A Seat is the execution boundary that equips one or more responsibility units:

```text
Seat
= responsibility units
+ workspace governance
+ project adaptation
+ applicable skill bundle
+ execution capacity
```

The Seat is reusable infrastructure. Its project adaptation determines how universal mechanisms are applied to a consuming project while preserving that project's own Product Law and authorization.

## Agent assignment

An Agent is the current worker assigned to one or more Responsibility Units. Agent identity is therefore separate from responsibility definition.

```text
Toolkit skill library
        ↓
Responsibility Unit
        ↓
Seat configuration
        ↓
Agent assignment
        ↓
execution + verification + handover
```

Changing Agent count changes allocation, not the underlying skill library.

## Scale rules

### Two-Agent baseline

Use broad responsibility units while keeping integration and verification explicit.

```text
Agent A: discovery + planning + analysis
Agent B: implementation + verification + operations
```

### Three-to-four Agent expansion

Split major specialist and integration responsibilities when parallel work reduces coupling or improves verification.

### Five-to-eight Agent expansion

Partition responsibility where justified into discovery, planning, research, design, implementation, verification, operations, and review/coordination.

More Agents are not permission to multiply skills, duplicate Product Law, or create competing authority.

## Skill resolution

A Seat loads the smallest sufficient skill bundle:

```text
project type
+ field
+ current XXX / phase
+ task / domain
+ provider / runtime
+ tools / plugins
+ project guidance
+ permissions / policy
= effective skill set
```

Skills remain instructional. Product Law determines truth, policy determines rules, permissions determine whether an action may occur, and project authority determines consumer-specific meaning.

## Boundary and handover

A Responsibility Unit must identify what it owns and what it hands over. Consumer-specific credentials, schemas, domain rules, provider decisions, and product semantics remain outside universal Toolkit authority.

## Verification invariants

A 004 implementation is valid only when:

1. every Responsibility Unit has an objective and scope;
2. required skills and knowledge are explicit;
3. authority boundaries are explicit and non-authorizing;
4. inputs, dependencies, outputs, verification, and handover are represented;
5. Seat configuration separates universal mechanisms from project adaptation;
6. Agent assignment is distinct from responsibility definition;
7. scaling changes allocation rather than duplicating the skill library;
8. the consuming-project boundary remains intact;
9. canonical governance and evidence remain traceable.

## Non-goals

004 does not implement a runtime scheduler, autonomous authorization, provider credentials, consumer-specific product law, or automatic upstream knowledge promotion. Those require later validated slices or the consuming project's own authority.
