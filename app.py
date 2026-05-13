import pandas as pd
import streamlit as st
import pickle


with open('music_recommendation_model.pkl', 'rb') as f:
    music, cosine_sim = pickle.load(f)

def get_recommendations(track_name, cosine_sim=cosine_sim):
  idx = music[music['track_name'] == track_name].index[0]
  sim_scores = list(enumerate(cosine_sim[idx])) # to iterate through a sequence and also keep track of the index of each item
  sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
  sim_scores = sim_scores[1:11] # Get top 10 similar music
  music_indices = [i[0] for i in sim_scores] # extract the music_indices
  return music[['track_name', 'artist_name']].iloc[music_indices]


st.title('Music Recommendation System')
st.write('Enter a track name to get music recommendations.')
track_name = st.selectbox('Select a song:', music['track_name'].tolist())
if st.button('Get Recommendations'):
    recommendations = get_recommendations(track_name)
    st.write(recommendations)