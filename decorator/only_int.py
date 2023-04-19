'''
only_ints
Write a function called only_ints which accepts a function and returns another function.
 The function passed to it should only be invoked if all of the arguments passed to it are integers. 
Otherwise the inner function should return "Please only invoke with integers.".

@only_ints 
def add(x, y):
    return x + y
    
add(1, 2) # 3
add("1", "2") # "Please only invoke with integers."
'''
from functools import wraps

def only_ints(func):
    @wraps(func)
    def inner(*args,**kwargs):
        if all([type(arg) == int for arg in args]):
            return func(*args,**kwargs)
        return "Please only invoke with integers."
    return inner
'''
        if any([arg for arg in args if type(arg) != int]):
            return "Please only invoke with integers."
        return fn(*args, **kwargs)
'''
@only_ints
def add(x, y):
    return x + y

print(add(1, 2) )# 3   
print(add("1", "2") )# "Please only invoke with integers."