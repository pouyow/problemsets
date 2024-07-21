import pytest
from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hello,ooo") == 0

def test_h():
    assert value("hi") == 20
    assert value("Hi") == 20
    assert value("HI") == 20
    assert value("hey") == 20

def test_other():
    assert value("sssss") == 100
    assert value("LALALALA") == 100
    assert value("GOOZ") == 100
    assert value("sex?") == 100

if __name__ == "__main__":
    pytest.main()
