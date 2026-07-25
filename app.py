import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

type_data = pd.read_csv("data/type_effectiveness.csv")

st.title("Pokémon Type Checker")
selected_type = st.selectbox(
    "Choose a Pokémon type:",
    ["Fire", "Water", "Grass"],
)
st.write("You selected:", selected_type)

selected_row = type_data[
    type_data["attacking_type"] == selected_type
]

chart_values = selected_row[
    ["Grass", "Normal", "Water", "Fire"]
].iloc[0].tolist()

fig, ax = plt.subplots()
ax.bar(
    ["Grass", "Normal", "Water", "Fire"],
    chart_values,
)
ax.set_title(f"{selected_type} Attack Effectiveness")
ax.set_ylabel("Damage multiplier")
st.pyplot(fig)