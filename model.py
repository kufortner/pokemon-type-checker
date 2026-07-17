"""
Lookup logic for the Pokémon Type Matchup Checker.

Version: 1.0.0
"""

from pathlib import Path

import pandas as pd


DATA_FILE = Path(__file__).parent / "data" / "type_chart.csv"


def load_type_chart() -> pd.DataFrame:
    """
    Load the Pokémon type matchup chart from the CSV file.

    Returns:
        A pandas DataFrame containing attacking types,
        defending types, and damage multipliers.
    """
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Type chart file was not found at: {DATA_FILE}"
        )

    chart = pd.read_csv(DATA_FILE)

    required_columns = {
        "attacking_type",
        "defending_type",
        "multiplier",
    }

    missing_columns = required_columns - set(chart.columns)

    if missing_columns:
        raise ValueError(
            f"The type chart is missing required columns: "
            f"{sorted(missing_columns)}"
        )

    return chart


def get_matchup(attacking_type: str, defending_type: str) -> float:
    """
    Return the damage multiplier for one attacking and defending type.

    Args:
        attacking_type: The attacking Pokémon type.
        defending_type: The defending Pokémon type.

    Returns:
        The damage multiplier as a float.

    Raises:
        ValueError: If the requested matchup is missing or duplicated.
    """
    chart = load_type_chart()

    matching_rows = chart[
        (chart["attacking_type"] == attacking_type)
        & (chart["defending_type"] == defending_type)
    ]

    if matching_rows.empty:
        raise ValueError(
            f"No matchup was found for "
            f"{attacking_type} attacking {defending_type}."
        )

    if len(matching_rows) > 1:
        raise ValueError(
            f"Duplicate matchup rows were found for "
            f"{attacking_type} attacking {defending_type}."
        )

    return float(matching_rows.iloc[0]["multiplier"])
