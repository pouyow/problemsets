from emoji import emojize
x = input("enter: ").replace(" ","_")
s = emoji.emojize(x)
print("out: ", s)
