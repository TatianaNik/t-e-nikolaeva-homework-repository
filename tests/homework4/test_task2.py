import pytest
from homework4.task2 import count_dots_on_i


class MockRequest(object):
    def __init__(self, data):
        self.data = data

    def read(self):
        return self.data.encode('utf-8')


def test_count_dots_on_i_mock(mocker):
    m = mocker.patch('urllib.request.urlopen', return_value=MockRequest("iii"))
    assert count_dots_on_i(m) == 3


def test_count_dots_on_i_value_error():
    with pytest.raises(ValueError):
        count_dots_on_i('https://hkjllkh.com')
