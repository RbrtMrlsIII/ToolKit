-- RLS policies — generic
alter table projects enable row level security;
create policy "Allow all for authenticated" on projects for all using (auth.role() = 'authenticated');
