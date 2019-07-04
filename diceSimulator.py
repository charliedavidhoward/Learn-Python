# Goal
#
# By using the random module, python can do things like pseudo-random number generation. So in this program, allow the user to input the amount of sides on a dice and how many times it should be rolled. From there, your program should simulate dice rolls and keep track of how many times each number comes up (this does not have to be displayed). After that, print out how many times each number came up.
#
# Subgoal
#
#     Adjust your program so that if the user does not type in a number when they need to, the program will keep prompting them to type in a real number until they do so.
#
#     Put the program into a loop so that the user can continue to simulate dice rolls without having to restart the entire program.
#
#     In addition to printing out how many times each side appeared, also print out the percentage it appeared. If you can, round the percentage to 4 digits total OR two decimal places.

import random

while True:
    no_of_sides = int(input("Number of sides >> "))
    no_of_rolls = int(input("Number of rolls >> "))

    rolls = []

    for i in range (0, no_of_rolls):
        roll = random.randint(1, no_of_sides)
        rolls.append(roll)

    for i in range (1, (no_of_sides + 1)):
        print(str(i) + " was rolled " + str(rolls.count(i)) + " times")


