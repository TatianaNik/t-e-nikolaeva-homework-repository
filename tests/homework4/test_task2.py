import pytest_mock

from homework4.task2 import count_dots_on_i


def test_count_dots_on_i_mock(mocker):
    m = mocker.patch('urllib.request.urlopen', return_value="iii")
    assert count_dots_on_i(m) == 3
