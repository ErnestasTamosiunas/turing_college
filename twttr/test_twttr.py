from twttr import shorten
import pytest


def test_string():
    assert shorten("Twitter") == "Twttr"
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("12345") == "12345"


def test_punctuation():
    assert shorten("Twitter, twitter....") == "Twttr, twttr...."


def test_int():
    with pytest.raises(TypeError):
        shorten(500)
