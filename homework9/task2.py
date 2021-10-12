"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
>>> with supressor(IndexError):
...    [][2]
"""


class supressor:
    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if (exc_type == self.exception) or (exc_type is None):
            return True
        else:
            return False


with supressor(IndexError):
    [][2]
