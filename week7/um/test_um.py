from um import count

def test_um():
    assert count("um um um") == 3

def test_case():
    assert count("UM Um um") == 3

def test_catches():
    assert count("Um, Um. um?") == 3
    assert count("yum um num") == 1
