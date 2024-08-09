import re

def convert(time_str):
    pattern = r'^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$'
    match = re.match(pattern, time_str)

    if not match:
        raise ValueError("Invalid time format")

    start_hour = int(match.group(1))
    start_minute = int(match.group(2) or "00")
    start_period = match.group(3)
    end_hour = int(match.group(4))
    end_minute = int(match.group(5) or "00")
    end_period = match.group(6)

    if not (0 <= start_hour <= 12) or not (0 <= start_minute < 60) or not (0 <= end_hour <= 12) or not (0 <= end_minute < 60):
        raise ValueError("Invalid time value")

    if start_period == "PM" and start_hour != 12:
        start_hour += 12
    elif start_period == "AM" and start_hour == 12:
        start_hour = 0

    if end_period == "PM" and end_hour != 12:
        end_hour += 12
    elif end_period == "AM" and end_hour == 12:
        end_hour = 0

    start_time = f"{start_hour:02}:{start_minute:02}"
    end_time = f"{end_hour:02}:{end_minute:02}"

    return f"{start_time} to {end_time}"
