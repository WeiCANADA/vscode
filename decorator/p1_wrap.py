from functools import wraps
def logit(func):
    @wraps(func)# without this, the name of the function will be with_logging
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logit
def addition_func(x):
    """Do some math."""
    return x + x    

@logit
def subtraction_func(x):
    """Do some math."""
    return x - x

print(addition_func(10))
print(subtraction_func(10))
print(addition_func.__name__)