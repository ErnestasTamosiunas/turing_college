from seasons import validate_dob
from seasons import age_to_minutes
from seasons import convert_to_words
from datetime import date


def test_validate_dob_positive():
    assert validate_dob("2024-02-05") is True


def test_calculate_minutes():
    assert age_to_minutes(date(2000, 1, 1)) > 0
    assert age_to_minutes(date.today()) == 0


def test_convert_to_words():
    assert convert_to_words(
        525600) == "Five hundred twenty five thousand six hundred"
    assert convert_to_words(1440) == "One thousand four hundred forty"
