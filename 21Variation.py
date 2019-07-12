# MAIN GOAL
#
# In this project, you will make a game similar to 21/blackjack. Since this is not an actual game (as far as I'm aware of), here the the instructions for how to play.
#
#     In this version, there is only one player, and there are two types of scores - the round score and the game score. The game score will begin at 100, and the game will last for five rounds.
#
#     At the beginning of the round, the player is given two random cards from a deck and they will be added together to make the player's round score. From here, the player has two options - draw another card to try to get their round score closer to 21, or they can end the round. The player can draw as many cards as they want until they end the round or their round score exceeds 21.
#
#     At the end of the round, the difference between 21 and the round score is subtracted from the game score, and then the next round begins. After the five rounds, the player is given their total score and the game is over.
#
# ---Other Information About The Game---
#
#     Aces are only worth 1.
#
#     If a player busts, 21 is subtracted from their total score.
#
#     All face cards are worth 10.
#
# So the point of your program is to allow the user to play the game described above. Many of the subgoals listed below can be added to shine up the game.
#
# SUBGOALS
#
#     At the beginning of each round, print the round number (1 to 5).
#
#     Since this is a text base game, tell the user what is happening. For example, tell him/her when he/she draws a card, the name of the card, when they bust, etc.
#
#     Create a ranking system at the end of the game and tell the user their rank. For example, if the player finishes with 50-59 points they get an F, 60-69 is a D, 70-79 is a C, 80-89 is a B, and 90-100 is an A.
#
#     At the end of each round, print out the user's total score.
#
#     This may be the hardest part of the project, depending on how you wrote it. Make sure the deck has 4 of each type of card, and then remove cards as they are drawn. At the end of each round, make the deck have all of the cards again.
#
#

import random
import time

cards = {
    "Ace": 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10
}

deck = {
    "Ace": 4,
    2: 4,
    3: 4,
    4: 4,
    5: 4,
    6: 4,
    7: 4,
    8: 4,
    9: 4,
    10: 4,
    "Jack": 4,
    "Queen": 4,
    "King": 4
}


def draw_card():
    card = random.choice(list(cards.items()))

    round_deck[card[0]] -= 1
    if round_deck[card[0]] == 0:
        del round_deck[card[0]]

    return card


game_score = 100

for i in range(1, 6):
    round_deck = deck.copy()
    print("Round {} of 5!".format(i))
    print("")
    time.sleep(1)
    print("Your game score is {}".format(game_score))
    print("")
    first_card = draw_card()
    second_card = draw_card()
    time.sleep(1)
    print("Your first card is a {}".format(first_card[0]))
    time.sleep(1)
    print('Your second card is a {}'.format(second_card[0]))
    total = first_card[1] + second_card[1]
    time.sleep(1)
    print("")
    print("Your total is {}".format(total))
    while True:
        time.sleep(1)
        print("")
        print("Stick or twist?")
        choice = input(">> ")
        print("")
        if choice.lower() == "stick":
            game_score = game_score - (21 - total)
            print("")
            break
        elif choice.lower() == "twist":
            card = draw_card()
            time.sleep(1)
            print("You have received a {}".format(card[0]))
            time.sleep(1)
            total = total + card[1]
            if total > 21:
                print("Bust!  Your total is {}!".format(total))
                print("")
                time.sleep(3)
                game_score = game_score - 21
                break
            else:
                print("Your total is {}".format(total))

if game_score < 0:
    game_score = 0

print("Game over!  Your total score is {}".format(game_score))

