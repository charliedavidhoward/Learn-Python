import random
from words_file import list_of_words
from hangman import hangman
from collections import Counter

word = random.choice(list_of_words)

incorrect_guesses = 0
guessed_letters = ""

def valid_guess(guess):
    if len(guess) == 1 and guess in 'abcdefghijklmnopqrstuvwxyz':
        return True
    else:
        return False

while True:
    for i in word:
        if i in guessed_letters:
            print(i.upper(), end=" ", flush=True)
        else:
            print("_ ", end="", flush=True)
    print("")
    if Counter(guessed_letters) == Counter(word):
        print("")
        print("Congratulations!")
        print("")
        print("The word was " + word.upper())
        break
    print("")
    while True:
        guess = input("Your guess (one letter, lower case) >> ")
        if valid_guess(guess):
            break
    if guess.lower() in list(word):
        print("")
        print("Correct!")
        print(hangman[incorrect_guesses])
        for i in range(word.count(guess)):
            guessed_letters += guess.lower()
    else:
        if incorrect_guesses == (len(hangman) - 2):
            print("")
            print("You lost!")
            print(hangman[-1])
            print("The word was " + word.upper())
            break
        else:
            print("")
            incorrect_guesses += 1
            if incorrect_guesses == (len(hangman) - 2):
                print("Incorrect!  Only one more chance!")
            else:
                print("Incorrect!")
            print(hangman[incorrect_guesses])

