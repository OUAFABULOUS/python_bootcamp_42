import sys
from random import randint


if __name__=="__main__":
    guessed = None
    rand_nb = randint(1, 99)
    while not guessed or not guessed.isdigit() or not (int(guessed) > 0 and int(guessed) < 100) or not int(guessed) == rand_nb:
        guessed = input("Guess a number between 1 and 99:")
        if guessed.isdigit() and int(guessed) == rand_nb:
            print("You won!")
            exit(0)
        elif str(guessed) == "exit":
            print("Goodbye!")
            exit(0)

