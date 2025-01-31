from fuel import convert, gauge
import pytest


def test_convert_positive():
    assert convert("1/1") == 100
    assert convert("1/100") == 1


def test_convert_negative():
    with pytest.raises(ZeroDivisionError):
        convert("10/0")
    with pytest.raises(ValueError):
        convert("10/5")


def test_gauge_positive():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
