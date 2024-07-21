from twtter import shorten

def main():
    test_temp()

def test_temp():
    assert shorten("pouya") == "py"

if __name__ == "__main__":
    main()
    