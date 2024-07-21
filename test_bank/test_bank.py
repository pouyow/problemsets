from bank import value

def main():
 test_es()

def test_es():
    assert value("hello") == "$0"
    assert value("h") == "$20"
    assert value("random") == "$100"

if __name__ == "__main__":
    main()
