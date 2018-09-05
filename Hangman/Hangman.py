import string
from list import return_words
from time import sleep


def convert_list(word):
    word_lst = []
    for x in word:
        word_lst.append(x)
    return word_lst


def convert_x(word):
    guess_word = convert_list(word)
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
    # setups Varible
    correct_word = convert_list(return_words())
    guessing = convert_x(correct_word)
    guess_count = 10
    lter_count = []

    while guess_count > 0:
        print("Guess left: %s" % (guess_count))
        print(' '.join(guessing), )

    # check for input
        guess = input("Enter guess: ")
        while len(guess) > 1:
            guess = input("Enter guess again: ")
        for x in lter_count:
            while guess.lower() == x:
                guess = input("Already guessed the letter: ")
        lter_count.append(guess.lower())

    # checks ascii
        while check_ascii(guess) is False:
            guess = input("Please Enter a vaild Letter: ")

    # updates word
        check = False
        for x in range(len(correct_word)):
            if guess.lower() == correct_word[x].lower():
                guessing[x] = correct_word[x]
                check = True
        if check is False:
            guess_count -= 1

    # check if won/lost
        if guessing == correct_word:
            print("You Win!")
            print("The word was %s" % (''.join(correct_word)))
            sleep(2)
            break
    else:
        print("You lost! Try again")
        print("The word was %s" % (''.join(correct_word)))
        sleep(2)


game()
again = input("Would you like play again? ")
while again == "Y" or again == "y":
    game()
    again = input("Would you like play again? ")
else:
    print("Sad to see you go :(")
    sleep(5)
