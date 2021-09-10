"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import string

from typing import List


def get_longest_diverse_words(file_path: str, encoding="utf8") -> List[str]:

    words_and_numbers_of_dif_sym = []   # working list of lists
    with open(file_path, encoding=encoding) as file:
        f = file.read()
        words = f.split()
        while len(words_and_numbers_of_dif_sym) < 10:
            for word in words:
                num_of_dif_symb = 0
                for i in range(len(word)):
                    if word.count(word[i]) == 1:
                        num_of_dif_symb += 1
                words_and_numbers_of_dif_sym.append([word, num_of_dif_symb])
#       print(words_and_numbers_of_dif_sym)
        number0 = 1
        result = []
        for word, number in words_and_numbers_of_dif_sym:
            if number >= number0 and len(result) < 10:
                result.append(word)
                number0 = number
            elif number >= number0:
                del result[0]
                result.append(word)

        print(result)
    return result


get_longest_diverse_words("data.txt", encoding="unicode-escape")

            
#  the code below is running slowly, but the result was "Y"
#  I made comments so it will not disturb other functions
#
# def get_rarest_char(file_path: str) -> str:
#
#     with open(file_path) as file:
#         f = file.read()
#         num_char = 1000000
#         for char in f:
#             num_new_char = f.count(char)
#             if num_new_char < num_char:
#                 num_char = num_new_char
#                 rarest_char = char
#     print(rarest_char)
#     return rarest_char
#
#
# get_rarest_char("data.txt")


def count_punctuation_chars(file_path: str, encoding="utf8") -> int:
    with open(file_path, encoding=encoding) as file:
        num = 0
        f = file.read()
        for symbol in f:
            if symbol in string.punctuation:
                num += 1

    print(num)
    return num


count_punctuation_chars("data.txt", encoding="unicode-escape")


def count_non_ascii_chars(file_path: str, encoding="utf8") -> int:
    with open(file_path, encoding=encoding) as file:
        f = file.read()
        counter = 0
        for symbol in f:
            if not symbol.isascii():
                counter += 1
    print(counter)
    return counter


count_non_ascii_chars("data.txt", encoding="unicode-escape")


def get_most_common_non_ascii_char(file_path: str, encoding="utf8") -> str:
    with open(file_path, encoding=encoding) as file:
        f = file.read()
        counter = 0
        for symbol in f:
            if not symbol.isascii() and counter < f.count(symbol):
                counter = f.count(symbol)
                most_common_char = symbol
    print(counter, most_common_char)
    return most_common_char


get_most_common_non_ascii_char("data.txt", encoding="unicode-escape")
