payam = input("enter: ")
for lette in payam:
    if lette.isupper():
        print(payam.replace(lette,'_' + lette.lower()))
    else:
        print(payam)