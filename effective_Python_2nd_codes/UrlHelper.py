from urllib.parse import parse_qs

my_values = parse_qs('red=5&blue=0&green=',
keep_blank_values=True)
print(repr(my_values))

# >> {'red': ['5'], 'blue': ['0'], 'green': ['']}

green = my_values.get('green', [''])[0] or 0
red = my_values.get('red', [''])[0] or 0
opacity = my_values.get('opacity', [''])[0] or 0

#readability is poor
red_str = my_values.get('red', [''])
red = int(red_str[0]) if red_str[0] else 0

#better
green_str = my_values.get('green', [''])
if green_str[0]:
    green = int(green_str[0])
else:
    green = 0

print(f'red: {red!r}')
print(f'green: {green!r}')
print(f'opacity: {opacity!r}')


#reuse this logic repeatedly
def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        return int(found[0])
    return default

print(f'red: {get_first_int(my_values, "red")!r}')





