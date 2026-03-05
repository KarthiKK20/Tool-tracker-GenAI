from scrapers.github_scraper import scrape_github_trending
from scrapers.reddit_scraper import scrape_reddit_mentions

from etl.extract import extract_github_data
from etl.transform import transform_data
from etl.load import load_to_database

import pandas as pd


def run_pipeline():

    scrape_github_trending()
    scrape_reddit_mentions()

    github_df = pd.read_csv("github_data.csv")
    reddit_df = pd.read_csv("reddit_data.csv")

    df = pd.concat([github_df, reddit_df])

    df = transform_data(df)

    load_to_database(df)

    print("Pipeline completed.")


if __name__ == "__main__":
    run_pipeline()