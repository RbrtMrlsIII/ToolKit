# Prompt: Align + Validate

```
After Classify:
1. Make smallest bounded change — ONE XXX only, no opportunistic refactors
2. Follow stack standard but never forbidden names (patch*, final*)
3. Validate source + consumers: tests, typecheck, lint
4. Run census: python scripts/census.py --base . --write — must PASS
5. Create validation/evidence/XXX-phase-target.md from TEMPLATE
6. Update finding Align + Validate sections

Skills: skills/align/SKILL.md, skills/validate/SKILL.md, skills/census-runner/SKILL.md
Census counts: tabs, UI screens, components, 3D models before conversion
```
