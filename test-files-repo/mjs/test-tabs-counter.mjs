#!/usr/bin/env node
// Count how many tabs do we have — from files and config entries
import fs from 'fs';
import path from 'path';

function findTabFiles(dir, results=[]) {
  try {
    for (const entry of fs.readdirSync(dir, {withFileTypes:true})) {
      if (entry.name.startsWith('.') || entry.name === 'node_modules') continue;
      const full = path.join(dir, entry.name);
      if (entry.isDirectory()) findTabFiles(full, results);
      else if (/tabs|tabbar/i.test(entry.name)) results.push(full);
    }
  } catch {}
  return results;
}

const tabs = findTabFiles(process.cwd());
console.log(`Tabs files found: ${tabs.length}`);
tabs.slice(0,10).forEach(f => console.log(` - ${f}`));

// Try count entries in config files
let entries = 0;
for (const f of tabs) {
  try {
    const txt = fs.readFileSync(f, 'utf8');
    entries += (txt.match(/"path"|"name"|path:/g) || []).length;
  } catch {}
}
console.log(`Estimated tab entries: ${entries}`);
console.log("Use this to know tabs before converting to 3D");
