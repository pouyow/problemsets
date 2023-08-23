payam = input("enter: ")
print("output:" , end="")
for letter in payam:
    if not letter.lower in ["e","a","i","u","o"]:
      print(letter, end="")

print()