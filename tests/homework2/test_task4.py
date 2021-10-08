from homework2.task4 import cache

# probably @cache is not necessary
@cache
def fun(a, b):
    return (a ** b) ** 2

# This test is finished with exit code 5
# But the lines below worked properly when called within the task4
cache_func = cache(fun)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
print(val_1 is val_2)
