from homework1.task3 import find_max_and_min


file = "Some_file.txt"


def test_check_find_max_and_min():
    assert find_max_and_min(file) == (1, 6)
