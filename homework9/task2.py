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
        try:
        except:
        os.chdir(self.path)

    def __exit__(self, *args):
        os.chdir(self.cwd)