import numb3rs


def test_positive_ip():
    assert numb3rs.validate("1.2.3.4") is True
    assert numb3rs.validate("255.255.255.255") is True


def test_negative_ip():
    assert numb3rs.validate("cat") is False
    assert numb3rs.validate("275.355.555.655") is False
    assert numb3rs.validate("0.355.0.6") is False
    assert numb3rs.validate("1.2.3.4.5") is False
