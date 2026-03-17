import pytest
from sort import sort


# --- Input validation ---
def test_negative_width_raises():
    with pytest.raises(ValueError, match="width"):
        sort(-1, 10, 10, 5)

def test_negative_mass_raises():
    with pytest.raises(ValueError, match="mass"):
        sort(10, 10, 10, -1)

def test_non_numeric_raises():
    with pytest.raises(TypeError, match="width"):
        sort("10", 10, 10, 5)

def test_none_raises():
    with pytest.raises(TypeError, match="mass"):
        sort(10, 10, 10, None)


# --- STANDARD ---
def test_standard_normal_package():
    assert sort(10, 10, 10, 5) == "STANDARD"

def test_standard_max_volume_boundary():
    # volume = 999,999 — just under bulky threshold
    assert sort(99, 101, 100, 10) == "STANDARD"  # 99*101*100 = 999,900

def test_standard_max_mass_boundary():
    # mass = 19 — just under heavy threshold
    assert sort(10, 10, 10, 19) == "STANDARD"


# --- SPECIAL: bulky only ---
def test_special_volume_exactly_1m():
    assert sort(100, 100, 100, 1) == "SPECIAL"  # volume = 1,000,000

def test_special_volume_over_1m():
    assert sort(200, 50, 100, 1) == "SPECIAL"

def test_special_dimension_exactly_150():
    assert sort(150, 1, 1, 1) == "SPECIAL"

def test_special_dimension_over_150():
    assert sort(200, 1, 1, 1) == "SPECIAL"

def test_special_height_over_150():
    assert sort(1, 200, 1, 5) == "SPECIAL"

def test_special_length_over_150():
    assert sort(1, 1, 150, 5) == "SPECIAL"

# --- SPECIAL: heavy only ---
def test_special_mass_exactly_20():
    assert sort(10, 10, 10, 20) == "SPECIAL"

def test_special_mass_over_20():
    assert sort(10, 10, 10, 50) == "SPECIAL"


# --- REJECTED: both heavy and bulky ---
def test_rejected_heavy_and_bulky_by_volume():
    assert sort(100, 100, 100, 20) == "REJECTED"

def test_rejected_heavy_and_bulky_by_dimension():
    assert sort(150, 1, 1, 20) == "REJECTED"

def test_rejected_extreme_values():
    assert sort(1000, 1000, 1000, 1000) == "REJECTED"


# --- Edge cases ---
def test_zero_mass_zero_volume():
    assert sort(0, 0, 0, 0) == "STANDARD"

def test_float_dimensions():
    # volume = 100.5 * 100.5 * 100 = ~1,010,025 — bulky
    assert sort(100.5, 100.5, 100, 5) == "SPECIAL"

def test_float_mass_just_under():
    assert sort(10, 10, 10, 19.9) == "STANDARD"

def test_float_mass_at_threshold():
    assert sort(10, 10, 10, 20.0) == "SPECIAL"
