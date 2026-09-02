# Prompt: Knowledge Search + Anti-Repeat

```
Before Classify, search PRODUCT-KNOWLEDGE.md for your planned approach:

python scripts/knowledge-search.py "your planned approach"
python scripts/knowledge-search.py "patch1.md" --anti
python scripts/knowledge-search.py --score

If approach is in Anti-Patterns → STOP, create investigation, use Validated Pattern instead.
If approach has Validated Pattern → MUST use it.

This prevents trial-and-error previous agents already passed.

Skill: skills/anti-pattern-checker/SKILL.md
```
