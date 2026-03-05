import pandas as pd
import random

def scrape_reddit_mentions():

    tools = [
        "LangChain",
        "AutoGPT",
        "LlamaIndex",
        "CrewAI",
        "Haystack",
        "OpenDevin"
    ]

    data = []

    for tool in tools:

        mentions = random.randint(50, 500)

        data.append({
            "tool_name": tool,
            "platform": "Reddit",
            "metric_name": "mentions",
            "metric_value": mentions
        })

    df = pd.DataFrame(data)

    df.to_csv("reddit_data.csv", index=False)

    print("Reddit data simulated.")

    return df


if __name__ == "__main__":
    scrape_reddit_mentions()