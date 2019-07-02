# GOAL
#
# Define a function that allows the user to find the value of the nth term in the sequence. To make sure you've written your function correctly, test the first 10 numbers of the sequence. Remember, the 0th term is 0 and the first and second term are both 1.


def fibonacci(n):
    num_one = 0
    num_two = 1
    if n == 0:
        return num_one
    elif n == 1:
        return num_two
    else:
        for i in range(1, n):
            sum = num_one + num_two
            num_one = num_two
            num_two = sum
        return num_two


answer = fibonacci(10)

print(answer)
