import pandas as pd
from datetime import datetime

def transform_data(df):

    df["captured_date"] = datetime.today().date()

    df["tool_name"] = df["tool_name"].str.strip()

    df["metric_value"] = df["metric_value"].astype(float)

    print("Transformed Data:")
    print(df.head())

    return df