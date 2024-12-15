# __Hangman__-save the guy from hanging
#### Video Demo: https://youtu.be/rtEVzv1JlV4?si=vqTYAC-ZlPM7Y58_
## Description:
I have made a classic game of hangman where we have to save the man from being hanged by guessing the letters.

Program Structure :
- project.py
- readme.md
- requrements.txt
- test_project.py

## Usage:
```python project.py```

When the code of the game is executed the program will ask you to choose a difficulty
```
Welcome to Hangman!!!
Enter the level
```
You can choose the level from 1-3 if you fail to do so the program will ask you to enter again until it is valid
```
Enter a valid lvl (1,2,3)
```
The difficulty of the level which you choose will decide the length of the charecter you have to guess
and begins the guessing game where you will get total of 7 lives to guess the correct letter of the word. Your life is only used when the letter you guessed is wrong.
```
  +---+
  |   |
      |
      |
      |
      |
=========
___
Guess the word:
```
if you guessed each letter of the word then you will have won the game
```
YOU WON!!!
```
or if you ran out of lives the game is over and the game will let you know what the word was
```
Game Over!!!
The word was odd
```
## Functions
The python file project.py contains a total of 5 functions including the main function whose propose is explained below:

 ### main():
 This function is responsible connecting all other functions in the program and make the game of hangman

 ### difficulty():
 This function is responsible for asking for the difficulty of the game from the user and returning a word suitable for the said difficulty.

 ### man(arg1)
 This function takes an argument as input where the argument is the counter of the number of mistakes the player has made and returns a suitable ascii art of the hangman or
 if the player has guessed the wrong letter for 7 times it returns False.

 ### guessed(arg1)
 This function takes a set of list as an argument and convert them into one string and returns the string.

 ### wordy(arg1,arg2)
 This function takes who arguments as input, where argument 1 is the word which the player has to guess and argument 2 is the letter which player has guessed.
 This function checks if the letter given by user is in the word the game as choosen to be guessed which if is the case then update the global variable a which consist of the guessed words in correct order and returns True if not then returns False.

## Libraries:
The following program consists of pip installable libraries:
- random: To find a random word from the dictionary of words to choose for the game
- pytest: To test the correctness of the program in test_pytest.py

To install all the libraries used in requirements.txt

```pip install -r requirements.txt```

__Made By: Siddhartha Karmacharya__
