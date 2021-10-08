from homework3.hw3_task4 import is_armstrong


def test_is_armstrong():
    assert is_armstrong(153)

def test_negative_case_is_armstrong():
    assert not is_armstrong(10)


