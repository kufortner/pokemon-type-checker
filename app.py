import streamlit as st
import matplotlib.pyplot as plt

from model import get_chart_values

st.title("Pokémon Type Checker")
selected_type = st.selectbox(
    "Choose a Pokémon type:",
    ["Fire", "Water", "Grass"],
)
st.write("You selected:", selected_type)

chart_values = get_chart_values(selected_type)

fig, ax = plt.subplots()
ax.bar(
    ["Grass", "Normal", "Water", "Fire"],
    chart_values,
)
ax.set_title(f"{selected_type} Attack Effectiveness")
ax.set_ylabel("Damage multiplier")
st.pyplot(fig)