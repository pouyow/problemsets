import pytest
from working import convert

def test_convert():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("8 PM to 8 AM") == "20:00 to 08:00"
    assert convert("7:15 AM to 7:15 PM") == "07:15 to 19:15"

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

    with pytest.raises(ValueError):
        convert("9 AM to 5:60 PM")

    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")

    with pytest.raises(ValueError):
        convert("9AM to 5PM")

    with pytest.raises(ValueError):
        convert("09:00 to 17:00")

    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

    with pytest.raises(ValueError):
        convert("10:7 AM - 5:1 PM")

    with pytest.raises(ValueError):
        convert("25:00 PM to 12:00 AM")

    with pytest.raises(ValueError):
        convert("12:00 AM - 12:00 PM")

    with pytest.raises(ValueError):
        convert("10 AM to 6 PM")

    with pytest.raises(ValueError):
        convert("6:30AM to 5:00PM")

    with pytest.raises(ValueError):
        convert("9 AM to 5PM")

    with pytest.raises(ValueError):
        convert("9AM to 5 PM")

def test_edge_cases():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("11:59 PM to 12:01 AM") == "23:59 to 00:01"
    assert convert("12:01 AM to 11:59 PM") == "00:01 to 23:59"

