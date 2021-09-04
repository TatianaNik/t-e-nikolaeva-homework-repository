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

inp1 = [2, 2, 1, 1, 3, 2, 2]
print(major_and_minor_elem(inp1))
