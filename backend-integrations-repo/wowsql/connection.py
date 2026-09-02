# WowSQL/MySQL connection — universal
import os
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("WOWSQL_HOST", "localhost"),
        user=os.getenv("WOWSQL_USER", "root"),
        password=os.getenv("WOWSQL_PASSWORD", ""),
        database=os.getenv("WOWSQL_DB", "agent_repo")
    )

# Validated pattern: use registry as source of truth
