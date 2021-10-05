"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""


def backspace_compare(first: str, second: str):
    f_list = list(first)
    s_list = list(second)
    for f in f_list:
        if f == '#':
            f_index = f_list.index('#')
            f_list[f_index] = '0'
            if f_index != 0:
                f_list[f_index - 1] = '0'

    for s in s_list:
        if s == '#':
            s_index = s_list.index('#')
            s_list[s_index] = '0'
            if s_index != 0:
                s_list[s_index - 1] = '0'

    while '0' in f_list:
        f_list.remove('0')
    while '0' in s_list:
        s_list.remove('0')
    print(f_list, s_list)
    for i in range(len(f_list)):
        if f_list[i] != s_list[i]:
            return False

    return True


# s1 = "ab#c"
# t1 = "ad#c"
# print(backspace_compare(s1, t1))
# s2 = "a##c"
# t2 = "#a#c"
# print(backspace_compare(t2, s2))
# s3 = "a#c"
# t3 = "b"
# print(backspace_compare(t3, s3))
