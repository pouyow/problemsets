def main():
    plate = input("Plate: ")
    if is_valid(plate):
      print("Valid")
    else:
      print("Invalid")
def is_valid(plate):
   if len(plate) < 2 or len(plate) > 6:
      return False
   if plate[0].isalpha() == False or plate[1].isalpha() == False:
      return False

   i = 0
   while i < len(plate):
      if plate[i].isalpha() == False and plate[i:].isalpha() == False:
       if plate[i] == "0":
          return False
       elif not plate[i:].isdigit():
          return False
       else:
          break
      i+=1
   for s in plate:
      if s in ["?","!"," ","."]:
         return False
   return True


main()