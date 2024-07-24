from plates import is_valid

def main():
    test_lenword()
    test_digit()
    test_marks()

def test_lenword():
    assert is_valid("three") == True
    assert is_valid("s") == False
    assert is_valid("sevenword") == False

def test_digit():
    assert is_valid("12wsa") == False
    assert is_valid("ask12s") == False
    assert is_valid("isa22") == True
    assert is_valid("0sdaas") == False

def test_marks():
    assert is_valid("as-s") == False
    assert is_valid("kcsk!") == False
    assert is_valid("douao2") == True
    assert is_valid("test es") == False

if __name__ == "__main__":
    main()
