from bank import value


def test_starts_with_hello():
    assert value("Hello") == 0
    assert value("Hello, Newman") == 0


def test_starts_with_h():
    assert value("hi") == 20
    assert value("how are you?") == 20
    assert value("HOLA") == 20


def test_anything_else():
    assert value("good morning") == 100
    assert value("What's up?") == 100
    assert value("CS50") == 100
