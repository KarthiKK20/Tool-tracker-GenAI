from flask import Flask, render_template
import sqlite3
import pandas as pd

app = Flask(__name__)


def get_trend_data():

    conn = sqlite3.connect("../genai_trends.db")

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

    pivot["trend_score"] = (
        0.6 * pivot.get("GitHub",0) +
        0.4 * pivot.get("Reddit",0)
    )

    pivot = pivot.sort_values("trend_score", ascending=False)

    conn.close()

    return pivot.reset_index()


@app.route("/")
def dashboard():

    data = get_trend_data()

    tools = data["tool_name"].tolist()
    scores = data["trend_score"].tolist()

    github_scores = data.get("GitHub", []).tolist()
    reddit_scores = data.get("Reddit", []).tolist()

    weekly_growth = [10, 20, 35, 50, 65]

    leaderboard = data.to_dict(orient="records")

    return render_template(
        "index.html",
        tools=tools,
        scores=scores,
        github_scores=github_scores,
        reddit_scores=reddit_scores,
        weekly_growth=weekly_growth,
        leaderboard=leaderboard
    )
if __name__ == "__main__":
    app.run(debug=True)