import sqlite3

conn = sqlite3.connect("genai_trends.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM metrics")

rows = cursor.fetchall()

for r in rows:
    print(r)

conn.close()