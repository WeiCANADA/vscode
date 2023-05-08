import os
print(os.getcwd())
print(os.path.abspath(__file__))

# a method to read a file
def read_file(file_name):
    with open(file_name, 'r') as f:
        for line in f:
            print(line,end="")
# a method to write a file
def write_file(file_name):
    with open(file_name, 'a') as f:
        f.write("0123456789abcdef\n")

# a method to read a file









