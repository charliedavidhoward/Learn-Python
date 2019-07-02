# MAIN GOAL
#
# Create a program that allows the user to input the sides of any triangle, and then return whether the triangle is a Pythagorean Triple or not.
#
# SUBGOALS
#
#     If your program requires users to input the sides in a specific order, change the coding so the user can type in the sides in any order. Remember, the hypotenuse (c) is always the longest side.
#
#     Loop the program so the user can use it more than once without having to restart the program.


while True:
    one = int(input("side one: "))
    two = int(input("side two: "))
    three = int(input("side three: "))

    if (one >= two) and (one >=three):
        hypotenuse = one
        adj = two
        opp = three
    elif (two >= one) and (two >= three):
        hypotenuse = two
        adj = one
        opp = three
    else:
        hypotenuse = three
        adj = one
        opp = two

    if (adj**2) + (opp**2) == (hypotenuse**2):
        print("This triangle is a Pythagorean Triple")
    else:
        print("This triangle is not a Pythagorean Triple")

    print('')

    quit = input("Quit? (y/n) ")

    if quit.lower() == 'y':
        break

    print("")

