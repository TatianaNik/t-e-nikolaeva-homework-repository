from homework1.task3 import find_max_and_min


from os import path
current_dir = path.dirname(__file__)
filename = path.join(current_dir, "Some_file.txt")


def test_check_find_max_and_min():
    assert find_max_and_min(filename) == (1, 6)
