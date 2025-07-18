from numb3rs import validate

def main():
    test_invalid()
    test_valid()
    test_first_byte_valid()
    test_first_byte_invalid()
    test_full_ip_valid()
    test_full_ip_invalid()

def test_first_byte_valid():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("127.127.127.127") == True
    assert validate("192.168.1.1") == True

def test_first_byte_invalid():
    assert validate("256.256.256.256") == False
    assert validate("300.300.300.300") == False
    assert validate("999.999.999.999") == False
    assert validate("abc.def.ghi.jkl") == False


def test_invalid():
    assert validate("cat") == False
    assert validate("256.256.256.256") == False
    assert validate("1.2.3.1000") == False
    assert validate("0.0.0.0.0") == False
    assert validate("10.10.10") == False
    assert validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == False
    assert validate("2.2.2") == False
    assert validate("500.12.22.14") == False
def test_valid():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("127.0.0.1") == True
    assert validate("192.168.1.1") == True
def test_full_ip_valid():
    assert validate("192.168.1.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True

def test_full_ip_invalid():
    assert validate("999.999.999.999") == False
    assert validate("256.256.256.256") == False
    assert validate("192.168.1.256") == False


if __name__ == "__main__":
    main()
