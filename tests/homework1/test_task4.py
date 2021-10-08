from homework1.task4 import check_sum_of_four

m = [1, 2, 3, 2]
e = [3, 1, 2, 2]
o = [3, 3, 0, 3]
p = [3, 1, 3, -2]

def test_check_sum_of_four():
    assert check_sum_of_four(m, e, o, p) == 1

x = [1, 1, 1, 1]
y = [2, 2, 2, 2]
z = [1, 1, 1, 1]
w = [2, 2, 2, 2]

def test_check_sum_of_four2():
    assert check_sum_of_four(x, y, z, w) == 0
