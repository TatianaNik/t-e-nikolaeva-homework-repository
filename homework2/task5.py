"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.
Write a function that accept any iterable of unique values and then
it behaves as range function:
import string
assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
"""


def custom_range(input_str, *args):
    if len(args) == 1:
        index = input_str.find(args[0])
        res = input_str[0:index]
    elif len(args) == 2:
        index1 = input_str.find(args[0])
        index2 = input_str.find(args[1])
        res = input_str[index1:index2]
    else:
        if len(args) == 3:
            index1 = input_str.find(args[0])
            index2 = input_str.find(args[1])
            res = input_str[index1:index2:args[2]]
    return [i for i in res]


# print(custom_range(string.ascii_lowercase, 'g'))
# print(custom_range(string.ascii_lowercase, 'g', 'p'))
# print(custom_range(string.ascii_lowercase, 'p', 'g', -2))
