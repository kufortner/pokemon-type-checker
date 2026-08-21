from model import (
    get_matchup,
    get_defensive_multiplier,
    get_stab_multiplier,
    calculate_final_multiplier,
)


def test_normal_single_type_matchup():
    assert get_matchup("Fire", "Grass") == 2.0

def test_dual_type_defensive_multiplier():
    assert get_defensive_multiplier("Electric", "Water", "Flying") == 4.0

def test_stab():
    assert get_stab_multiplier("Electric", "Electric", None) == 1.5

def test_no_stab():
    assert get_stab_multiplier("Normal", "Electric", None) == 1.0

def test_immunity():
    assert get_defensive_multiplier("Electric", "Ground", None) == 0.0

def test_zapdos_example():
    assert calculate_final_multiplier(
        "Electric",
        "Electric",
        "Electric",
        "Flying",
        "Flying",
    ) == 1.5

def test_gen1_ghost_vs_psychic():
    assert get_matchup("Ghost", "Psychic") == 0.0