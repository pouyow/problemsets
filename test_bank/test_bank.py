import pytest
from bank import value

def test_value():
    assert value("hello") == "$0"
    assert value("h") == "$20"
    assert value("hey") == "$20"
    assert value("goodbye") == "$100"
    assert value("anything else") == "$100"

if __name__ == "__main__":
    pytest.main()
