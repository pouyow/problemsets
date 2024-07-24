from plates import is_valid

def main():
 test_digit()
 test_lenword()
 test_marks()

 def test_lenword():
   assert is_valid("three") == "Valid"
   assert is_valid("s") == "Invalid"
   assert is_valid("sevenword") == "Invalid"

def test_digit():
  assert is_valid("12wsa") == "Invalid"
  assert is_valid("ask12s") == "Invalid"
  assert is_valid("isa22") == "Valid"
  assert is_valid("0sdaas") == "Invalid"
def test_marks():    # not carl marx
  assert is_valid("as-s") == "Invalid"
  assert is_valid("kcsk!") == "Invalid"
  assert is_valid("douao2") == "Valid"
  assert is_valid("test es") == "Invalid"

if __name__ == "__main__":
  main()
