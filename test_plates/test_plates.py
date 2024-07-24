from plates import is_valid

def main():
    test_lenword()
    test_digit()
    test_marks()
    test_zero()
    test_beginning()

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

def test_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("CS50P1") == False

def test_beginning():
    assert is_valid("AA1234") == True
    assert is_valid("A1234") == True
    assert is_valid("1234AA") == False
    assert is_valid("AAA123") == True

if __name__ == "__main__":
    main()
