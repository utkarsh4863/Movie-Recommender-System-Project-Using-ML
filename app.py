import streamlit as st
import pickle
import pandas as pd
import requests

# -------------------------------
# Load Data
# -------------------------------
movies_dict = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

# -------------------------------
# Fetch Movie Info (Poster + Rating + Plot) via OMDb API
# -------------------------------
def fetch_movie_data(movie_title):
    api_key = "c88079fe"  # ✅ Your OMDb API key
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"

    try:
        response = requests.get(url)
        data = response.json()

        poster_url = data.get('Poster') if data.get('Poster') and data.get('Poster') != "N/A" else "https://via.placeholder.com/500x750?text=No+Poster"
        rating = data.get('imdbRating', 'N/A')
        plot = data.get('Plot', 'Plot not available.')

        if len(plot) > 180:
            plot = plot[:180] + "..."

        return {"poster": poster_url, "rating": rating, "plot": plot}
    except Exception as e:
        print("Error fetching movie data:", e)
        return {"poster": "https://via.placeholder.com/500x750?text=Error", "rating": "N/A", "plot": "Could not fetch plot."}

# -------------------------------
# Recommend Function
# -------------------------------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    movie_data_list = []

    for i in movie_list:
        movie_title = movies.iloc[i[0]].title
        recommended_movies.append(movie_title)
        movie_data_list.append(fetch_movie_data(movie_title))

    return recommended_movies, movie_data_list

# -------------------------------
# Streamlit UI Design
# -------------------------------
st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")

# ✅ Dark Theme but readable
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #FFFFFF;
    }
    /* Headings and labels */
    h1, h2, h3, h4, h5, h6, label {
        color: #FFFFFF !important;
    }

    /* Dropdown box */
    div[data-baseweb="select"] > div {
        background-color: #1a1c23 !important;
        color: white !important;
        border: 1px solid #F63366 !important;
    }

    /* Dropdown text */
    div[data-baseweb="select"] span {
        color: white !important;
    }

    /* Recommend Button */
    div.stButton > button:first-child {
        background-color: #F63366;
        color: white;
        border: none;
        padding: 0.6rem 1.2rem;
        border-radius: 10px;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        background-color: #ff4b77;
        color: white;
        transform: scale(1.05);
        cursor: pointer;
    }

    /* Movie Titles */
    .movie-title {
        text-align: center;
        color: #F63366;
        font-weight: 600;
        margin-top: 8px;
    }

    /* Plot + Rating */
    .movie-info {
        text-align: center;
        color: #cccccc;
        font-size: 0.9rem;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# Page Title
# -------------------------------
st.markdown("<h1 style='text-align: center; color: #F63366;'>🎥 Movie Recommendation System</h1>", unsafe_allow_html=True)
st.write("### Get personalized movie recommendations based on your favorite movie!")

selected_movie_name = st.selectbox(
    '🎬 Select or type a movie name:',
    movies['title'].values
)

if st.button('Recommend 🎬'):
    with st.spinner('Fetching similar movies...'):
        names, data_list = recommend(selected_movie_name)

        cols = st.columns(5)
        for i, col in enumerate(cols):
            with col:
                st.image(data_list[i]["poster"], use_container_width=True)
                st.markdown(f"<div class='movie-title'>{names[i]}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='movie-info'>⭐ IMDb: {data_list[i]['rating']}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='movie-info'>{data_list[i]['plot']}</div>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Developed with ❤️ using Streamlit & OMDb API</p>", unsafe_allow_html=True)

