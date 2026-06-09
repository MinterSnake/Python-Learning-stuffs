# Numbers guessing game

import random

GuessedNumber = 0
RandomNumber = 0
NumberOfGuesses = 0

def _GameScore():
    global NumberOfGuesses
    global RandomNumber
    if GuessedNumber != RandomNumber:
        NumberOfGuesses += 1

def _GenerateRandomNumber():
    global RandomNumber
    RandomNumber = random.randint(1, 6)

def _DisplayMessage(Text):
    print(Text)

def _GuessedNumberCheck():
    global GuessedNumber
    global RandomNumber
    global NumberOfGuesses
    if GuessedNumber == RandomNumber:
        _DisplayMessage("Congrats! You guessed the right number!" + " Amount of guesses: " + str(NumberOfGuesses))
    else:
        _DisplayMessage("Sorry! Ya got the wrong number!")
        _GameScore()
        _DisplayMessage("Try again! Amount of guesses: " + str(NumberOfGuesses))
        _GenerateRandomNumber()
        _UserInput()
        _GuessedNumberCheck()

def _UserInput():
    global GuessedNumber
    _DisplayMessage("-----")
    GuessedNumber = int(input("Enter your Number: "))
    _DisplayMessage("-----")

_DisplayMessage("Welcome to Minters number guessing game")
_DisplayMessage("Guess a number between 1 and 6")

_GenerateRandomNumber()

_UserInput()

_GuessedNumberCheck()

