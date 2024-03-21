import string
from pwn import *
from tqdm import tqdm
from itertools import combinations_with_replacement
context.log_level='critical'

lst = [dict() for _ in range(4)]
for c in string.printable.strip():
    flag = ' '*12 + c*4
    p = process(['./handout', flag])
    p.recvuntil(b'BadMagic([')
    for idx, val in enumerate(p.recvlineS()[:-3].split(', ')):
        lst[idx][c] = val

for m in tqdm(combinations_with_replacement(string.printable.strip(), 3)):
    try:
        if ''.join(m) == '4LL':
            continue
        magic = ''.join(m)
        flag = ' '*13 + magic

        p = process(['./handout', flag])
        p.recvuntil(b'BadMagic([')
        res = p.recvlineS()[:-3].split(', ')
        if (lst[0][m[0]], lst[1][m[1]], lst[3][m[0]]) != (res[0], res[1], res[3]):
            print(m)
            break
        p.close()
    except:
        print(m)
        break