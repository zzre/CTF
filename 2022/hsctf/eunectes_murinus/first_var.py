import re

with open("disasm.txt", 'r') as f:
    code = f.read()

code = code.split("LOAD_CONST              5: 'Failed'")[1:]
code = code[:-1]

i = 0
for c in code:
    idx = c.find("LOAD_FAST               ") + len("LOAD_FAST               ")
    x = 'x[' + c[idx:idx+2].strip(":") + ']'
    i += 1

    idx = c.find("STORE_FAST              ") + len("STORE_FAST              ")
    c = c[idx:]

    idx = c.find('\n')

    com = re.compile("[a-z]{2,}")
    var = com.findall(c[:idx])

    print(f"{var[0]} = {x}")

# print(i)