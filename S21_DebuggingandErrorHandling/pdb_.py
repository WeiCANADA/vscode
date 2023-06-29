# Debuggling with pdb
import pdb
first = 'First'
second = 'Second'
result = first+second
pdb.set_trace()
third = 'Third'
result += third
print(result)

# import pdb
# pdb.set_trace()

# Common PDB Commands:
# l (list)
# n (next line)
# p (print)
# c (continue - finishes debugging)

# Also, you can use the debugger in VS Code.
