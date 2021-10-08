from homework2.task2 import major_and_minor_elem

inp1 = [2, 2, 1, 1, 3, 2, 2]

inp2 = [4, 4, 4, 4, 5, 5, 5, 1]

def test_check_most_common_and_least_common_elem1():
    assert major_and_minor_elem(inp1) == (2, 3)


def test_check_most_common_and_least_common_elem2():
    assert major_and_minor_elem(inp2) == (4, 1)

