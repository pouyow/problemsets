from numb3rs import validate


def main():
    cat()
    zero()
    qqq()
    ppp()
    qqq1()

def cat():
    assert validate("cat") == False

def zero():
    assert validate("0.0.0.0") == True

def qqq():
    assert validate("255.255.255.255") == True

def ppp():
    assert validate("522.522.522.522") == False

def qqq1():
    assert validate("1.2.3.1000") == False

if __name__ == "__main__":
    main()
