from seasons import minutes_lived

def test_minutes_lived():
    assert minutes_lived("2000-01-01") == "eleven million, five hundred fifty-six thousand, four hundred minutes"
    assert minutes_lived("1990-01-01") == "sixteen million, seven hundred seventy-six thousand, eight hundred minutes"
    assert minutes_lived("2023-01-01") == "zero minutes"
    assert minutes_lived("invalid-date") == None

def test_future_date():
    assert minutes_lived("3000-01-01") == None
