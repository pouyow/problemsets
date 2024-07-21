from twttr import shorten

def main():
    test_temp()

def test_temp():
   try:
    assert shorten("pouya") == "py"
   except(1):
      pass
if __name__ == "__main__":
    main()
