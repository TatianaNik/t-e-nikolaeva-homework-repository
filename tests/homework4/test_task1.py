import pytest
import os

from homework4.task1 import read_magic_number


def write_to_file(file_name, str_of_numbers):
    file_name.write(str_of_numbers)
    file_name.close()
    return file_name


# str1 = "2\n, 3, 4, 5"


@pytest.fixture
def tmp_file():
    # some file setup
    fl = open('tmp_file', 'w')
    yield write_to_file(fl, str1)
    # teardown
    os.remove('tmp_file')


# def test_read_magic_number_true_case(tmp_file):
#     assert read_magic_number(tmp_file.name)


str1 = "0\n, 8, 9, 0"


# def test_read_magic_number_false_case(tmp_file):
#     assert not read_magic_number(tmp_file.name)



def test_file_not_found_case(capsys):
    read_magic_number('t_file')
    captured = capsys.readouterr()
    assert captured.out == "file not found\n"



# str1 = "wrong_str"
#
# def test_read_magic_number_value_error(tmp_file):
#     with pytest.raises(ValueError):
#          read_magic_number(tmp_file.name)
