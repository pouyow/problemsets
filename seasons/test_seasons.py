from seasons import minutes_lived

def test_minutes_lived():
    assert minutes_lived("2000-01-01") == "Twelve million, three hundred forty-nine thousand, six hundred minutes"
    assert minutes_lived("2020-01-01") == "Two million, one hundred forty-four thousand minutes"

    assert minutes_lived("2016-02-29") == "Four million, one hundred seventy-six thousand, one hundred sixty minutes"

    assert minutes_lived("2023-08-10") == "Zero minutes"

    assert minutes_lived("2020-13-01") is None
    assert minutes_lived("abcd-ef-gh") is None

    assert minutes_lived("2020-02-30") is None
    assert minutes_lived("2020-04-31") is None

