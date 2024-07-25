def main():
    fuel_percentage = guage(input("enter fuel range x/y: "))
    print(fuel_percentage)

def guage(fuel):
    x = convert(fuel)
    if x == 0:
        return "E"
    elif x == 100:
        return "F"
    else:
        return f"{x}%"

def convert(fuel):
    try:
        ff = fuel.split("/")
        x = int(ff[0])
        y = int(ff[1])
        q = round(float(x / y * 100))
        if q <= 100:
            return q
    except (ValueError, ZeroDivisionError, IndexError):
        raise

if __name__ == "__main__":
    main()
