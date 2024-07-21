from twttr import shorten

def main():
    test_temp()

def test_temp():
    assert shorten("pouya") == "py"
    assert shorten("POUYA") == "PY"
    assert shorten("Twitter") == "Twttr"
    assert shorten("TwItter") == "Twttr"
    assert shorten("1234") == "1234"
    assert shorten("!@#$") == "!@#$"

if __name__ == "__main__":
    main()
