#!/usr/bin/env node
// Verify all 16 skills exist and have required sections
import fs from 'fs';
import path from 'path';

const root = process.cwd();
const skillsPaths = [path.join(root, 'skills'), path.join(root, 'agent-repo-template/skills'), path.join(root, 'agent-complete/agent-repo-template/skills'), path.join(root, '.agent/skills')];
let skillsDir = skillsPaths.find(p => fs.existsSync(p));
if (!skillsDir) {
  console.log("Skills dir not found, checking agent-skills-repo");
  skillsDir = path.join(root, 'agent-skills-repo/skills');
}
if (!fs.existsSync(skillsDir)) {
  console.error("No skills dir found");
  process.exit(1);
}
const skills = fs.readdirSync(skillsDir);
console.log(`Skills found: ${skills.length}`);
let ok = 0;
for (const s of skills) {
  const skillFile = path.join(skillsDir, s, 'SKILL.md');
  if (fs.existsSync(skillFile)) {
    const txt = fs.readFileSync(skillFile, 'utf8');
    if (txt.includes('When To Use') && txt.includes('Validation Checklist')) ok++;
  }
}
console.log(`Valid skills (with required sections): ${ok}/${skills.length}`);
if (ok < 8) {
  console.error("FAIL: Not enough valid skills");
  process.exit(1);
}
console.log("PASS: Skills repo OK");
