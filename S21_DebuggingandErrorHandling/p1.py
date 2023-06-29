
# RAISE ERROR

def colorize(text, color):
    colors = ('cyan', 'yellow', 'blue', 'green', 'magenta')
    if type(text) is not str:
        raise TypeError('text must be instance of str')
    if color not in colors:
        raise ValueError('color is invalid color')
    print(f'Printed {text} in {color}')


colorize('hello', 'red')
colorize(34, 'red')

# TRY EXCEPT ELSE FINALLY   (else and finally are optional)


def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None


d = {'name': 'Rahul'}
print(get(d, 'name'))
print(get(d, 'city'))


def divide(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        print('dont divide by zero')
    except TypeError as err:
        print('a and b must be int or float')
        print(err)
    else:
        print(f'{a} divided by {b} is {result}')
    finally:
        print('executing finally')


print(divide(1, 2))
print(divide(1, 'a'))
print(divide(1, 0))
