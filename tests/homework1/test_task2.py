from homework1.task2 import check_fib


data1 = [0, 1, 1, 2, 3, 5, 8, 13]
data2 = [1, 2]
data3 = [0, 1, 1, 2, 4]
data4 = []

def test_check_fib1():
    assert check_fib(data1)


def test_check_fib2():
    assert not check_fib(data2)


def test_check_fib3():
    assert not check_fib(data3)


def test_check_fib4():
    assert not check_fib(data4)



