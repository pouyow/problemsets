def main():
   x = (getxy("enter fuel range x/y: "))
   if x == 0:
     print ("E")
   elif x == 100:
     print ("F")
   else:
     print(f"{x}%")

def getxy(x):
 while True:
    try:
     ff = input("enter: ").split("/")
     x = float(ff[0])
     y = float(ff[1])
     q = round(x/y *100)
     return q

    except (ValueError, ZeroDivisionError):
       pass
main()