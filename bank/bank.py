koli = input("entet: ")
flitt = koli.capitalize()[0].lower().strip()
fword = koli.split()[0].lower().replace("," , "").strip()
if fword == ("hello"):
    print ("$0")
elif flitt == ("h"):
    print("$20")
else:
    print("$100")
