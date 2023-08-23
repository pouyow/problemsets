def main():
    plate = input("Plate: ")
    if is_valid(plate):
      print("Valid")
    else:
      print("Invalid")
def is_valid(s):
     while True:
      if len(s) >= 2 and len(s) <= 6 and s[:2].isalpha() and s[:2].isupper() and s[2:].isdigit() and "." not in s and " " not in s and "?" not in s and "!" not in s and "0" not in len(s[0]):
       return True
      else:
        return False



main()