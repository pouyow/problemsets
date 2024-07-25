def main():
    x = (getxy("enter fuel range x/y: "))
    if x == 0 or x == 1:
        return "E"
    elif x == 100 or x == 99:
        return "F"
    else:
        return f"{x}%"

def getxy(prompt):
    while True:
        try:
            ff = prompt.split("/")
            x = int(ff[0])
            y = int(ff[1])
            q = round(float(x / y * 100))
            if q <= 100:
                return q
        except (ValueError, ZeroDivisionError, IndexError):
            pass

if __name__ == "__main__":
    result = main()
    if result:
        print(result)
