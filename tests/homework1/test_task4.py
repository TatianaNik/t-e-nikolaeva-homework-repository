from homework1.task4 import check_sum_of_four

m = [1, -1, 2, -2]
e = [0, 1, 2, -2]
o = [1, -3, 3, -1]
p = [-1, 0, 1, 1]

def test_check_sum_of_four():
    assert check_sum_of_four(m, e, o, p) == 7

x = [1, 1, 1, 1]
y = [2, 2, 2, 2]
z = [1, 1, 1, 1]
w = [2, 2, 2, 2]

def test_check_sum_of_four2():
    assert check_sum_of_four(x, y, z, w) == 0
