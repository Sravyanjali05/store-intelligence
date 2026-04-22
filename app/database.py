import sqlite3

conn = sqlite3.connect("store.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS events (
    event_id TEXT,
    store_id TEXT,
    visitor_id TEXT
)
""")

conn.commit()