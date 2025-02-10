from plates import is_valid


def test_positive():
    assert is_valid("CS50") is True


def test_negative():
    assert is_valid("CS..50") is False
    assert is_valid("12345") is False
    assert is_valid("CS50S") is False
    assert is_valid("12TEST") is False
    assert is_valid("CS50000") is False
    assert is_valid("CS00") is False
