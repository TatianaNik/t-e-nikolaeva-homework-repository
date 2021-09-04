from homework1.task5 import find_max_sub_array_sum

nums1 = [1, 3, -1, -1, 3, 5, 6]


def test_1_positive():

    assert find_max_sub_array_sum(nums1, 3) == 14


nums2 = [1, 2, 3, 4, 5, 6, 7, 7]


def test_2_positive():

    assert find_max_sub_array_sum(nums2, 3) == 20
