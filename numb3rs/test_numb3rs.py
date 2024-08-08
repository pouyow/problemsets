from numb3rs import validitate


def main():
    cat()

def cat():
    assert validitate("cat") == False

def zero():
    assert validitate("0.0.0.0") == True

def qqq():
    assert validitate("255.255.255.255") == True

def ppp():
    assert validitate("522.522.522.522") == False

def qqq():
    assert validitate("1.2.3.1000") == False

