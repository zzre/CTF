import string
from pwn import *
from shlex import quote

p = process(['gdb', 'chall'])
execute = lambda x: p.sendlineafter("gdb-peda$", x)

base = 0x7ffff7fdaad2
offset = 0x64

flag = 'kalmar{'
idx = len(flag)

execute('b*0x4012f2')
while flag[-1] != '}':
    for c in string.printable.strip():
        execute(f'r <<< {quote(flag + c)}')
        execute(f'x/c {base+2500*idx+offset}')
        res = int(p.recvlineS().split(':\t0x')[-1], 16)
        if res == 0:
            flag += c
            idx += 1
            print(flag)
            break

