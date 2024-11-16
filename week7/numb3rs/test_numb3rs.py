from numb3rs import validate

def test_ip():
    assert validate("1.2.3.4") == True
    assert validate("1.192.168.4") == True

def test_range():
    assert validate("255.256.255.266") == False
    assert validate("255.256.255.266.1123") == False

def test_alpha():
    assert validate("apple") == False
    assert validate("ball") == False
