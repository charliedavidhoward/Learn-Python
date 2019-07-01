# When some people receive change after shopping, they put it into a container and let it add up over time. Once they fill up the container, they'll roll them up in coin wrappers which can then be traded in at a bank for what they are worth. While most banks will give away coin wrappers for free, it's convenient to have an idea of how many you will need. Instead of counting how many coins you have, it's easier to separate all of your coins, weigh them, and then estimate how many of each type you have and then how many wrappers you'll need.
#
# For example, if you weigh all of your dimes and see that you have 1276.9g of them, you can estimate that you have about 563 dimes (since each one is 2.268g) and you would be able to fill 11 dime wrappers.
#
# Goal Create a program that allows the user to input the total weight of each type of coin they have (pennies, nickels, dimes, and quarters), and then print out how many of each type of wrapper they would need, how many coins they have, and the estimated total value of all of their money.
#
# Weight of each coin and how many fit inside each type of wrapper.
#
# Subgoals
#
#     Round all numbers printed out to the nearest whole number.
#
#     Allow the user to select whether they want to submit the weight in either grams or pounds.
#
#
# Amount in one roll:
# pennies - 50
# nickels - 40
# dimes - 50
# quarters - 40
#
# weight (g):
# penny - 2.5
# nickel - 5
# dime - 2.268
# quarter - 5.670

import math

print("Enter your weight (g) of:")
pennies = float(input("Pennies: "))
nickels = float(input("Nickels: "))
dimes = float(input("Dimes: "))
quarters = float(input("Quarters: "))

if pennies > 0:
    no_of_pennies = round(pennies / 2.5)
    no_of_pennies_wrappers = math.floor(no_of_pennies / 50)
    print("You have approximately " + str(no_of_pennies) + " pennies")
    print("So you need " + str(no_of_pennies_wrappers) + " penny wrappers")
else:
    print("No pennies")

if nickels > 0:
    no_of_nickels = round(nickels / 5)
    no_of_nickels_wrappers = math.floor(no_of_nickels / 40)
    print("You have approximately " + str(no_of_nickels) + " nickels")
    print("So you need " + str(no_of_nickels_wrappers) + " nickel wrappers")
else:
    print("No nickels")

if dimes > 0:
    no_of_dimes = round(dimes / 2.268)
    no_of_dimes_wrappers = math.floor(no_of_dimes / 50)
    print("You have approximately " + str(no_of_dimes) + " dimes")
    print("So you need " + str(no_of_dimes_wrappers) + " dime wrappers")
else:
    print("No dimes")

if quarters > 0:
    no_of_quarters = round(quarters / 5.670)
    no_of_quarters_wrappers = math.floor(no_of_quarters / 40)
    print("You have approximately " + str(no_of_quarters) + " quarters")
    print("So you need " + str(no_of_quarters_wrappers) + " quarter wrappers")
else:
    print("No quarters")

total = (no_of_pennies * 0.01) + (no_of_nickels * 0.05) + (no_of_dimes * 0.1) + (no_of_quarters * 0.25)

print("In total, you have $" + str(total))
