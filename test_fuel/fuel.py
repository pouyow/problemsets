def main():
   x = (getxy("enter fuel range x/y: "))
   if x == 0 or x == 1:
     print ("E")
   elif x == 100 or x == 99:
     print ("F")
   else:
     print(f"{x}%")

def getxy(prompt):
    while True:
        try:
            ff = input(prompt).split("/")
            x = int(ff[0])
            y = int(ff[1])
            q = round(float(x / y * 100))
            if q <= 100:
                return q
        except (ValueError, ZeroDivisionError, IndexError):
            pass

if __name__ == "__main__":
    main()
