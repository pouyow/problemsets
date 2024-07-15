payam = input("enter: ")
for lette in payam:
    if lette.isupper():
        payam = payam.replace(lette,'_' + lette.lower())
print (payam)
