"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.
You may assume that the array is non-empty and the most common element
always exist in the array.
Example 1:
Input: [3,2,3]
Output: 3, 2
Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2, 1
"""

from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:

    major = inp[0]
    minor = inp[0]
    major_count = inp.count(inp[0])
    minor_count = inp.count(inp[0])

    for i in range(0, len(inp)):
        if inp.count(inp[i]) > major_count:
            major = inp[i]
        elif inp.count(inp[i]) < minor_count:
            minor = inp[i]
    return major, minor


# inp1 = [2, 2, 1, 1, 3, 2, 2]
#print(major_and_minor_elem(inp1))
