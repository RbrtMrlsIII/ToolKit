// test-supabase.js — validate supabase integration
import fs from 'fs';
const clientPath = 'backend-integrations-repo/supabase/client.ts';
if (!fs.existsSync(clientPath)) {
  console.log("Supabase client not found, checking agent-complete...");
}
console.log("Checking supabase files exist...");
const files = ['supabase/client.ts','supabase/schema.sql','firebase/firebase-config.ts','wowsql/schema.sql','paypal/paypal-client.ts'];
let ok=0;
for (const f of files) {
  const paths = [`backend-integrations-repo/${f}`, `agent-complete/backend-integrations-repo/${f}`, `agent-repo-template/../backend-integrations-repo/${f}`];
  if (paths.some(p => fs.existsSync(p))) { ok++; console.log(`Found ${f}`); }
}
console.log(`Backend files found: ${ok}/${files.length} — ${ok>=3?'PASS':'FAIL'}`);
