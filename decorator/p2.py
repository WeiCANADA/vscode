"""
Write a function called show_args which accepts a function and returns another function. 
Before invoking the function passed to it, show_args should be responsible for printing two things: 
a tuple of the positional arguments, and a dictionary of the keyword arguments.
"""

from functools import wraps


def show_args(fn):
    @wraps(fn)
    def with_show_args(*args,**kwargs):
        print(f' Here are the args:{args} \n Here are the kwargs: {kwargs}')
        return fn(*args,**kwargs)
    return with_show_args

@show_args
def do_something(*args,**kwargs):
    pass

print(do_something(1, 2, 3,a="hi",b="bye"))