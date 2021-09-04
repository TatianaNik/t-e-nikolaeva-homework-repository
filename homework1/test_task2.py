import pytest
from homework1 import check_fib

data1 = [0, 1, 1, 2, 3, 5, 8, 13]
data2 = []
data3 = [1, 2]
data4 = [0, 1, 1, 2, 4]

def test_check_fib1():
    assert check_fib(data1)
def test_check_fib2():
    assert check_fib(data2)
def test_check_fib3():
    assert check_fib(data3)
def test_check_fib4():
    assert check_fib(data4)
