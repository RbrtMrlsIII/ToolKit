# SKILL: Census Runner

> Universal skill as MD file. Load before Census.

### Metadata
- ID: census-runner
- Phase: Census
- Type: governance
- Applies To: All projects

### When To Use
Weekly, before checkpoint.

### Prerequisites
scripts/census.py exists

### Steps
1. Run census.py --write\n2. Read JSON status\n3. Fix fails, re-run

### Output Template
census JSON + report MD

### Validation Checklist
- [ ] census executed\n- [ ] No FAIL

### Anti-Patterns
Ignoring FAIL

### Distillation to PRODUCT-KNOWLEDGE.md
Census quirk to Knowledge

### Cross-References
- Load next skill per SKILLS_INDEX.md O-R-U-C-A-V-E-A
- Always check PRODUCT-KNOWLEDGE Anti-Patterns before, update Validated Patterns after
