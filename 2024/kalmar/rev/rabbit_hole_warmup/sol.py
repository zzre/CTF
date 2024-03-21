from z3 import *

'''
breakpoints
0x7ffff7f548ec

flag check
0x401d19
'''

def concat(lst):
    res = 0
    for i, val in enumerate(lst):
        res += val << (i*8)
    return res

s = Solver()
flag = [BitVec(f'flag_{i}', 64) for i in range(36)]

# flag format
s.add(flag[0] == ord('k'))
s.add(flag[1] == ord('a'))
s.add(flag[2] == ord('l'))
s.add(flag[3] == ord('m'))
s.add(flag[4] == ord('a'))
s.add(flag[5] == ord('r'))
s.add(flag[6] == ord('{'))
s.add(flag[-1] == ord('}'))

# magic
s.add(flag[13] == ord('4'))
s.add(flag[14] == ord('L'))
s.add(flag[15] == ord('L'))

for c in flag:
    s.add(And(0x20 < c, c <= 0x7f))

'''
1. flag[5:9] * flag[-4:] == 0x3807D9F2865ACBFA
2. flag[5:9] * flag[-8:] == 0xb24e2f293372cb2c
'''

MASK = 0xffffffffffffffff
s.add((concat(flag[5:9]) * concat(flag[-4:])) & MASK == 0x3807D9F2865ACBFA)
s.add((concat(flag[5:9]) * concat(flag[-12:-4])) & MASK == 0xb24e2f293372cb2c)
s.add((concat(flag[9:11]) * concat(flag[11:13])) & 0xffffffff == 0x914af60)
s.add((concat(flag[16:24]) / concat(flag[9:11])) & MASK == 0x1afb1b1238743)
s.add((concat(flag[24:28]) ^ concat(flag[16:20])) & 0xffffffff == 0x1b41001f)

assert s.check() == sat, "unsat"
m = s.model()
ans = [chr(m[c].as_long()) for c in flag]
print(''.join(ans))
