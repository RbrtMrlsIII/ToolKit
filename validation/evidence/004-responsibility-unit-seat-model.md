# Validation Evidence — 004 Responsibility Unit + Seat Model

**XXX:** `004-responsibility-unit-seat-model`  
**State:** VALIDATED / ENDORSEMENT PENDING

## Baseline

Validated against the merged 003 self-protecting universal foundation and the existing `docs/WEB_AI_SEAT_FOUNDATION.md`, `docs/SKILL_SCOPE_INDEX.md`, `POLICY.md`, and `PRODUCT-KNOWLEDGE.md` anti-pattern rules.

## Assertions verified

- Responsibility Unit has explicit objective, scope, knowledge, skills, authority boundary, inputs, dependencies, outputs, verification, and handover.
- Seat composes responsibility units with governance, project adaptation, skill bundle, and execution capacity.
- Agent identity is distinct from responsibility definition.
- Scaling changes responsibility allocation rather than duplicating the universal skill library.
- Skill resolution remains scope-aware and never grants authorization.
- Consumer-specific Product Law and permissions remain outside Toolkit authority.

## Validation sequence

1. static structural inspection;
2. canonical-integrity and baseline-governance CI on the exact PR head;
3. review changed-file scope for unintended canonical deletion;
4. confirm continuity state and evidence agree;
5. record advancement decision only after endorsement.

## External CI evidence

Exact PR head `4d817d419588921f367a7b1d81cfdac192061f82` was executed by GitHub Actions workflow `toolkit-governance` run `34541116690`.

- `canonical-integrity`: PASS
- `baseline-governance`: PASS
- Python syntax check: PASS
- required governance documents: PASS

## Scope integrity

PR #6 merged the 004 model without introducing runtime scheduling, automatic authorization, provider credentials, or consumer-specific product authority. The changed-file scope was limited to the 004 model and its continuity/evidence surfaces.

## Current gate

004 is **VALIDATED** but remains **ENDORSEMENT PENDING**. Do not advance to 005 until explicit human/authorized endorsement is recorded.
