# Pokémon Type Checker

A beginner Python and Streamlit app for calculating Generation I Pokémon type effectiveness and Same-Type Attack Bonus (STAB).

## Features

- Uses the 15 Generation I Pokémon types
- Supports single- and dual-type attackers
- Supports single- and dual-type defenders
- Calculates defensive type effectiveness
- Applies the Generation I 1.5× STAB multiplier automatically
- Prevents duplicate attacker or defender types
- Shows the final damage multiplier
- Provides an expandable calculation breakdown
- Uses automated tests with pytest

The calculator assumes an ordinary damaging move using standard Generation I type-effectiveness and STAB rules. Fixed-damage moves and other unusual moves may not follow the displayed calculation.

## Project Structure

- `app.py` — Streamlit user interface
- `model.py` — type matchup and calculation logic
- `test_model.py` — automated tests
- `data/type_chart.csv` — Generation I type-effectiveness data
- `requirements.txt` — Python package dependencies

## Run the App

Activate the project environment, then run:

```bash
streamlit run app.py