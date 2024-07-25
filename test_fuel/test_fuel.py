import pytest
from io import StringIO
from unittest.mock import patch
from fuel import getxy, main

def test_zero_division():
    with patch('builtins.input', return_value='1/0'):
        with pytest.raises(ZeroDivisionError):
            getxy("enter fuel range x/y: ")

def test_value_error():
    with patch('builtins.input', return_value='5/3'):
        with pytest.raises(ValueError):
            getxy("enter fuel range x/y: ")

def test_convert():
    with patch('builtins.input', return_value='1/4'):
        assert getxy("enter fuel range x/y: ") == 25
    with patch('builtins.input', return_value='1/1'):
        assert getxy("enter fuel range x/y: ") == 100
    with patch('builtins.input', return_value='0/1'):
        assert getxy("enter fuel range x/y: ") == 0

def test_gauge():
    with patch('builtins.input', return_value='0/1'):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
            assert fake_out.getvalue().strip() == "E"
    with patch('builtins.input', return_value='1/1'):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
            assert fake_out.getvalue().strip() == "F"
    with patch('builtins.input', return_value='1/4'):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
            assert fake_out.getvalue().strip() == "25%"

if __name__ == "__main__":
    pytest.main()
