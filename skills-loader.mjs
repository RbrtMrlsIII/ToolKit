#!/usr/bin/env node
/**
 * skills-loader.mjs — Skill Orchestrator
 * Part of bright improvement #5
 * Reads registry.json current_xxx, MASTERPLAN.md row, auto-loads correct skill
 * For mobile AI: node skills-loader.mjs
 */

import fs from 'fs';
import path from 'path';

function findFile(relativePaths) {
  for (const p of relativePaths) {
    if (fs.existsSync(p)) return p;
  }
  return null;
}

const root = process.cwd();
const registryPaths = [
  path.join(root, '.agent/continuity/registry.json'),
  path.join(root, 'agent-repo-template/.agent/continuity/registry.json'),
  path.join(root, 'agent-complete/agent-repo-template/.agent/continuity/registry.json')
];
const registryPath = findFile(registryPaths);
let currentXXX = '001';
let knowledgeRows = 0;
if (registryPath) {
  try {
    const reg = JSON.parse(fs.readFileSync(registryPath, 'utf8'));
    currentXXX = reg.current_xxx || '001';
    knowledgeRows = reg.knowledge_index?.total_rows || 0;
  } catch {}
}

const masterplanPaths = [
  path.join(root, 'MASTERPLAN.md'),
  path.join(root, 'agent-repo-template/MASTERPLAN.md'),
  path.join(root, 'agent-complete/agent-repo-template/MASTERPLAN.md')
];
let masterplanRow = null;
const mpPath = findFile(masterplanPaths);
if (mpPath) {
  const mpText = fs.readFileSync(mpPath, 'utf8');
  const match = mpText.match(new RegExp(`\\|\\s*${currentXXX}\\s*\\|([^\\n]+)`, 'i'));
  if (match) masterplanRow = match[0];
}

const pkPaths = [
  path.join(root, 'PRODUCT-KNOWLEDGE.md'),
  path.join(root, 'agent-repo-template/PRODUCT-KNOWLEDGE.md')
];
const pkPath = findFile(pkPaths);
let antiPatterns = [];
if (pkPath) {
  const pkText = fs.readFileSync(pkPath, 'utf8');
  // Extract Anti-Patterns table rows
  const antiMatch = pkText.match(/## 2\. Anti-Patterns[\s\S]*?(?=##|$)/);
  if (antiMatch) {
    antiPatterns = antiMatch[0].split('\n').filter(l => l.startsWith('|') && !l.includes('Anti-Pattern') && !l.includes('---')).slice(0,5);
  }
}

// Determine phase from MASTERPLAN or XXX
const phaseMap = {
  '000': 'scaffold', '001': 'scaffold', '002': 'scaffold', '003': 'contract', '004': 'census',
  '005': 'align', '006': 'align', '007': 'validate', '008': 'knowledge', '009': 'endorse'
};
let phase = 'observe';
if (masterplanRow) {
  const phaseMatch = masterplanRow.match(/\|\s*\w+\s*\|\s*(\w+)\s*\|/);
  if (phaseMatch) phase = phaseMatch[1].toLowerCase();
} else {
  phase = phaseMap[currentXXX] || 'observe';
}

// Map phase to skill
const skillMap = {
  'scaffold': 'scaffold-initializer',
  'observe': 'observe',
  'record': 'record',
  'understand': 'understand',
  'classify': 'classify',
  'align': 'align',
  'validate': 'validate',
  'endorse': 'endorse',
  'advance': 'advance',
  'contract': 'contract-manager',
  'census': 'census-runner',
  'knowledge': 'knowledge-distiller'
};
const skillId = skillMap[phase] || 'observe';

const skillPaths = [
  path.join(root, `skills/${skillId}/SKILL.md`),
  path.join(root, `.agent/skills/${skillId}/SKILL.md`),
  path.join(root, `agent-repo-template/skills/${skillId}/SKILL.md`),
  path.join(root, `agent-complete/agent-repo-template/skills/${skillId}/SKILL.md`),
  path.join(root, `agent-skills-repo/skills/${skillId}/SKILL.md`)
];
const skillPath = findFile(skillPaths);

console.log(`=== Skill Orchestrator ===`);
console.log(`Current XXX: ${currentXXX}`);
console.log(`Phase: ${phase}`);
console.log(`Skill to load: ${skillId}`);
console.log(`Skill path: ${skillPath || 'NOT FOUND'}`);
console.log(`Knowledge rows: ${knowledgeRows}`);
console.log(`MASTERPLAN row: ${masterplanRow || 'Not found'}`);
console.log(`\nAnti-Patterns (top 3) to avoid:`);
antiPatterns.slice(0,3).forEach(ap => console.log(` - ${ap.substring(0,120)}`));
console.log(`\nNext actions for mobile AI:`);
console.log(`1. Read PRODUCT-KNOWLEDGE.md Anti-Patterns section`);
console.log(`2. Read skill: ${skillPath || `skills/${skillId}/SKILL.md`}`);
console.log(`3. Execute ${phase} gate per skill steps`);
console.log(`4. Run: python scripts/census.py --base . --write`);
console.log(`5. Distill to PRODUCT-KNOWLEDGE.md before archiving`);
if (skillPath && fs.existsSync(skillPath)) {
  console.log(`\n--- Skill ${skillId} content preview (first 20 lines) ---`);
  console.log(fs.readFileSync(skillPath, 'utf8').split('\n').slice(0,20).join('\n'));
}
