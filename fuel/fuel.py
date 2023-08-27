def main():
   x = getxy("enter fuel range x/y: ")
   print(f"{x * 100}%")

def getxy(x):
 while True:
    try:
     ff = input("enter: ").split("/")
     x = int(ff[0])
     y = int(ff[1])
     q = (x/y)
     if q == 0:
        return ("E")
     elif q == 1:
        return ("F")
     else:
        return q

    except (ValueError, ZeroDivisionError):
       pass
main()