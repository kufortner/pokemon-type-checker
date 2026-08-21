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


def get_available_types() -> list[str]:
    """Return all available Pokémon types in alphabetical order."""
    chart = load_type_chart()

    return sorted(chart["attacking_type"].unique().tolist())

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

def get_defensive_multiplier(
    attacking_type: str,
    defender_type_1: str,
    defender_type_2: str | None = None,
) -> float:
    """Return the combined multiplier against one or two defender types."""
    multiplier = get_matchup(attacking_type, defender_type_1)

    if defender_type_2 is not None:
        multiplier *= get_matchup(
            attacking_type,
            defender_type_2,
        )

    return multiplier

def get_stab_multiplier(
    attack_type: str,
    attacker_type_1: str,
    attacker_type_2: str | None = None,
) -> float:
    """Return the Generation I Same-Type Attack Bonus multiplier."""
    attacker_types = [attacker_type_1, attacker_type_2]

    if attack_type in attacker_types:
        return 1.5

    return 1.0

def calculate_final_multiplier(
    attack_type: str,
    attacker_type_1: str,
    defender_type_1: str,
    attacker_type_2: str | None = None,
    defender_type_2: str | None = None,
) -> float:
    """Return defensive effectiveness multiplied by STAB."""
    defensive_multiplier = get_defensive_multiplier(
        attack_type,
        defender_type_1,
        defender_type_2,
    )

    stab_multiplier = get_stab_multiplier(
        attack_type,
        attacker_type_1,
        attacker_type_2,
    )

    return defensive_multiplier * stab_multiplier

def get_calculation_breakdown(
    attack_type: str,
    attacker_type_1: str,
    defender_type_1: str,
    attacker_type_2: str | None = None,
    defender_type_2: str | None = None,
) -> dict:
    """Return the individual multipliers used in the calculation."""
    defender_1_multiplier = get_matchup(
        attack_type,
        defender_type_1,
    )

    defender_2_multiplier = None

    if defender_type_2 is not None:
        defender_2_multiplier = get_matchup(
            attack_type,
            defender_type_2,
        )

    defensive_multiplier = get_defensive_multiplier(
        attack_type,
        defender_type_1,
        defender_type_2,
    )

    stab_multiplier = get_stab_multiplier(
        attack_type,
        attacker_type_1,
        attacker_type_2,
    )

    final_multiplier = defensive_multiplier * stab_multiplier

    return {
        "defender_1_multiplier": defender_1_multiplier,
        "defender_2_multiplier": defender_2_multiplier,
        "defensive_multiplier": defensive_multiplier,
        "stab_multiplier": stab_multiplier,
        "final_multiplier": final_multiplier,
    }