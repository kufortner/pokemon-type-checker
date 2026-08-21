import streamlit as st

from model import get_available_types, get_calculation_breakdown


st.title("Pokémon Type Checker")

types = get_available_types()
optional_types = ["None"] + types

attack_type = st.selectbox(
    "Attack type:",
    types,
)

left_column, right_column = st.columns(2)

with left_column:
    st.subheader("Attacker")

    attacker_type_1 = st.selectbox(
        "Attacker type 1:",
        types,
    )

    attacker_type_2 = st.selectbox(
        "Attacker type 2:",
        optional_types,
    )

with right_column:
    st.subheader("Defender")

    defender_type_1 = st.selectbox(
        "Defender type 1:",
        types,
    )

    defender_type_2 = st.selectbox(
        "Defender type 2:",
        optional_types,
    )

attacker_type_2_value = (
    None if attacker_type_2 == "None" else attacker_type_2
)

defender_type_2_value = (
    None if defender_type_2 == "None" else defender_type_2
)

has_duplicate_attacker_types = (
    attacker_type_2_value == attacker_type_1
)

has_duplicate_defender_types = (
    defender_type_2_value == defender_type_1
)

if has_duplicate_attacker_types:
    st.error("Attacker type 1 and type 2 must be different.")

if has_duplicate_defender_types:
    st.error("Defender type 1 and type 2 must be different.")

if not (
    has_duplicate_attacker_types
    or has_duplicate_defender_types
):
    breakdown = get_calculation_breakdown(
        attack_type=attack_type,
        attacker_type_1=attacker_type_1,
        attacker_type_2=attacker_type_2_value,
        defender_type_1=defender_type_1,
        defender_type_2=defender_type_2_value,
    )

    st.subheader("Final damage multiplier")

    st.metric(
        "Final multiplier",
        f"{breakdown['final_multiplier']}×",
    )

    with st.expander("Calculation breakdown"):
        st.write(
            f"{attack_type} vs {defender_type_1}: "
            f"{breakdown['defender_1_multiplier']}×"
        )

        if defender_type_2_value is not None:
            st.write(
                f"{attack_type} vs {defender_type_2_value}: "
                f"{breakdown['defender_2_multiplier']}×"
            )

        st.write(
            "Combined defensive multiplier:",
            f"{breakdown['defensive_multiplier']}×",
        )

        if breakdown["stab_multiplier"] == 1.5:
            st.write(
                f"STAB applied because {attack_type} matches "
                "one of the attacker’s types: 1.5×"
            )
        else:
            st.write(
                f"No STAB because {attack_type} does not match "
                "either attacker type: 1.0×"
            )

        st.write(
            "Final calculation:",
            f"{breakdown['defensive_multiplier']} × "
            f"{breakdown['stab_multiplier']} = "
            f"{breakdown['final_multiplier']}×",
        )

    st.info(
        "This calculator assumes an ordinary damaging move using the "
        "standard Generation I type-effectiveness and STAB rules. "
        "Fixed-damage moves, such as Dragon Rage, which always deals "
        "40 HP of damage, and other unusual moves may not follow "
        "this calculation."
    )