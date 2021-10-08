"""
Write a function that merges integer from sorted files and returns an iterator
file1.txt:
1
3
5
file2.txt:
2
4
6
>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""

from pathlib import Path
from typing import List, Union, Iterator


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    list_of_files = []
    for file in file_list:
        list_of_files.append(open(file))
    numbers = list(map(lambda x: (x.readline()), list_of_files))

    while True:
        min_number = min(numbers)
        if min_number == '1000000':
            break
        index_min_number = numbers.index(min_number)
        numbers[index_min_number] = (list_of_files[index_min_number].readline())
        if numbers[index_min_number] == '':
            numbers[index_min_number] = '1000000'
        yield min_number


file_list1 = ['file1.txt', 'file2.txt']
print(list(merge_sorted_files(file_list1)))

