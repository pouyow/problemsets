from datetime import date
from seasons import minutes_lived

def test_minutes_lived():
    fixed_today = date(2023, 8, 10)

    class FixedDate(date):
        @classmethod
        def today(cls):
            return fixed_today

    import seasons
    seasons.date = FixedDate

    result = minutes_lived("2000-01-01")
    expected = "Twelve million, four hundred fifteen thousand, six hundred eighty"
    assert result == expected, f"Expected: {expected}, but got: {result}"
