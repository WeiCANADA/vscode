names = ['Cecilia', 'Lise', 'Marie']
counts = [len(n) for n in names]
print(counts) # >>>[7, 4, 5]

longest_name = None
max_count = 0

#
print(f'longest name is {names[counts.index(max(counts))]}')

# Enumerate provides concise syntax for looping over 
# an iterator and getting the index of each item from the iterator as you go.
for i, name in enumerate(names):
    count = counts[i]
    if count > max_count:
        longest_name = name
        max_count = count

#zip provides a concise syntax for traversing lists in parallel
for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_count = count

#zip truncates its output silently if you supply it with iterators of different lengths

#zip_longest function from the itertools built-in module
import itertools
for name, count in itertools.zip_longest(names, counts):
    print(f'{name}: {count}')


'''
Things to Remember
✦ The zip built-in function can be used to iterate over multiple iterators
in parallel.
✦ zip creates a lazy generator that produces tuples, so it can be used
on infinitely long inputs.
✦ zip truncates its output silently to the shortest iterator if you supply
it with iterators of different lengths.
✦ Use the zip_longest function from the itertools built-in module
if you want to use zip on iterators of unequal lengths without
truncation.
'''
