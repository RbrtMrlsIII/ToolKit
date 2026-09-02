# Queries for census inventory
def get_tabs_count(conn):
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM tabs")
    return cur.fetchone()[0]

def get_ui_screens_count(conn):
    # Example: count from projects where phase = frontend
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM projects WHERE phase LIKE '%frontend%' OR phase LIKE '%ui%'")
    return cur.fetchone()[0]
