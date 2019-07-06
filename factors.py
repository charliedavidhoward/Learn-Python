# Define a function that creates a list of all the numbers that are factors of the user's number. For example, if the function is called factor, factor(36) should return [1,2,3,4,6,9,12,18,36]. The numbers in your list should be from least to greatest, and 1 and the original number should be included.

answers = []


def factors(num):
    num = int(num)
    for i in range (1, num):
        if num % i == 0:
            answers.append(i)
    answers.append(num)
    return answers


number = input("Enter your number >> ")

factors = factors(number)

print(factors)

