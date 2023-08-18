immie = input("enter: ").split(".")
dorost = immie[-1].strip().lower()
if dorost == ("jpeg"):
    print("image/jpeg")
elif dorost == ("jpg"):
    print("image/jpg")
elif dorost == ("png"):
    print("image/png")
elif dorost == ("gif"):
    print("image/gif")
elif dorost == ("txt"):
    print("text/plain")
elif dorost == ("zip"):
    print("application/zip")
elif dorost == ("pdf"):
    print("application/pdf")
else:
    print("application/octet-stream")
