import pytest
from fuel import convert, guage

def main():
    test_zero()
    test_sez()
    test_koli()

def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_sez():
    with pytest.raises(ValueError):
        convert("kit/cat")

def test_koli():
    assert convert("1/4") == 25
    assert guage("1/4") == "25%"
    assert convert("4/4") == 100
    assert guage("4/4") == "F"
    assert convert("0/4") == 0
    assert guage("0/4") == "E"

if __name__ == "__main__":
    main()
