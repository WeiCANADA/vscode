# doctests_demo.py
# This module demonstrates the use of the doctest module.
# write a doctest for this function

def add(a, b):
    '''
    >>> add(1, 2)
    3
    >>> add(100, 200)
    400
    '''
    return a + b

if __name__ == '__main__':
    import doctest
    #doctest.testmod()
    doctest.testmod(verbose=True)
