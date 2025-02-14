from jar import Jar
import pytest


def test_init():
    jar = Jar()
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"


def test_deposit_positive():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5


def test_deposit_negative():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(14)


def test_withdraw_positive():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2


def test_withdraw_negative():
    jar = Jar()
    jar.deposit(5)
    with pytest.raises(ValueError):
        jar.withdraw(6)
