// Supabase client — universal authority example
import { createClient } from '@supabase/supabase-js';

const supabaseUrl = process.env.SUPABASE_URL!;
const supabaseAnonKey = process.env.SUPABASE_ANON_KEY!;

export const supabase = createClient(supabaseUrl, supabaseAnonKey);

// Validated pattern from PRODUCT-KNOWLEDGE.md: Use registry as source of truth, not memory
// Authority: docs/contracts/api-v1.yaml or supabase schema
// Consumers: frontend, mobile, validation
