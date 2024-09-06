import json
from pwn import *
from Crypto.Util.number import long_to_bytes, getPrime
context.log_level='debug'

p = process(["python3", "t.py"])
# p = remote('18.203.110.195', int(32609))

def encrypt():
    p.sendlineafter(b">", b'e')
    p.recvuntil(b"Flag = ")
    return int(p.recvlineS(), 16)

e1 = encrypt()
r = getPrime(1024)

pay = {"p": r, "q": r}

p.sendlineafter(b">", b'a')
p.sendlineafter(b">", json.dumps(pay))
e2 = encrypt() % (r**2)

p.sendlineafter(b">", b'a')
p.sendlineafter(b">", json.dumps(pay))
e3 = encrypt() % (r**2)

r2 = r**2
tmp = (e3 * inverse_mod(e2, r2)) % r2
y8 = pow(tmp, inverse_mod(0x10001, r*(r-1)), r2)

xy15 = pow(e2, inverse_mod(0x10001, r*(r-1)), r2)

print(y8, r)

def dfs(cur, depth):
    print(depth)
    if depth == 3:
        y = cur
        x = (xy15 * inverse_mod(y, r**2)**15) % (r**2)
        flag = long_to_bytes(int(x))
        if long_to_bytes(int(x)).startswith(b'BHFlagY{'):
            print(flag)
            exit()
        
        x = (xy15 * inverse_mod(y, r**2)**14) % (r**2)
        flag = long_to_bytes(int(x))
        if long_to_bytes(int(x)).startswith(b'BHFlagY{'):
            print(flag)
            exit()
        return

    for nxt in Mod(cur, r).sqrt(all=True):
        dfs(nxt, depth+1)

dfs(y8, 0)

p.interactive()