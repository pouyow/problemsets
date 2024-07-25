def main():
    fraction = input("enter fuel range x/y: ")
    percentage = convert(fraction)
    print(gauge(percentage))

def convert(fraction):
    x, y = map(int, fraction.split("/"))
    if y == 0:
        raise ZeroDivisionError("division by zero")
    if x > y:
        raise ValueError("x cannot be greater than y")
    return round((x / y) * 100)

def gauge(percentage):
    if percentage == 0 or percentage == 1:
        return "E"
    elif percentage == 100 or percentage == 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
