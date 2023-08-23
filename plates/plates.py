def main():
    plate = input("Plate: ")
    if is_valid(plate):
      print("Valid")
    else:
      print("Invalid")
def is_valid(s):
     while True:
      if len(s) >= 2 and len(s) <= 6 and s[0:].isalpha() and s[0:].isupper() and s[:2].isdigit() False and "." not in s and " " not in s and "?" not in s and "!" not in s and "0" not in s[0]:
       return True
      else:
        return False



main()