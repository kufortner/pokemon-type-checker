import streamlit as st

st.title("Pokémon Type Checker")
selected_type = st.selectbox(
    "Choose a Pokémon type:",
    ["Fire", "Water", "Grass"],
)
st.write("You selected:", selected_type)
