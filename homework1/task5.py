from typing import List


def find_max_sub_array_sum(nums: List[int], k: int) -> int:

    result = nums[0]

# assume len(nums)>1
    for i in range(0, len(nums)-k+1):
        res_sub_array = nums[i]
        for j in range(1, k):
            if (nums[i+j] + res_sub_array) > res_sub_array:
                res_sub_array = res_sub_array + nums[i+j]

        if res_sub_array > result:
            result = res_sub_array

    return result


# first tests
# nums1 = [1, 3, -1, -1, 3, 5, 6]

# print(find_max_sub_array_sum(nums1, 3))

# nums2 = [1, 5, 5, 5, 10]

# print(find_max_sub_array_sum(nums2, 3))
