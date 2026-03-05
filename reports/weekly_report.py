from analytics.trend_score import compute_trend_scores


def generate_report():

    trends = compute_trend_scores()

    top_tools = trends.head(5)

    print("\nTop Trending GenAI Tools\n")

    print(top_tools)

    top_tools.to_csv("top_trending_tools.csv")

    print("\nReport saved to top_trending_tools.csv")