def main():
   x = int(getxy("enter fuel range x/y: "))
   print(f"{x}%")

def getxy(x):
 while True:
    try:
     ff = input("enter: ").split("/")
     x = int(ff[0])
     y = int(ff[1])
     q = (x/y *100)
     if q == 0:
        return ("E")
     elif q == 1:
        return ("F")
     else:
        return q

    except (ValueError, ZeroDivisionError):
       pass
main()