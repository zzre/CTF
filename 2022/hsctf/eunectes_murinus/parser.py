import re

with open("chall.py", "r") as f:
    code = f.read()

with open("first_var", "r") as f:
    first_vars = ['akimotoite = x[50]'] + f.read().split('\n')[:-1]

code = code.split("encode()\n")[1]
code = code.split("    return x32('Success')")[0]
code = code.split("\n        return print('Failed')\n")[:-1]


f = open("sol.py", "w")

data = '''
from z3 import *
import subprocess

s = Solver()
x = [BitVec(f'x{i}', 8) for i in range(58)]

s.add(And(
    x[0] == ord('f'),
    x[1] == ord('l'),
    x[2] == ord('a'),
    x[3] == ord('g'),
    x[4] == ord('{'),
    x[57] == ord('}')
))

for i in range(5, 57):
    s.add(
        Or(
            And(ord('a') <= x[i], x[i] <= ord('z')),
            And(ord('0') <= x[i], x[i] <= ord('9')),
            #And(ord('A') <= x[i], x[i] <= ord('Z')),
            x[i] == ord('_')
        )
    )

'''

for ii, c in enumerate(code):
    line1, line2 = c.split('\n')
    line1 = line1.split('    ')[1]
    line2 = line2.split("if ")[1]

    # print(line1)
    com = re.compile("[a-z]{2,}")
    var = com.findall(line1)
    # print(var)

    com = re.compile("\d{1,2}")
    line1 = com.findall(line1)

    line1 = list(map(lambda x: 'x[' + x + ']', line1))
    line2 = line2.replace("!=", "==")

    data += f"{first_vars[ii]}\n"
    data += f"{var[0]}={line1[0]}\n{var[1]} = {line1[2]}\n"
    data += "s.add(" + line2[:-1] + ')\n'

data += '''
while True:
    if s.check() != sat:
        break

    m = s.model()
    res = [int(m[i].as_long()) for i in x]
    flag = ''.join(map(chr, [res[i] for i in range(58)]))

    print(f"[-] try : {flag}")

    p = subprocess.Popen(["python3.9", "eunectes-murinus.pyc"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stderr, stdout = p.communicate(flag.encode())

    if b"Success" in stderr:
        print()
        print(f"[*] flag : {flag}")
        break
'''

f.write(data)
f.close()