#!/usr/bin/env node
// Count 3D assets before conversion
import fs from 'fs';
import path from 'path';

const exts = ['.glb','.gltf','.obj','.fbx','.usd','.usda','.stl','.blend'];
let models = [];
function walk(dir) {
  try {
    for (const e of fs.readdirSync(dir, {withFileTypes:true})) {
      if (e.name.startsWith('.') || e.name === 'node_modules') continue;
      const full = path.join(dir, e.name);
      if (e.isDirectory()) walk(full);
      else if (exts.some(ext => full.toLowerCase().endsWith(ext))) models.push(full);
    }
  } catch {}
}
walk(process.cwd());
console.log(`3D Models found: ${models.length}`);
models.slice(0,20).forEach(f => console.log(` - ${f}`));
console.log(`Before converting to 3D: you have ${models.length} 3D assets`);
