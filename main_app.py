# main_app.py
import streamlit as st
import pandas as pd
from preprocess import load_and_preprocess
from utils_map import draw_route
from sklearn.ensemble import RandomForestRegressor

st.title("Cab Price Prediction & Route Visualizer")

# Sidebar Inputs
uploaded_file = st.sidebar.file_uploader("Upload Cab Data CSV", type=["csv"])

pickup = st.sidebar.selectbox("Select Pickup Point", [
    "Back Bay", "Beacon Hill", "Boston University", "Fenway",
    "Financial District", "Haymarket Square", "North End",
    "North Station", "Northeastern University", "South Station",
    "Theatre District", "West End"
])

drop = st.sidebar.selectbox("Select Drop Point", [
    "Back Bay", "Beacon Hill", "Boston University", "Fenway",
    "Financial District", "Haymarket Square", "North End",
    "North Station", "Northeastern University", "South Station",
    "Theatre District", "West End"
])

ride_type = st.sidebar.radio("Ride Type", ["Individual", "Shared"])

if pickup == drop:
    st.warning("Pickup and drop point cannot be the same.")

# Show Route Map
if pickup != drop:
    st.subheader("Cab Route Visualization")
    draw_route(pickup, drop)

if uploaded_file:
    X, y = load_and_preprocess(uploaded_file)

    model = RandomForestRegressor()
    model.fit(X, y)

    st.success("Model trained on uploaded data.")

    # Show predictions (for demo purposes, show the first 5 rows)
    st.subheader("Sample Predictions")
    st.write(pd.DataFrame({
        "Predicted Price": model.predict(X[:5]),
        "Actual Price": y[:5].values
    }))
