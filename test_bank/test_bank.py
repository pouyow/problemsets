import pytest
from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hello, world") == 0

def test_h():
    assert value("hi") == 20
    assert value("Hi") == 20
    assert value("HI") == 20
    assert value("hey") == 20

def test_other():
    assert value("goodbye") == 100
    assert value("Goodbye") == 100
    assert value("GOODBYE") == 100
    assert value("what's up?") == 100

if __name__ == "__main__":
    pytest.main()
