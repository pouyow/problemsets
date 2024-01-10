import emoji
x = input("enter: ").replace(" ","_")
s = emoji.emojize(x)
print(s)
