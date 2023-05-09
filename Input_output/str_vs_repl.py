s = 'Hello,world!'
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
def test(kwargs):
    print(kwargs)
test(table)

def test(**kwargs):
    print(kwargs)
test(**table)