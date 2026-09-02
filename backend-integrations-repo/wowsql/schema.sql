-- WowSQL / MySQL schema — generic for all projects
-- Census counts as data_models

CREATE TABLE IF NOT EXISTS projects (
  id VARCHAR(36) PRIMARY KEY,
  xxx VARCHAR(10) NOT NULL,
  phase VARCHAR(50) NOT NULL,
  target VARCHAR(100) NOT NULL,
  status VARCHAR(20) DEFAULT 'TODO',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS knowledge (
  id VARCHAR(36) PRIMARY KEY,
  xxx VARCHAR(10) NOT NULL,
  pattern_type VARCHAR(50) NOT NULL,
  description TEXT NOT NULL,
  evidence_link TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS census_inventory (
  id VARCHAR(36) PRIMARY KEY,
  date DATE NOT NULL,
  tabs_total INT,
  ui_screens_total INT,
  ui_components_total INT,
  models_3d_total INT,
  status VARCHAR(20)
);

-- For tabs count
CREATE TABLE IF NOT EXISTS tabs (
  id VARCHAR(36) PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  path VARCHAR(255),
  order_index INT
);
