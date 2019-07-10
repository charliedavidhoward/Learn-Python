# GOAL
#
# Create a program that allows the user to choose a time and date, and then prints out a message at given intervals (such as every second) that tells the user how much longer there is until the selected time.
#
# SUBGOALS
#
#     If the selected time has already passed, have the program tell the user to start over.
#
#     If your program asks for the year, month, day, hour, etc. separately, allow the user to be able to type in either the month name or its number.

from datetime import datetime
import time


def get_user_input(string):
    if string == "year":
        while True:
            try:
                return int(input("Enter {} >> ". format(string)))
            except ValueError:
                print("Must be four digits, please try again")
    else:
        while True:
            try:
                return int(input("Enter {} >> ".format(string)))
            except ValueError:
                print("Must be two digits, please try again")


while True:
    while True:
        year = get_user_input("year")
        if len(str(year)) is not 4:
            print("Year must be four digits")
        else:
            break

    while True:
        month = get_user_input("month")
        if month > 12 or month < 1:
            print("Month must be between 1 and 12")
        else:
            break

    while True:
        day = get_user_input("day")
        if month == 2 and (day > 28 or day < 1):
            print("Day must be between 1 and 28")
        elif (month == 4 or month == 6 or month == 9 or month == 11) and (day > 30 or day < 1):
            print("Day must be between 1 and 30")
        elif day > 31 or day < 1:
            print("Day must be between 1 and 31")
        else:
            break

    while True:
        hour = get_user_input('hour')
        if hour > 24 or hour < 0:
            print("Hour must be between 0 and 24")
        else:
            break

    while True:
        minute = get_user_input("minute")
        if minute > 60 or minute < 0:
            print("Minute must be between 0 and 60")
        else:
            break

    while True:
        second = get_user_input("second")
        if second > 60 or second < 0:
            print("Second must be between 0 and 60")
        else:
            break

    chosen_time = datetime(year, month, day, hour, minute, second)

    if chosen_time < datetime.now():
        print("Your chosen time is before the current time, try again")
    else:
        break

while datetime.now() < chosen_time:
    time_difference = chosen_time - datetime.now().replace(microsecond=0)
    print("Time to go: {}".format(time_difference))
    time.sleep(1)

print("Time reached")
