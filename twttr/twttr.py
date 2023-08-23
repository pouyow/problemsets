payam = input("enter: ")
q = ["e","a","i","u","o"]
for letter in payam:
    if not letter.lower() in q:
      print(letter, end="")
