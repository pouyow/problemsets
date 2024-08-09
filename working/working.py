import re

def convert(s):
    pattern = r"(\d{1,2}):?(\d{2})? ?(AM|PM) to (\d{1,2}):?(\d{2})? ?(AM|PM)"
    match = re.match(pattern, s)

    if not match:
        raise ValueError("Invalid time format")

    start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()

    start_hour = int(start_hour)
    end_hour = int(end_hour)
    start_minute = int(start_minute) if start_minute else 0
    end_minute = int(end_minute) if end_minute else 0

    if start_period == "PM" and start_hour != 12:
        start_hour += 12
    elif start_period == "AM" and start_hour == 12:
        start_hour = 0

    if end_period == "PM" and end_hour != 12:
        end_hour += 12
    elif end_period == "AM" and end_hour == 12:
        end_hour = 0

    return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"

if __name__ == "__main__":
    print(convert(input("Hours: ")))
