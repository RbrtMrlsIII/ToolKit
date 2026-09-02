// WowSQL MySQL connection MJS
import mysql from 'mysql2/promise';

export async function getConnection() {
  return await mysql.createConnection({
    host: process.env.WOWSQL_HOST || 'localhost',
    user: process.env.WOWSQL_USER || 'root',
    password: process.env.WOWSQL_PASSWORD || '',
    database: process.env.WOWSQL_DB || 'agent_repo'
  });
}
