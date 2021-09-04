from typing import Sequence


def check_fib(data: Sequence[int]) -> bool:

    if data == [0, 1] or data == [0]:
        return True
    elif (len(data) == 0) or ((len(data) == 1) & (data != [0])) or ((len(data) == 2) & (data != [0, 1])):
        return False
    else:
        for i in range(2, len(data)):
            if data[i] != data[i-1] + data[i-2]:
                return False
        return True
