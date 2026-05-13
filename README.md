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

## 🛠️ Installation & Setup

Ensure you have Python 3.8 or higher installed on your system.

### 1. Clone this Repository
```bash
git clone github.com
cd music-recommendation-system
```

### 2. Install Dependencies
Install the required packages using your terminal:
```bash
pip install numpy pandas scikit-learn streamlit
```

### 3. Add the Pre-trained Files
Ensure your project folder contains your saved model variables from your Jupyter Notebook:
- `app.py` (The web script)
- `music_recommendation_model.pkl` (The file holding your Kaggle DataFrame and Cosine Similarity matrix)

---

## 💻 How to Run

Launch the web app directly from your terminal workspace:
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

