import sqlite3

conn = sqlite3.connect("genai_trends.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tools (
    tool_id INTEGER PRIMARY KEY AUTOINCREMENT,
    tool_name TEXT,
    category TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS metrics (
    metric_id INTEGER PRIMARY KEY AUTOINCREMENT,
    tool_id INTEGER,
    platform TEXT,
    metric_name TEXT,
    metric_value FLOAT,
    captured_date DATE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS trend_scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tool_id INTEGER,
    week_start DATE,
    trend_score FLOAT
)
""")

conn.commit()
conn.close()

print("Database initialized.")