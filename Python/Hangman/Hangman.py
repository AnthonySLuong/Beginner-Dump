import json
import string
from time import sleep
from random import randint


def convert_x(word):
    guess_word = list(word)
    x_list = []
    for x in guess_word:
        if x == " ":
            x_list.append(" ")
        else:
            x_list.append("_")
    return x_list


def check_ascii(input):
    for x in list(string.ascii_lowercase):
        if input.lower() == x:
            return True
    else:
        return False


def game():
    # Setup Variable
    ListOfWords = json.loads(open('Words.json').read())
    Answer_word = ListOfWords[randint(0, len(ListOfWords))]
    Progress = convert_x(Answer_word)
    guess_count = 10
    lter_count = []

    # Check Amount of guess left & init loop
    while guess_count > 0:
        print("Guess left: %s" % (guess_count))
        print(' '.join(Progress))

        # checks for correct input
        guess = input("Enter guess: ")
        while len(guess) > 1:
            guess = input("Enter guess again: ")
        for x in lter_count:
            while guess.lower() == x:
                guess = input("Already guessed the letter: ")
        lter_count.append(guess.lower())

        # check Ascci
        while check_ascii(guess) is False:
            guess = input("Please Enter a vaild Letter: ")

        # Update the blank letters
        check = False
        for x in range(len(Answer_word)):
            if guess.lower() == Answer_word[x].lower():
                Progress[x] = Answer_word[x]
                check = True
        if check is False:
            guess_count -= 1
        print(" ")

        # Checks if player has won
        if Progress == Answer_word:
            print("You Win!")
            print("The word was %s" % (Answer_word))
            sleep(2)
            break

    # End game
    else:
        print("You lost! Try again")
        print("The word was %s" % (Answer_word))
        sleep(2)


game()
again = input("Would you like play again? ")
while again == "Y" or again == "y":
    game()
    again = input("Would you like play again? ")
else:
    print("Sad to see you go :(")
    sleep(5)
