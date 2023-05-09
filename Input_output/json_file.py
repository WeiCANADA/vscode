import json
x = [1, 'simple', 'list']
with open(r'Input_output\test.txt', 'a') as f:
    # json.dump(x, f)
    s = json.dumps(x)
    f.write(s)