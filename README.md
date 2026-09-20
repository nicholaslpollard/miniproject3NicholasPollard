# Mini Project 3 - Movie Ratings by Genre

INF601 - Advanced Programming in Python  
Nicholas Pollard

## Project Question

How do movie ratings compare across genres, and which genre has the highest average rating?

## Data Source

This project uses the FHSU Practice Hub sanctioned movies dataset:

https://practice.fhsucyber.com/api/v1/datasets/movies

The program requests 100 movie records from the API and loads them into a Pandas DataFrame. Each record includes:

- title
- director
- year
- genre
- rating

## What the Program Does

`miniproject3.py` does the following:

1. Sends an authenticated request to the Practice Hub API and retrieves 100 movie records.
2. Loads the records into a Pandas DataFrame and checks that all of the expected columns are present.
3. Groups the movies by genre and calculates the average rating for each genre using Pandas.
4. Sorts the genres from highest to lowest average rating.
5. Prints an analysis to the terminal, including how many movies were analyzed, the average rating and movie count for each genre, and which genre has the highest average rating.
6. Generates two charts and saves them to the `charts/` folder.

## The Analysis

The core of the analysis uses a Pandas `groupby`:

```python
genre_averages = df.groupby("genre")["rating"].mean().sort_values(ascending=False)