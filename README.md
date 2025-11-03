# 🎬 Movie Recommender System Using Machine Learning

A **content-based movie recommendation system** built with **Python, Streamlit**, and **OMDb API** that suggests similar movies based on your favorite selection. The system uses **cosine similarity** on text features including genres, cast, crew, keywords, and overview.

---

## 🚀 Live Demo
🔗 [View on Streamlit Cloud](#) *(Add your Streamlit URL after deployment)*

---

## 📦 Features

- 🎯 **Smart Recommendations** - Get movie suggestions based on content similarity
- 🖼️ **Rich Metadata** - Fetches posters, IMDb ratings, and plots via OMDb API
- 💻 **Clean UI** - Built with responsive Streamlit interface
- 📊 **Efficient Processing** - Uses pickle files for fast model loading
- 🚀 **Easy Deployment** - No database required, simple to set up

---

## 🧠 Tech Stack

| Component | Technology |
|-----------|------------|
| **Frontend** | Streamlit |
| **Backend** | Python |
| **ML Algorithm** | Cosine Similarity |
| **API** | OMDb API |
| **Data Source** | TMDB 5000 Dataset (Kaggle) |

---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/utkarsh4863/Movie-Recommender-System-Project-Using-ML.git
cd Movie-Recommender-System-Project-Using-ML
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate # macOS/Linux
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application
```bash
streamlit run app.py
```

---

## 🔑 API Setup

This project requires the **OMDb API** for fetching movie metadata.

1. Get your free API key from: [https://www.omdbapi.com/apikey.aspx](https://www.omdbapi.com/apikey.aspx)
2. Replace the placeholder in your code:
```python
api_key = "your_api_key_here"
```

---

## 📊 Dataset

The project uses the **TMDB 5000 Movies Dataset** from Kaggle:

🔗 [TMDB Movie Metadata](https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)

**Dataset includes:**
- Movie titles, genres, and keywords
- Cast and crew information
- Movie overviews and metadata

---

## 🖥️ Screenshots


![Home Page](https://raw.githubusercontent.com/utkarsh4863/Movie-Recommender-System-Project-Using-ML/main/Screenshot%202025-11-03%20232229.png)
---

## 📁 Project Structure
```
Movie-Recommender-System-Project-Using-ML/
│
├── app.py                      # Main Streamlit application
├── movies.pkl                  # Serialized movie data
├── similarity.pkl              # Precomputed similarity matrix
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
│
└── Movies/
    ├── tmdb_5000_movies.csv   # Movie dataset
    └── tmdb_5000_credits.csv  # Credits dataset
```

---

## 🛠️ How It Works

1. **Data Processing** - Movie features (genres, cast, keywords, overview) are extracted and combined
2. **Vectorization** - Text data is converted into numerical vectors
3. **Similarity Calculation** - Cosine similarity is computed between all movie pairs
4. **Recommendation** - When a user selects a movie, the system returns the most similar movies
5. **Enrichment** - Movie metadata is fetched from OMDb API for enhanced display

---

## 🚀 Future Enhancements

- [ ] Add collaborative filtering for personalized recommendations
- [ ] Implement user ratings and watchlist functionality
- [ ] Include trailer links and streaming availability
- [ ] Add advanced filters (year, genre, rating)
- [ ] Create a recommendation explanation feature

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## ❤️ Developed By

**Utkarsh Kashyap**

[![GitHub](https://img.shields.io/badge/GitHub-utkarsh4863-black?style=flat&logo=github)](https://github.com/utkarsh4863)




