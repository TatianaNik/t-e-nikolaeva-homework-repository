import pytest
import os

from homework4.task1 import read_magic_number


def write_to_file(file_name, str_of_numbers):
    file_name.write(str_of_numbers)
    file_name.close()
    return file_name


str1 = "2\n, 3, 4, 5"


@pytest.fixture
def tmp_file():
    # some file setup
    fl = open('tmp_file', 'w')
    yield write_to_file(fl, str1)
    # teardown
    os.remove('tmp_file')


def test_read_magic_number_true_case(tmp_file):
    assert read_magic_number(tmp_file.name)

добавить тесты