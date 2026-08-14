# Movie Recommender System

A content-based **Movie Recommender System** built with Python and Streamlit. Users can select a movie and receive the **top 5 similar movie recommendations**, along with movie posters fetched from the TMDB API.


## Project Aim

The aim of this project is to build an interactive application that helps users discover movies similar to a movie they already like.

The system uses processed movie data and a pre-computed similarity matrix to identify similar movies using content-based filtering. Streamlit provides the interactive interface, while the TMDB API provides movie poster information.


## Features

- Select a movie from an interactive dropdown.
- Generate the **Top 5 similar movie recommendations**.
- Display recommended movie titles.
- Fetch movie posters using the TMDB API.
- Interactive web interface built with Streamlit.


## How It Works

The project follows a **content-based recommendation approach**.

```text
Movie Dataset
     |
Data Preprocessing
     |
Movie Features
     |
Similarity Calculation
     |
Similarity Matrix
     |
User Selects a Movie
     |
Find Selected Movie
     |
Compare Similarity Scores
     |
Top 5 Similar Movies
     |
Fetch Posters from TMDB
     |
Display Recommendations
```
When a user selects a movie, the application finds its index, retrieves its similarity scores, sorts movies by similarity, selects the top five results, and fetches their posters from TMDB.

## Technologies Used

### Programming Language:

- Python
  - Pandas - data manipulation
  - Pickle - loading processed movie data and the similarity matrix
  - Requests - TMDB API requests

- Streamlit
  - TMDB API - movie poster information


## Project Structure

```text
Movie-Recommender-System/
|
|-- .streamlit/
|   `-- secrets.toml          # Local API secrets - DO NOT upload
|
|-- app.py                    # Main Streamlit application
|-- movies_dict.pkl           # Processed movie data
|-- similarity.pkl            # Pre-computed similarity matrix
|-- tmdb_5000_movies.csv      # Movie dataset
|-- tmdb_5000_credits.csv     # Movie credits dataset
|-- requirements.txt          # Python dependencies
|-- .gitignore                # Git exclusions
|-- Procfile                  # Existing deployment configuration
`-- setup.sh                  # Existing setup script
```


## Future Enhancements

- Add genre and metadata filters.
- Display ratings, release year, cast, and descriptions.
- Add a search feature instead of only a dropdown.
- Allow users to rate movies and generate personalized recommendations.
- Add collaborative filtering.
- Improve the recommendation algorithm with additional movie features.
- Add caching for repeated TMDB requests.


## Limitations

- The current system is based on movie similarity rather than individual user rating history.
- Poster retrieval depends on TMDB API availability.
- Network or API failures can prevent posters from loading.

## License

This project is intended for educational and portfolio purposes. Review the terms and attribution requirements of the datasets and APIs used before redistributing underlying data.



















