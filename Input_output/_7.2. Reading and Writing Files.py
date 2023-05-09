
# with open(r'C:\Users\NB0590\vscode\Input_output\test.txt', 'r+',encoding="utf-8") as f:
'''
with open(r'Input_output\test.txt',encoding="utf-8") as f:
  for line in f:
    print(line,end="")


    # print(f.read())
#Input_output\test.txt
    # print(f.readline())
with open(r'Input_output\test.txt', 'a',encoding="utf-8") as f:
  f.write("0123456789abcdef\n")

with open(r'Input_output\test.txt', 'r+',encoding="utf-8") as f:
  for line in f:
    print(line,end="")
'''
with open(r'Input_output\test.txt', 'r+') as f:
    #print(f.tell())
    index = f.seek(10)
    print(index)
    print(f.read(1))
