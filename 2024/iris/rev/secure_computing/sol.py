import re
from z3 import *

# seccomp-tools dump ./chal_patched -l 8 > seccomp.txt
with open('./seccomp.txt', 'r') as f:
    code = f.read().split('\n')[2:]

s = Solver()
A = BitVec('A', 64)
X = BitVec('X', 64)
mem = [BitVec(f'mem_{i}', 64) for i in range(16)]
args = [BitVec(f'args_{i}', 64) for i in range(6)]
orig_args = [_ for _ in args]
arch = 0xc000003e # AUDIT_ARCH_X86_64
sys_number = 0x1337
offset = 34

for i in range(6):
    for j in range(8):
        c = Extract((j+1)*8 - 1, j*8, orig_args[i])
        s.add(And(0x20 < c, c < 0x7f))

for c in code:
    line = c[offset:]
    res = re.search('if \((.*)\) goto (\d+)', line)
    if res:
        comp, n = res.groups()
        if 'KILL' in code[int(n)]:
            exec(f's.add(Not({comp}))')
        else:
            exec(f's.add({comp})')
    elif re.search('return', line):
        continue
    else:
        res = re.search('(.*) = (.*) >> (.*)', line)
        if res:
            lst = res.groups()
            exec(f'{lst[0]} = LShR({lst[1]}, {lst[2]})')
        else:
            exec(line)

    A = A & 0xFFFFFFFF
    X = X & 0xFFFFFFFF

while True:
    if s.check() != sat:
        break

    m = s.model()
    res = [int(m[i].as_long()) for i in orig_args]

    print(''.join(map(lambda x: x.to_bytes(64, 'little').decode(), res)))
    check = And([orig_args[i] == res[i] for i in range(6)])
    s.add(check == False)