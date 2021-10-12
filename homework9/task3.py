"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
For dir with two files from hw1.py:
>>> universal_file_counter(test_dir, "txt")
6
>>> universal_file_counter(test_dir, "txt", str.split)
6
"""
from pathlib import Path
from typing import Optional, Callable
import os

def universal_file_counter(
    dir_path: Path, file_extention: str, tokenizer: Optional[Callable] = None
) -> int:

    files = [f for f in os.listdir(dir_path) if f.endswith(file_extention)]
    if tokenizer is None:
        line_count = 0
        for file in files:
            with open(file) as f:
                line_count += len(f.readlines())

        return line_count
    else:
        token_count = 0
        for file in files:
            with open(file) as f:
                tokens = tokenizer(f.read())
                token_count += len(tokens)
        return token_count


test_dir = 'C:/Users/DELL_USER/PycharmProjects/python_homework/homework9'
# print(universal_file_counter(test_dir, "txt"))
print(universal_file_counter(test_dir, "txt", str.split))