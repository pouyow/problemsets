from numb3rs import validitate


def main():
    cat()

def cat():
    assert validitate("cat") == False

def zero():
    assert validitate("0.0.0.0") == True

def qqq():
    assert validitate("255.255.255.255") == True
