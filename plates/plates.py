def main():
    plate = input("Plate: ")
    if is_valid(plate):
      print("Valid")
    else:
      print("Invalid")
def is_valid(s):
     while True:
      if len(s) <= 6 and s[:2].isalpha() and s[:2].isupper() and s[2:].isdigit():
       return True
      else:
         return False



main()