def main():
   x = (getxy("enter fuel range x/y: "))
   print(f"{x}%")

def getxy(x):
 while True:
    try:
     ff = input("enter: ").split("/")
     x = float(ff[0])
     y = float(ff[1])
     q = round(x/y *100)
     if q == 0:
        return ("E")
     elif q == 100:
        return ("F")
     else:
        return q

    except (ValueError, ZeroDivisionError):
       pass
main()