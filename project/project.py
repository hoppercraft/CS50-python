#Hangman-save the guy from hanging
import random
a=[]

def main():
    print("Hangman-save the guy from hanging")
    global a
    guess = 0
    word=difficulty().lower()
    for i in range(len(word)):
        a.append("_")
    while True:
        if man(guess) != False:
            print(man(guess))
            print(guessed(a))
            g=input("Guess the word: ")
            w=wordy(word,g)
            if not w==True:
                guess+=1
            if guessed(a)==word:
                print(word)
                print("YOU WON!!!")
                break
        else:
            print("Game Over!!!\nThe word was",word)
            break

def difficulty(diff=""):
    easy=["And", "Fix", "Own", "Are", "Fly", "Odd", "Ape", "Fry", "Our", "Ace", "For", "Pet", "Act", "Got", "Pat", "Ask", "Get", "Peg", "Arm", "God", "Paw"]
    medium=["Back", "Ball", "Five", "Cake", "Fish", "Game", "Dark", "Home", "Cool", "Four", "King", "Good", "Girl", "Bean", "Fire"]
    hard=["Apple", "Bread", "Cloud", "Dance", "Flame", "Grace", "House", "Jelly", "Knife", "Light", "Music", "Night", "Quest", "River"]
    while True:
        if __name__ == "__main__":
            diff = input("Enter the level: ")
        if diff in ["1","2","3"]:
            break
        else:
                print("Enter a valid lvl (1,2,3)")
    diff=int(diff)
    if diff==1:
        c = easy
    elif diff==2:
        c = medium
    else:
        c = hard
    return(random.choice(c))

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


def man(g):
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
    try:
        return hangmans[g]
    except IndexError:
        return(False)

if __name__ == "__main__":
    main()
