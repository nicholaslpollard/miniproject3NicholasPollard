# Mini Project 3 - Movie Ratings by Genre

INF601 - Advanced Programming in Python  
Nicholas Pollard

## What this project does

This project uses the FHSU Practice Hub movies dataset to compare movie ratings across different genres. The question I wanted to answer was which movie genre has the highest average rating.

The program retrieves 100 movie records from the Practice Hub API and stores the data in a Pandas DataFrame. The dataset includes the movie title, director, year, genre, and rating.

Pandas is used to group the movies by genre and calculate the average rating for each group. The program also counts how many movies are included in each genre.

For this sample, Horror had the highest average rating at 5.97.

The program creates two charts using Matplotlib:

- `average_rating_by_genre.png` - shows the average rating for each genre and displays the exact average above each bar
- `rating_distribution_by_genre.png` - shows how the individual movie ratings are distributed within each genre

The charts are saved as PNG files in the `charts/` folder when the program runs.

## Setup

### 1. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install the requirements

```powershell
pip install -r requirements.txt
```

### 3. Set the Practice Hub API token

The program uses the `PRACTICE_API_TOKEN` environment variable to access the Practice Hub API.

In PowerShell, set the token with:

```powershell
$env:PRACTICE_API_TOKEN = "your-token-here"
```

The token is not stored in the GitHub repository.

## Running the program

With the virtual environment activated and the API token set, run:

```powershell
python miniproject3.py
```

The program will print the number of movies analyzed, the average rating and movie count for each genre, and the genre with the highest average rating.

It will also create two PNG charts inside the `charts/` folder.

The `charts/` folder is included in `.gitignore`, so the generated chart files are not stored in the GitHub repository.

## Project files

- `miniproject3.py` - main Python program
- `requirements.txt` - required Python packages
- `.gitignore` - excludes the virtual environment, generated charts, local environment files, and Python cache files
- `README.md` - project information and setup instructions

## AI Usage

### Claude was used for

I used Claude Code to help build the main Pandas analysis, create the Matplotlib charts, add basic data validation, and troubleshoot and test the program.

### What I did myself

I created the project environment and GitHub repository, installed the required packages, connected to and tested the Practice Hub API, wrote the initial DataFrame inspection code, reviewed and tested the completed program, and worked through the Git process.

### What I changed

After reviewing the AI-generated code, I added the exact average rating above each bar in the average rating chart. I also added the number of movies in each genre to the terminal output so the results provide more context.
