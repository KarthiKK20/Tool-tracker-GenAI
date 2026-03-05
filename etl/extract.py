import pandas as pd

def extract_github_data():
    
    df = pd.read_csv("github_data.csv")

    print("Extracted Data:")
    print(df.head())

    return df


if __name__ == "__main__":
    extract_github_data()