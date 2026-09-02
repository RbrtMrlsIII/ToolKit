# SKILL: Validate — Evidence

> Universal skill as MD file. Load before Validate.

### Metadata
- ID: validate
- Phase: Validate
- Type: core
- Applies To: All projects

### When To Use
After Align.

### Prerequisites
Changed files

### Steps
1. Validate source+consumers\n2. Run census.py --write\n3. Create evidence file

### Output Template
validation/evidence/XXX file

### Validation Checklist
- [ ] Source+consumer PASS\n- [ ] census PASS

### Anti-Patterns
Skipping consumer validation

### Distillation to PRODUCT-KNOWLEDGE.md
Prepare lesson

### Cross-References
- Load next skill per SKILLS_INDEX.md O-R-U-C-A-V-E-A
- Always check PRODUCT-KNOWLEDGE Anti-Patterns before, update Validated Patterns after
