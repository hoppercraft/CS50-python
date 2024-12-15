from project import difficulty,guessed,man

easy=["And", "Fix", "Own", "Are", "Fly", "Odd", "Ape", "Fry", "Our", "Ace", "For", "Pet", "Act", "Got", "Pat", "Ask", "Get", "Peg", "Arm", "God", "Paw"]
medium=["Back", "Ball", "Five", "Cake", "Fish", "Game", "Dark", "Home", "Cool", "Four", "King", "Good", "Girl", "Bean", "Fire"]
hard=["Apple", "Bread", "Cloud", "Dance", "Flame", "Grace", "House", "Jelly", "Knife", "Light", "Music", "Night", "Quest", "River"]

def test_difficulty():
    assert difficulty("1") in easy
    assert difficulty("2") in medium
    assert difficulty("3") in hard

def test_guessed():
    assert guessed(["a","p","p","l","e"]) == "apple"
    assert guessed(["b","a","l","l"]) == "ball"
    assert guessed(["c","a","t"]) == "cat"

def test_man():
    assert man(1) == """
  +---+
  |   |
  O   |
      |
      |
      |
========="""

    assert man(3) == """
  +---+
  |   |
  O   |
 /|   |
      |
      |
========="""

    assert man(8) == False
