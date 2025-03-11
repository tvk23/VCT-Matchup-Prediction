#Tyrelle V. Kelley II

import streamlit as st
import pandas as pd
import numpy as np
import random



# Dictionary of VCT Americas teams and their average ACS
teams = {
    "LOUD": 9.5,
    "Evil Geniuses": 9.2,
    "NRG": 9.0,
    "Sentinels": 8.8,
    "100 Thieves": 8.7,
    "Cloud9": 8.6,
    "FURIA": 8.5,
    "KRÜ Esports": 8.4,
    "MIBR": 8.3,
    "Leviatán": 8.2,
    "T1": 8.1,
}

def calculate_win_probability(team1_rating, team2_rating):
    """Calculate win probability using Elo-like formula"""
    rating_diff = team1_rating - team2_rating
    probability = 1 / (1 + 10 ** (-rating_diff / 4))
    return probability

st.title("VCT Americas Team Matchup Predictor")
st.write("Compare two teams and see their predicted win probabilities!")

# Create two columns for team selection
col1, col2 = st.columns(2)

with col1:
    team1 = st.selectbox("Select Team 1", list(teams.keys()), key="team1")
    st.write(f"Power Rating: {teams[team1]}")

with col2:
    team2 = st.selectbox("Select Team 2", list(teams.keys()), key="team2")
    st.write(f"Power Rating: {teams[team2]}")

if st.button("Calculate Matchup"):
    if team1 != team2:
        prob_team1 = calculate_win_probability(teams[team1], teams[team2])
        prob_team2 = 1 - prob_team1

        st.write("---")
        st.write("### Predicted Win Probabilities")
        
        # Display probabilities with progress bars
        st.write(f"{team1}")
        st.progress(prob_team1)
        st.write(f"{prob_team1:.1%}")
        
        st.write(f"{team2}")
        st.progress(prob_team2)
        st.write(f"{prob_team2:.1%}")
    else:
        st.error("Please select different teams to compare!")
