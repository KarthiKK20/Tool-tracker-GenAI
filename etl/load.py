import sqlite3

def load_to_database(df):

    conn = sqlite3.connect("genai_trends.db")
    cursor = conn.cursor()

    for _, row in df.iterrows():

        cursor.execute(
            "INSERT OR IGNORE INTO tools (tool_name, category) VALUES (?, ?)",
            (row["tool_name"], "GenAI Tool")
        )

        cursor.execute(
            "SELECT tool_id FROM tools WHERE tool_name=?",
            (row["tool_name"],)
        )

        tool_id = cursor.fetchone()[0]

        cursor.execute(
            """
            INSERT INTO metrics (tool_id, platform, metric_name, metric_value, captured_date)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                tool_id,
                row["platform"],
                row["metric_name"],
                row["metric_value"],
                row["captured_date"]
            )
        )

    conn.commit()
    conn.close()

    print("Data loaded into database.")