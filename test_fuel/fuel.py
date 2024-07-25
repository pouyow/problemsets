def main():
    fraction = input("Enter fuel range x/y: ")
    try:
        percentage = convert(fraction)
        print(gauge(percentage))
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")

def convert(fraction):
    try:
        x, y = map(int, fraction.split("/"))
        if y == 0:
            raise ZeroDivisionError
        if x > y or x < 0 or y < 0:
            raise ValueError
        return round(x / y * 100)
    except ValueError:
        raise ValueError("Invalid input")

def gauge(percentage):
    if percentage == 0:
        return "E"
    elif percentage == 100:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
