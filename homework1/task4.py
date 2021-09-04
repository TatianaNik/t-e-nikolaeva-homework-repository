from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:

    n = len(a)
    result = 0
    for i in range(n-1):
        for j in range(n-1):
            for k in range(n-1):
                for g in range(n-1):
                    if (a[i] + b[j] + c[k] + d[g]) == 0:
                        result += 1
    return result


