def cache(times=3):
    def cache_func(func):
        cache_dict = {}  # this is dict with cashed values
        times_dict = {}  # this is dict with how many times the function was called

        def wrapper(*args):
            cache_key = tuple(args)
            if cache_key in cache_dict and times_dict[cache_key] < times:
                times_dict[cache_key] += 1
                return cache_dict[cache_key]
            else:
                cache_dict[cache_key] = func(*args)
                times_dict[cache_key] = 1
                return cache_dict[cache_key]
        return wrapper
    return cache_func


@cache(times=2)
def f():
    return input('? ')


print(f())
print(f())
print(f())








