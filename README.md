# Movie-Recommender-System-Project-Using-ML

# 🎬 Movie Recommender System Using Machine Learning

A **content-based movie recommendation system** built with **Python, Streamlit**, and **OMDb API**, which suggests similar movies based on your favorite one.  
This project uses **cosine similarity** on text features such as genres, cast, crew, keywords, and overview.

---

## 🚀 Live Demo  
🔗 [Click here to view on Streamlit Cloud](#) *(Add your Streamlit URL after deployment)*

---

## 📦 Features
✅ Movie recommendations based on similarity  
✅ Fetches **posters, IMDb ratings, and plots** using the **OMDb API**  
✅ Built with a clean and responsive **Streamlit UI**  
✅ Uses **Pickle files** for model and similarity data  
✅ Simple to deploy — no database needed  

---

## 🧠 Tech Stack
| Component | Technology |
|------------|-------------|
| Frontend | Streamlit |
| Backend | Python |
| ML Algorithm | Cosine Similarity |
| API | OMDb API |
| Data Source | TMDB 5000 Dataset (Kaggle) |

---

## ⚙️ Installation Guide

### 1️⃣ Clone this repository
```bash
git clone https://github.com/utkarsh4863/Movie-Recommender-System-Project-Using-ML.git
cd Movie-Recommender-System-Project-Using-ML

---

### 2️⃣ Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate    # For Windows

---

3️⃣ Install dependencies
```bash
pip install -r requirements.txt

---

4️⃣ Run the Streamlit app
```bash
streamlit run app.py

---

## 🔑 API Setup

This project uses the OMDb API to fetch posters, plots, and IMDb ratings.

Get your API key from: https://www.omdbapi.com/apikey.aspx

Replace your key in the code:

api_key = "your_api_key_here"

---

## 📊 Dataset Used

The project is based on the TMDB 5000 Movies Dataset from Kaggle:
🔗 https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

---

## 🖥️ Screenshots
Home Page	Recommendations

---
	
## 📁 Project Structure
├── app.py
├── movies.pkl
├── similarity.pkl
├── requirements.txt
├── README.md
└── Movies/
    ├── tmdb_5000_movies.csv
    └── tmdb_5000_credits.csv

---

## ❤️ Developed By

Utkarsh Kashyap
📧 Feel free to connect on GitHub


