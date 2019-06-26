# write a program to find the largest number in a list

numbers = [20, 3, 4, 40, 323, 3]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number

print(max)
