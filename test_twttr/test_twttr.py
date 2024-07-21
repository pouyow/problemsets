from twttr import shorten

def main():
    test_temp()

def test_temp():
   try:
    assert shorten("pouya") == "py"
   except:
      pass(1)
if __name__ == "__main__":
    main()
