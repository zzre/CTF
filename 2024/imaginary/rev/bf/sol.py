import re

with open("bf.txt", 'r') as f:
    data = f.read()

    pattern = r'^>>(\++)\[<(\++)\>-\]<\[-<\+\>\]<(-+)'
    for line in data.split(',')[1:]:
        m = re.search(pattern, line)
        x, y, z = m.groups()
        print(chr(len(z) - len(x)*len(y)), end='')