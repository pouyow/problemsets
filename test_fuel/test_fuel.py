import pytest
from fuel import convert, gauge

def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_sez():
    with pytest.raises(ValueError):
        convert("2/1")

def test_koli():
    assert convert("1/4") == 25
    assert gauge(25) == "25%"
    assert convert("4/4") == 100
    assert gauge(100) == "F"
    assert convert("0/4") == 0
    assert gauge(0) == "E"

if __name__ == "__main__":
    pytest.main()
