cal = input("enter: x y z ").split(" ")
x = int(cal[0])
y = (cal[1])
z = int(cal[2])
if y == ("+"):
    print (float( x + z))
elif y == ("-"):
    print (float(x - z))
elif y == ("/"):
    print (float(x / z))
elif y == ("*"):
    print (float(x * z))
else:
    print("erorr")