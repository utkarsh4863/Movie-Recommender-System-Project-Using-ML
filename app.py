import streamlit as st
import pickle
import pandas as pd
import requests
import gdown
import numpy as np
import os

# -------------------------------
# 🎬 Load Pickle Files from Google Drive
# -------------------------------
@st.cache_data(show_spinner=False)
def load_pickle_from_drive(file_id, filename):
    """
    Downloads and loads a pickle file from Google Drive using its file ID.
    """
    url = f"https://drive.google.com/uc?export=download&id={file_id}"
    if not os.path.exists(filename):
        gdown.download(url, filename, quiet=False)
    with open(filename, 'rb') as f:
        return pickle.load(f)

# ✅ Correct File IDs
MOVIES_FILE_ID = "1TGlF7hNSwigCXSnCM4uT4rp21vJQdr10"     # movies.pkl
SIMILARITY_FILE_ID = "1976olyJTylhEbS-Ua_3c6RpGdDZ94nJT"  # similarity.pkl

# ✅ Load Data
movies_dict = load_pickle_from_drive(MOVIES_FILE_ID, "movies.pkl")
movies = pd.DataFrame(movies_dict)
similarity = load_pickle_from_drive(SIMILARITY_FILE_ID, "similarity.pkl")

# ✅ Ensure similarity is numeric array
if isinstance(similarity, pd.DataFrame):
    similarity = similarity.to_numpy()
similarity = np.array(similarity, dtype=float)

# -------------------------------
# 🎥 Fetch Movie Info (Poster + Rating + Plot)
# -------------------------------
def fetch_movie_data(movie_title):
    api_key = "c88079fe"  # Your OMDb API key
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"

    try:
        response = requests.get(url)
        data = response.json()

        poster_url = (
            data.get('Poster')
            if data.get('Poster') and data.get('Poster') != "N/A"
            else "https://via.placeholder.com/500x750?text=No+Poster"
        )
        rating = data.get('imdbRating', 'N/A')
        plot = data.get('Plot', 'Plot not available.')
        if len(plot) > 180:
            plot = plot[:180] + "..."
        return {"poster": poster_url, "rating": rating, "plot": plot}

    except Exception as e:
        print("Error fetching movie data:", e)
        return {
            "poster": "https://via.placeholder.com/500x750?text=Error",
            "rating": "N/A",
            "plot": "Could not fetch plot."
        }

# -------------------------------
# 🧠 Recommendation Function
# -------------------------------
def recommend(movie):
    if movie not in movies['title'].values:
        return [], []

    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(
        list(enumerate(distances)), reverse=True, key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    movie_data_list = []

    for i in movie_list:
        movie_title = movies.iloc[i[0]].title
        recommended_movies.append(movie_title)
        movie_data_list.append(fetch_movie_data(movie_title))

    return recommended_movies, movie_data_list

# -------------------------------
# 💅 Streamlit Page Configuration
# -------------------------------
st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #FFFFFF;
    }
    h1, h2, h3, h4, h5, h6, label {
        color: #FFFFFF !important;
    }
    div[data-baseweb="select"] > div {
        background-color: #1a1c23 !important;
        color: white !important;
        border: 1px solid #F63366 !important;
    }
    div[data-baseweb="select"] span {
        color: white !important;
    }
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
        transform: scale(1.05);
        cursor: pointer;
    }
    .movie-title {
        text-align: center;
        color: #F63366;
        font-weight: 600;
        margin-top: 8px;
    }
    .movie-info {
        text-align: center;
        color: #cccccc;
        font-size: 0.9rem;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# 🏠 App Layout
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

        if not names:
            st.warning("⚠️ No recommendations found for this movie.")
        else:
            cols = st.columns(5)
            for i, col in enumerate(cols):
                with col:
                    st.image(data_list[i]["poster"], use_container_width=True)
                    st.markdown(f"<div class='movie-title'>{names[i]}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='movie-info'>⭐ IMDb: {data_list[i]['rating']}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='movie-info'>{data_list[i]['plot']}</div>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Developed with ❤️ by <b>Utkarsh Kashyap</b> using Streamlit & OMDb API</p>", unsafe_allow_html=True)
