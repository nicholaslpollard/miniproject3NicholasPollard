# INF601 - Advanced Programming in Python
# Nicholas Pollard
# Mini Project 3

import os

import pandas as pd
import requests


BASE_URL = "https://practice.fhsucyber.com"


def main():
    token = os.getenv("PRACTICE_API_TOKEN")

    if not token:
        raise RuntimeError("PRACTICE_API_TOKEN is not set.")

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        f"{BASE_URL}/api/v1/datasets/movies",
        headers=headers,
        params={"count": 100},
        timeout=30
    )
    response.raise_for_status()

    rows = response.json()["rows"]
    df = pd.DataFrame(rows)

    print("First five rows:")
    print(df.head())

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nDataFrame information:")
    df.info()


if __name__ == "__main__":
    main()