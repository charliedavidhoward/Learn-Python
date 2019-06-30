# Goal
#
#     Allow the user to enter their question
#
#     Display an in progress message( i.e. "thinking")
#
#     Create 20 responses, and show a random response
#
#     Allow the user to ask another question or quit
#
# Bonus Using whatever module you like, add a gui. Your gui must have:
#
#     A box for users to enter the question
#
#     At least 4 buttons: Ask , clear(the text box), play again and quit(this must close the window)

import time
import random

responses = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "You may rely on it",
    "Yes, definitely",
    "Most likely",
    "As I see it, yes"
    "Yes",
    "All signs point to yes",
    "Reply hazy, try again",
    "Better not tell you now",
    "Ask again later",
    "Don't count on it",
    "Outlook not so good",
    "My sources say no",
    "Very doubtful",
    "My reply is no",
    "Concentrate and ask again",
    "Cannot predict now",
    "No"
]


while True:
    question = input("> ")
    if question.lower() == "quit":
        break
    else:
        print("Thinking...")
        time.sleep(2)
        print(random.choice(responses))

