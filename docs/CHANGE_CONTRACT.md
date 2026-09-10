# CHANGE_CONTRACT.md — Canonical Change Discipline

## Purpose

Every meaningful Toolkit change declares what is changing, why it is authorized, what must remain intact, and what proves completion.

## Required chain

```text
USER OBJECTIVE
  ↓
AUTHORITY
  ↓
SCOPE
  ↓
MASTERPLAN SLICE
  ↓
AFFECTED CANONICAL ARTIFACTS
  ↓
AFFECTED SKILLS / KNOWLEDGE
  ↓
ACTION
  ↓
VERIFICATION
  ↓
EVIDENCE
  ↓
LOG / HANDOVER
  ↓
ENDORSEMENT
```

## Change contract fields

| Field | Required question |
|---|---|
| Objective | What user-approved outcome is being pursued? |
| Authority | Which Product Law / policy / permission permits it? |
| Scope | What exact semantic area may change? |
| Slice | Which MASTERPLAN XXX owns the work? |
| Consumers | Which fields, skills, projects, or artifacts depend on it? |
| Preservation | Which canonical structures are explicitly protected? |
| Skills | Which skills must be loaded or created? |
| Evidence | What evidence will prove the result? |
| Verification | Which tests, checks, or inspections must pass? |
| Knowledge | What reusable lesson may be distilled? |
| Endorsement | What human or authorized approval closes the gate? |

## Canonical preservation rule

For a canonical document, the declared semantic scope is the allowed change boundary. Everything outside it is protected by default.

A PR that introduces the requested change while deleting unrelated canonical sections MUST fail review or validation until the deletion is explicitly explained and authorized.

## Deletion classes

```text
INTENDED_CHANGE
  = deletion/change inside declared scope

UNINTENDED_STRUCTURAL_CHANGE
  = unexplained structural delta

CANONICAL_SECTION_LOSS
  = previously present canonical heading/section disappears

HISTORICAL_DELETION
  = historical evidence removed without explicit archival authority
```

Default policy: `UNINTENDED_STRUCTURAL_CHANGE`, `CANONICAL_SECTION_LOSS`, and `HISTORICAL_DELETION` are fail-closed.

## Minimum human-readable declaration

```markdown
### Change
- Objective: ...
- Authority: ...
- Slice: ...
- Allowed paths: ...
- Allowed semantic sections: ...
- Protected canonical sections: all unrelated sections
- Required skills: ...
- Verification: ...
- Evidence: ...
- Knowledge promotion: yes/no + destination
- Endorsement: required/not required
```

## Relationship to skills

The change contract does not replace a skill. It tells the skill system what work is authorized and what structures must be preserved. Skills explain HOW; policy/permissions explain WHETHER; Product Law defines WHAT IS TRUE.
