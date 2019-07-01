# BASIC GOAL Imagine that your friend is a cashier, but has a hard time counting back change to customers. Create a program that allows him to input a certain amount of change, and then print how how many quarters, dimes, nickels, and pennies are needed to make up the amount needed.
#
# For example, if he inputs 1.47, the program will tell that he needs 5 quarters, 2 dimes, 0 nickels, and 2 pennies.
#
# SUBGOALS
#
#     So your friend doesn't have to calculate how much change is needed, allow him to type in the amount of money given to him and the price of the item. The program should then tell him the amount of each coin he needs like usual.
#
#     To make the program even easier to use, loop the program back to the top so your friend can continue to use the program without having to close and open it every time he needs to count change.

import math

while True:
    price = math.floor(float(input("Price of item(s): ")) * 100)
    cash = math.floor(float(input("Cash given: ")) * 100)

    change = (cash - price)

    no_of_quarters = 0
    no_of_dimes = 0
    no_of_nickels = 0
    no_of_pennies = 0

    if change >= 25:
        no_of_quarters = math.floor(change / 25)
        change = change % 25

    if change >= 10:
        no_of_dimes = math.floor(change / 10)
        change = change % 10

    if change >= 5:
        no_of_nickels = math.floor(change / 5)
        change = change % 5

    if change >= 1:
        no_of_pennies = change

    print(str(no_of_quarters) + " quarters")
    print(str(no_of_dimes) + " dimes")
    print(str(no_of_nickels) + " nickels")
    print(str(no_of_pennies) + " pennies")
