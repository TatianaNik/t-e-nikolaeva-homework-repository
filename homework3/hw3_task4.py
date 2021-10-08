"""
Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
- 9 is an Armstrong number, 9 = 9^1 = 9
- 10 is not: 10 != 1^2 + 0^2 = 1
- 153 is : 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
Write a function that detects if a number is Armstrong number in functionaly style:
 - use map or other utilities from functools library,
 - use anonymous functions (or use function as argument)
 - do not use loops, preferably using list comprehensions
"""


def is_armstrong(number: int) -> bool:
    number_str = str(number)
    number_list = list(number_str)
    int_numbers = [int(i) for i in number_list]
    number_of_digits = len(number_str)
    res = list(map(lambda i: i ** number_of_digits, int_numbers))
    res_sum = sum(i for i in res)
    if res_sum == number:
        print(f'{number} is Armstrong number')
        return True
    else:
        print(f'{number} is not Armstrong number')
        return False


# is_armstrong(153)
# is_armstrong(10)

# assert is_armstrong(153) is True, 'Is Armstrong number'
# assert is_armstrong(10) is False, 'Is not Armstrong number'
