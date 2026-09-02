# Prompt: Endorse + Advance — Knowledge Distillation (Most Important)

```
After Validate PASS:
1. DISTILL to PRODUCT-KNOWLEDGE.md — MANDATORY:
   - What worked → Validated Patterns table with XXX + evidence link
   - What failed → Anti-Patterns & Dead Ends table (CRITICAL — prevents repeat errors)
   - Gotcha → Contract & Dependency Gotchas
   - Add Minimalism Log entry: Date | Source Finding | Distilled To | Archived To | XXX
2. Update registry.json knowledge_index: total_rows++, last_distilled_xxx=XXX
3. Update state.json
4. Create docs/handover/XXX-handover.md + .agent/continuity/checkpoint-XXX.md with next AI instructions + anti-repeat check
5. Move finding docs/findings/XXX-...md → docs/archive/XXX-...md with header > DISTILLED TO: PRODUCT-KNOWLEDGE.md section
6. Update MASTERPLAN status to DISTILLED|ENDORSED|ADVANCED
7. Run census again: python scripts/census.py --base . --write — must PASS minimalism (findings <=10)
8. Generate dashboard: docs/census/dashboard-latest.html
9. Update README.md Quick Status
10. Add draft to ENDORSEMENT.md Pending (not self-approve)

Skills: skills/endorse/SKILL.md, skills/advance/SKILL.md, skills/knowledge-distiller/SKILL.md, skills/minimalism-enforcer/SKILL.md, skills/checkpoint-creator/SKILL.md

If you skip distillation, XXX is INCOMPLETE and future AIs will repeat your errors.
```
