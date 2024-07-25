def main():
    x = input("enter fuel range x/y: ")
    try:
        percentage = convert(x)
        print(gauge(percentage))
        exit(0)  # Exit code 0 for success
    except (ValueError, ZeroDivisionError):
        exit(1)  # Exit code 1 for error

def convert(fraction):
    try:
        num, denom = map(int, fraction.split("/"))
        if num < 0 or denom <= 0 or num > denom:
            raise ValueError
        return round((num / denom) * 100)
    except (ValueError, ZeroDivisionError):
        raise

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
