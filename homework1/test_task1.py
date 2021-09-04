import pytest

from homework1.task1 import check_power_of_2()

def test_positive_case():
    assert check_power_of_2(1024)
    
def test_negative_case():
    assert not check_power_of_2(14)
