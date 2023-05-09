
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

# a method to copy a file to another file
def copy_file(file_name, new_file_name):
    with open(file_name, 'r') as f:
        with open(new_file_name, 'w') as f1:
            for line in f:
                f1.write(line)

# a method to copy a file to another file in reverse order
def copy_file_reverse(file_name, new_file_name):
# 定义一个块大小，例如 4KB
    block_size = 4 * 1024

# 以二进制模式打开文件以兼容各种文件类型
    with open(file_name, "rb") as input_file, open(new_file_name, "wb") as output_file:
        # 获取文件大小
        file_size = input_file.seek(0, 2)
        
        # 从文件末尾开始逐块读取和写入
        for block_start in range(file_size, 0, -block_size):
            # 如果块的大小大于剩余字节，则调整块大小
            if block_start < block_size:
                block_size = block_start
            
            # 定位到块的开始位置并读取内容
            input_file.seek(block_start - block_size, 0)
            content = input_file.read(block_size)
            
            # 反转块内容并写入输出文件
            output_file.write(content[::-1])
            output_file.write(content[::-1])



    











