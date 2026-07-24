import streamlit as st
import matplotlib.pyplot as plt

st.title("Pokémon Type Checker")
selected_type = st.selectbox(
    "Choose a Pokémon type:",
    ["Fire", "Water", "Grass"],
)
st.write("You selected:", selected_type)

effectiveness = {
    "Fire": [2.0, 1.0, 0.5, 0.5],
    "Water": [0.5, 1.0, 2.0, 2.0],
    "Grass": [0.5, 1.0, 0.5, 2.0],
}

fig, ax = plt.subplots()
ax.bar(
    ["Grass", "Normal", "Water", "Fire"],
    effectiveness[selected_type],
)
ax.set_title(f"{selected_type} Attack Effectiveness")
ax.set_ylabel("Damage multiplier")
st.pyplot(fig)