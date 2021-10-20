from homework5.task2 import print_result

import sys

def twice_sum(x, y):
    """twice_sum calculates sum of x, y multiplied by 2"""
    return (2*(x + y))


def test_print_result_check_3_attributes():
    decorated = print_result(twice_sum)

    assert(twice_sum.__name__ == decorated.__name__)
    assert(twice_sum.__doc__ == decorated.__doc__)
    assert(decorated.__original_func is twice_sum)


def test_print_result_check_3_attributes_with_args():
    decorated = print_result(twice_sum)
    args = [1, 2]
    assert(decorated(*args) == twice_sum(*args))


def test_myoutput(capsys):
    decorated = print_result(twice_sum)
    args = [3, 2]
    decorated(*args)
    captured = capsys.readouterr()
    assert captured.out == "10\n"