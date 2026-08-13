import streamlit as st
import pickle
import pandas as pd
import requests

# fetch movie poster from TMDB
def fetch_posters(movie_id):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}"

    params = {
        "api_key": st.secrets["TMDB_API_KEY"],
        "language": "en-US"}

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    poster_path = data.get('poster_path')

    return "https://image.tmdb.org/t/p/w500/" + poster_path

# recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]]['id']

        recommended_movies.append(movies.iloc[i[0]]['title'])
        # fetch posters from API
        recommended_movies_posters.append(fetch_posters(movie_id))

    return (recommended_movies, recommended_movies_posters)

# load movies data
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

# load similarity matrix
similarity = pickle.load(open('similarity.pkl','rb'))

# streamlit interface
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Enter the name of the movie: ',
    movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.header(names[0])
        st.image(posters[0])
    with col2:
        st.header(names[1])
        st.image(posters[1])
    with col3:
        st.header(names[2])
        st.image(posters[2])
    with col4:
        st.header(names[3])
        st.image(posters[3])
    with col5:
        st.header(names[4])
        st.image(posters[4])