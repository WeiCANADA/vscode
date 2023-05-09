from time import time
from functools import wraps
def timetest(func):
    @wraps(func)
    def with_timetest(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print("Time taken for %s is %s" % (func.__name__, end - start))
        return result
    return with_timetest

@timetest
def sum_gen(n):
    return sum(num for num in range(n))

print(sum_gen(1000000))

@timetest
#DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated, and in 3.8 it will stop working
def sum_list(n):    
    return sum([num for num in range(n)])

print(sum_list(1000000))