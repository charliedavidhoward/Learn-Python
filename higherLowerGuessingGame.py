# BASIC GOAL Create a simple game where the computer randomly selects a number between 1 and 100 and the user has to guess what the number is. After every guess, the computer should tell the user if the guess is higher or lower than the answer. When the user guesses the correct number, print out a congratulatory message.
#
# SUB GOALS
#
#     Add an introduction message that explains to the user how to play your game.
#
#     In addition to the congratulatory message at the end of the game, also print out how many guesses were taken before the user arrived at the correct answer.
#
#     At the end of the game, allow the user to decide if they want to play again (without having to restart the program).

import random

print("Welcome to the game.  Guess a number between 1 and 100!")

while True:
    secret_number = random.randint(1, 100)
    no_guesses = 0
    while True:
        guess = input("> ")
        if int(guess) == secret_number:
            print("Congratulations! The secret number was " + str(secret_number) + "!")
            no_guesses += 1
            print("You took " + str(no_guesses) + " guesses")
            break
        elif int(guess) > secret_number:
            print("Your guess is higher than the number")
            no_guesses += 1
        else:
            print("Your guess is lower than the number")
            no_guesses += 1
    play_again = input("Do you want to play again? (Y/N) ")
    if play_again.lower() == 'n':
        break
