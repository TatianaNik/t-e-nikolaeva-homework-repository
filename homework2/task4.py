"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.
"""
from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}  # this is dict with cashed values

    def wrapper(*args):
        cache_key = tuple(args)
        if cache_key in cache_dict:
            return cache_dict[cache_key]
        else:
            cache_dict[cache_key] = func(*args)
            return cache_dict[cache_key]
    return wrapper


@cache
def fun(a, b):
    return (a ** b) ** 2
