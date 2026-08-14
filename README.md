
```text
root
├── app.py
├── movies_dict.pkl
├── similarity.pkl
├── movies.pkl
├── .gitignore 
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
├── Procfile
├── setup.sh
└── requirements.txt
```
# Movie Recommender System

A content-based **Movie Recommender System** built with Python and Streamlit. Users can select a movie and receive the **top 5 similar movie recommendations**, along with movie posters fetched from the TMDB API.

---

## Project Aim

The aim of this project is to build an interactive application that helps users discover movies similar to a movie they already like.

The system uses processed movie data and a pre-computed similarity matrix to identify similar movies using content-based filtering. Streamlit provides the interactive interface, while the TMDB API provides movie poster information.

---

## Features

- Select a movie from an interactive dropdown.
- Generate the **Top 5 similar movie recommendations**.
- Display recommended movie titles.
- Fetch movie posters using the TMDB API.
- Interactive web interface built with Streamlit.

---

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

- Streamlit - interactive web application
  - TMDB API - movie poster information
