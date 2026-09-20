# INF601 - Advanced Programming in Python
# Nicholas Pollard
# Mini Project 3

import os

import matplotlib.pyplot as plt
import pandas as pd
import requests


BASE_URL = "https://practice.fhsucyber.com"
CHARTS_DIR = "charts"
REQUIRED_COLUMNS = ["title", "director", "year", "genre", "rating"]


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

    missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Dataset is missing required columns: {missing_columns}")

    # average rating per genre, sorted highest to lowest
    genre_averages = df.groupby("genre")["rating"].mean().sort_values(ascending=False)

    # number of movies in each genre
    genre_counts = df["genre"].value_counts()

    top_genre = genre_averages.index[0]

    print(f"Movies analyzed: {len(df)}")
    print("\nAverage rating by genre:")

    for genre, avg_rating in genre_averages.items():
        print(
            f"  {genre}: {avg_rating:.2f} "
            f"({genre_counts[genre]} movies)"
        )

    print(
        f"\nHighest average rating: "
        f"{top_genre} ({genre_averages.iloc[0]:.2f})"
    )

    os.makedirs(CHARTS_DIR, exist_ok=True)

    make_bar_chart(genre_averages)
    make_box_plot(df, genre_averages.index)


def make_bar_chart(genre_averages):
    fig, ax = plt.subplots(figsize=(8, 5))

    bars = ax.bar(
        genre_averages.index,
        genre_averages.values,
        color="steelblue"
    )

    ax.bar_label(bars, fmt="%.2f", padding=3)

    ax.set_title("Average Movie Rating by Genre")
    ax.set_xlabel("Genre")
    ax.set_ylabel("Average Rating")
    ax.set_ylim(0, 10)
    ax.tick_params(axis="x", rotation=30)

    fig.tight_layout()

    fig.savefig(
        os.path.join(CHARTS_DIR, "average_rating_by_genre.png")
    )

    plt.close(fig)


def make_box_plot(df, genre_order):
    ratings_by_genre = [
        df.loc[df["genre"] == genre, "rating"]
        for genre in genre_order
    ]

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.boxplot(
        ratings_by_genre,
        tick_labels=genre_order
    )

    ax.set_title("Distribution of Movie Ratings by Genre")
    ax.set_xlabel("Genre")
    ax.set_ylabel("Rating")
    ax.tick_params(axis="x", rotation=30)

    fig.tight_layout()

    fig.savefig(
        os.path.join(CHARTS_DIR, "rating_distribution_by_genre.png")
    )

    plt.close(fig)


if __name__ == "__main__":
    main()