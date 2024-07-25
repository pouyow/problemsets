def main():
    fuel_range = input("Enter fuel range x/y: ")
    percentage = convert(fuel_range)
    print(gauge(percentage))

def convert(fuel):
    try:
        x, y = map(int, fuel.split('/'))
        percentage = round((x / y) * 100)
        if percentage > 100:
            raise ValueError
        return percentage
    except (ValueError, ZeroDivisionError):
        raise

def gauge(percentage):
    if percentage == 0:
        return "E"
    elif percentage == 100:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
