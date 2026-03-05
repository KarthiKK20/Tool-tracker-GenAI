import sqlite3
import pandas as pd


def compute_trend_scores():

    conn = sqlite3.connect("genai_trends.db")

    query = """
    SELECT t.tool_name, m.platform, m.metric_value
    FROM metrics m
    JOIN tools t ON m.tool_id = t.tool_id
    """

    df = pd.read_sql_query(query, conn)

    pivot = df.pivot_table(
        index="tool_name",
        columns="platform",
        values="metric_value",
        aggfunc="sum"
    ).fillna(0)

    if "GitHub" not in pivot:
        pivot["GitHub"] = 0

    if "Reddit" not in pivot:
        pivot["Reddit"] = 0

    pivot["trend_score"] = (
        0.6 * pivot["GitHub"] +
        0.4 * pivot["Reddit"]
    )

    ranked = pivot.sort_values("trend_score", ascending=False)

    conn.close()

    return ranked