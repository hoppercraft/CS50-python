import random
import sys
lvl=["1","2","3"]
a=[]
hangmans = [
  """
  +---+
  |   |
      |
      |
      |
      |
=========""",
  """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
  """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
  """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
  """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
  """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
  """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
========="""
]
easy=["And", "Fix", "Own", "Are", "Fly", "Odd", "Ape", "Fry", "Our", "Ace", "For", "Pet", "Act", "Got", "Pat", "Ask", "Get", "Peg", "Arm", "God", "Paw"]
medium=["Back", "Ball", "Five", "Cake", "Fish", "Game", "Dark", "Home", "Cool", "Four", "King", "Good", "Girl", "Bean", "Fire"]
hard=["Apple", "Bread", "Cloud", "Dance", "Flame", "Grace", "House", "Jelly", "Knife", "Light", "Music", "Night", "Quest", "River"]
def main():
    global a
    guess = 0
    print("Welcome to Hangman!!!")
    while True:
        diff = input("Enter the level: ")
        if diff in lvl:
            break
        else:
            print("Enter a valid lvl (1,2,3)")

    word=random.choice(difficulty(int(diff))).lower()
    for i in range(len(word)):
        a.append("_")
    while True:
        print(man(guess,word))
        print(guessed(a))
        g=input("Guess the word: ")
        w=wordy(word,g)
        if not w==True:
            guess+=1
        if guessed(a)==word:
            print(word)
            break
    print("YOU WON!!!")

def difficulty(diff):
    if diff==1:
        c = easy
    elif diff==2:
        c = medium
    else:
        c = hard
    return(c)

def guessed(a):
    x="".join(a)
    return(x)

def wordy(word,g):
    global a
    n=0
    x=False
    for i in word:
        if i==g:
            a[n]=g
            x=True
        n+=1
    return(x)


def man(n,word):
    try:
        return hangmans[n]
    except IndexError:
        sys.exit("Game Over!!! The word was "+word)

if __name__ == "__main__":
    main()
