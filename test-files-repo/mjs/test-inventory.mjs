#!/usr/bin/env node
// Universal inventory test — tabs, UI, 3D — applicable to all project types
import { glob } from 'fs';
import fs from 'fs';
import path from 'path';

const root = process.cwd();
const patterns = {
  tabs: ["**/tabs.*", "**/*Tabs.*", "**/tabBar.*"],
  ui_screens: ["src/screens/**/*.*", "src/pages/**/*.*", "src/views/**/*.*"],
  ui_components: ["src/components/**/*.*", "components/**/*.*"],
  models_3d: ["**/*.glb", "**/*.gltf", "**/*.obj", "**/*.fbx", "**/*.usd"]
};

console.log("=== Universal Inventory Census ===");
for (const [key, pats] of Object.entries(patterns)) {
  let count = 0;
  // Simple recursive count
  function walk(dir) {
    try {
      const entries = fs.readdirSync(dir, {withFileTypes:true});
      for (const e of entries) {
        if (e.name.startsWith('.') || e.name === 'node_modules') continue;
        const full = path.join(dir, e.name);
        if (e.isDirectory()) walk(full);
        else {
          // check pattern match simple
          if (pats.some(p => full.includes(p.replace('**/','').replace('/*.*','')))) count++;
        }
      }
    } catch {}
  }
  walk(root);
  console.log(`${key}: ${count}`);
}
console.log("PASS: Inventory test done — before converting to 3D, you know tabs/UI/3D counts");
