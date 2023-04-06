#o create an empty set you have to use set(), not {}; 
set_ = set()
set_a = set('abc')
set_b = set('cde')
print(f'{set_a}\n {set_b}')
print(f'{set_a - set_b}')
print(f'{set_a | set_b}')
print(f'{set_a ^ set_b}')
print(f'{set_a & set_b}')