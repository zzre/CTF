from pwn import *
from Crypto.Util.number import long_to_bytes
context.log_level='debug'

res = []

p = process('openssl s_client -connect without-a-trace.chal.uiuc.tf:1337'.split(), stdin=PTY)
p.recvuntil(b'[WAT] Welcome')

param = [1, 1, 1, 1, 1]
for j in param:
    p.sendlineafter(b' = ', str(j))

p.recvuntil(b'Have fun: ')
res.append(int(p.recvlineS()))

p.close()

for i in range(5):
    p = process('openssl s_client -connect without-a-trace.chal.uiuc.tf:1337'.split(), stdin=PTY)
    p.recvuntil(b'[WAT] Welcome')
    
    param = [1, 1, 1, 1, 1]
    param[i] = 2
    for j in param:
        p.sendlineafter(b' = ', str(j))
    
    p.recvuntil(b'Have fun: ')
    res.append(int(p.recvlineS()))
    
    p.close()

for flag in res[1:]:
    print(long_to_bytes(flag - res[0]).decode(), end='')
print()