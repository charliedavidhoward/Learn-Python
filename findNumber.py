# Between 1 and 1000, there are only 2 numbers that meet the following criteria. 
# #
# #     The number has two or more digits.
# #
# #     The number is prime.
# #
# #     The number does NOT contain a 1 or 7 in it.
# #
# #     The sum of all of the digits is less than or equal to 10.
# #
# #     The first two digits add up to be odd.
# #
# #     The second to last digit is even.
# #
# #     The last digit is equal to how many digits are in the number.


def two_or_more(num):
    if num >= 10:
        return True
    else:
        return False


def prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True


def no_one_or_seven(num):
    i = str(num)
    if '1' in i or '7' in i:
        return False
    else:
        return True


def sum_less_than_or_equal_ten(num):
    answer = [int(i) for i in str(num)]
    result = 0
    for i in answer:
        result += i
    if result <= 10:
        return True
    else:
        return False


def first_two_sum_odd(num):
    if num < 10:
        return False
    else:
        sum = 0
        answer = [int(i) for i in str(num)]
        for i in range(0, 2):
            sum += answer[i]
        if sum % 2 == 0:
            return False
        else:
            return True


def second_to_last_even(num):
    answer = str(num)
    result = int(answer[-2])
    if result % 2 == 0:
        return True
    else:
        return False


def last_digit_equal_to_length(num):
    answer = str(num)
    result = int(answer[-1])
    if int(result) == len(answer):
        return True
    else:
        return False


for i in range (0, 1001):
    if two_or_more(i) and prime(i) and no_one_or_seven(i) and sum_less_than_or_equal_ten(i) \
            and first_two_sum_odd(i) and second_to_last_even(i) and last_digit_equal_to_length(i):
        print(i)
