# 🎵 Music Recommendation System

An interactive web application built with **Streamlit** that suggests 10 similar songs based on a user's selection. This project adapts the core machine learning concepts from a **Movie Recommendation System tutorial** and reimagines them to work with a **Kaggle Music Dataset**.

---

## 💡 Project Origin & References

- **The Dataset:** Sourced from the [Kaggle Spotify Global Music Dataset (2009-2025)](https://www.kaggle.com/datasets/wardabilal/spotify-global-music-dataset-20092025).
- **The Inspiration:** Built by modifying and expanding the architecture shown in this [YouTube Movie Recommendation System Tutorial](https://youtu.be/i-B_I2DGIAI?si=0lqicw9GNnvmu7xX).
- **The Adaptation:** While movie datasets usually have unique titles, music datasets contain identical song names from different artists. The codebase adapts the tutorial's logic to retrieve the proper row vectors while keeping the core mathematical workflow intact.

---

## 🚀 Features

- **Dropdown Search:** Quickly scan through the entire Kaggle music library using a clean Streamlit selectbox.
- **Cosine Similarity Engine:** Analyzes preprocessed song vector features to compute musical distance.
- **Pickled Model Fast-loading:** Uses Python's `pickle` module to load data arrays instantly without reprocessing the dataset on every click.

---

## 📦 Environment & Data Serialization
To keep the repository lightweight and professional, we use a virtual environment and pre-computed model files. Note that these are excluded from GitHub via .gitignore.

1. **The Virtual Environment (.venv/)**
- A local folder containing the project's specific Python interpreter and libraries (Streamlit, Pandas, etc.).
- It ensures isolation. This prevents conflicts between project dependencies and keeps the environment consistent for every developer.
- These folders are massive and system-specific. Instead, we use requirements.txt so you can recreate the environment locally.

2. **Pickle Files (.pkl)**
- Binary "snapshots" of our processed music DataFrame and the heavy Cosine Similarity matrix.
- Speed. Calculating musical "distance" for thousands of tracks is math-intensive. By "pickling" the results, the app loads the answers instantly without recalculating on every refresh.
- These matrices often exceed 100MB (GitHub’s limit). You generate these locally by running the processing script.

---
## 💻 How to Run

1) Setup Environment:
```bash
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows
pip install streamlit pandas numpy scikit-learn
```

2) Launch the web app directly from your terminal workspace:
```bash
streamlit run app.py
```
The app will instantly launch a local server and open your interface at `http://localhost:8501`.

---

## 🧠 Behind the Code: How it Works

1. **Pickle Extraction:** The application loads a saved tuple containing the Kaggle pandas DataFrame (`music`) and the similarity array (`cosine_sim`).
2. **Index Lookup:** When a song is selected, the application extracts its structural row index number (`.index`).
3. **Similarity Mapping:** It grabs that specific row index vector out of the `cosine_sim` matrix and uses `enumerate()` to map similarity values to their respective song positions.
4. **Descending Sort:** The list is sorted from highest similarity score to lowest.
5. **Top 10 Slice:** It skips the first item (the song itself) and slices the next 10 items (`[1:11]`) to return the recommended track names and artists.

