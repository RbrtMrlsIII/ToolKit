-- Supabase schema — generic, applicable to all projects
-- Authority: supabase schema
-- Census counts this as data_models

create table if not exists projects (
  id uuid primary key default gen_random_uuid(),
  xxx text not null, -- from MASTERPLAN 001, 002...
  phase text not null, -- scaffold, contract, knowledge, etc.
  target text not null,
  status text default 'TODO',
  created_at timestamp default now()
);

create table if not exists knowledge (
  id uuid primary key default gen_random_uuid(),
  xxx text not null,
  pattern_type text not null, -- Validated Patterns, Anti-Patterns, Gotchas
  description text not null,
  evidence_link text,
  created_at timestamp default now()
);

create table if not exists census (
  id uuid primary key default gen_random_uuid(),
  date date not null,
  tabs_total int,
  ui_screens_total int,
  models_3d_total int,
  status text,
  report_path text
);
