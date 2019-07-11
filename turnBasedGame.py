# GOAL
#
# Write a simple game that allows the user and the computer to take turns selecting moves to use against each other. Both the computer and the player should start out at the same amount of health (such as 100), and should be able to choose between the three moves:
#
#     The first move should do moderate damage and has a small range (such as 18-25).
#
#     The second move should have a large range of damage and can deal high or low damage (such as 10-35).
#
#     The third move should heal whoever casts it a moderate amount, similar to the first move.
#
# After each move, a message should be printed out that tells the user what just happened, and how much health the user and computer have. Once the user or the computer's health reaches 0, the game should end.
#
# SUBGOALS
#
#     When someone is defeated, make sure the game prints out that their health has reached 0, and not a negative number.
#
#     When the computer's health reaches a set amount (such as 35%), increase it's chance to cast heal.
#
#     Give each move a name.

import random
import time

user_health = 100
computer_health = 100


def get_user_input():
    while True:
        try:
            return int(input("Your move >> "))
        except ValueError:
            print("You must enter a number")


while True:
    print("Your health is {}".format(user_health))
    print("Your opponent's health is {}".format(computer_health))

    time.sleep(2)

    print("""
    Choose your move:
    Enter '1' - Bazooka Blast (can be high damage, but inaccurate)
    Enter '2' - Karate Chop (Reliable, but low damage)
    Enter '3' - Medical kit (heal yourself, if there are enough plasters!)
    """)

    while True:
        move = get_user_input()
        if move < 1 or move > 3:
            print("You must enter 1, 2 or 3")
        else:
            break

    if move == 1:
        print("Reloading bazooka...")
        time.sleep(1)
        print("Firing...")
        time.sleep(3)
        damage = random.randint(0, 40)
        if damage == 0:
            print("Missed!")
        elif damage < 25:
            print("You missed!  But shrapnel from the blast still hit your opponent, inflicting damage of {}!".format(damage))
        else:
            print("Direct hit, damage of {}!".format(damage))
        time.sleep(3)
        computer_health = computer_health - damage
    elif move == 2:
        print("Karate chop!")
        time.sleep(1)
        print("Your opponent stumbles back...")
        time.sleep(2)
        print("You assess the damage...")
        time.sleep(3)
        damage = random.randint(5, 15)
        print("Damage of {}!".format(damage))
        time.sleep(3)
        computer_health = computer_health - damage
    elif move == 3:
        print("You open the medical kit...")
        time.sleep(3)
        heal = random.randint(5, 20)
        if heal < 15:
            print("Only a few bandages remain...")
            time.sleep(3)
            print("Your health increases by {}!".format(heal))
        else:
            print("You stitch your arm back on...")
            time.sleep(3)
            print("Your health increases by {}!".format(heal))
        time.sleep(3)
        user_health = user_health + heal
    print("")

    if computer_health < 1:
        print("You are victorious, your opponent's health is 0!")
        break

    print("Your opponent makes their choice...")
    time.sleep(3)

    if computer_health < 35:
        opponent_move = random.choices(population=[1, 2, 3], weights=[0.2, 0.2, 0.6], k=1)[0]
    else:
        opponent_move = random.randint(1, 3)

    if opponent_move == 1:
        print("Your opponent chooses to load their slingshot!")
        time.sleep(3)
        print("They launch the rock... it flies towards you...")
        damage = random.randint(5, 15)
        time.sleep(3)
        print("Direct hit to your stomach, damage of {}!".format(damage))
        user_health = user_health - damage
        time.sleep(3)
        print("")
    elif opponent_move == 2:
        print("Your opponent instructs their homing pigeon...")
        time.sleep(2)
        print("Your notice a mine attached to its back!")
        time.sleep(3)
        damage = random.randint(0, 40)
        if damage == 0:
            print("You dive out of the way, avoiding any damage")
        elif damage < 25:
            print("You run away, but not fast enough, still experiencing damage of {}!".format(damage))
        else:
            print("The pigeon swoops in for a direct hit, damage of {}!".format(damage))
        user_health = user_health - damage
        time.sleep(3)
        print("")
    elif opponent_move == 3:
        print("Your opponent reaches for their medical pack")
        time.sleep(3)
        heal = random.randint(5, 20)
        print("Their health increases by {}".format(heal))
        computer_health = computer_health + heal
        time.sleep(3)
        print("")

    if user_health < 1:
        print("Your health is 0... you have died...")
        break

