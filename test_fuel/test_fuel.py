import pytest
from fuel import getxy, ss

def test_zero():
    with pytest.raises(ZeroDivisionError):
        getxy("1/0")

def test_sez():
    with pytest.raises(ValueError):
        getxy("kit/cat")

def test_koli():
    assert getxy("1/4") == 25
    assert ss("1/4") == "25%"
    assert getxy("4/4") == 100
    assert ss("4/4") == "F"
    assert getxy("0/4") == 0
    assert ss("0/4") == "E"

if __name__ == "__main__":
    pytest.main()
