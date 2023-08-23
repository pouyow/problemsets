payam = input("enter: ")
q = ["e","a","i","u","o"]
print("output:" , end="")
for letter in payam:
    if not letter in q:
      print(letter, end="")

print()