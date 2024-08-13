from pwn import *
from Crypto.Util.number import long_to_bytes

p = remote("20.80.240.190", 4455)

n = int(p.recvlineS().split('=')[1])
e = int(p.recvlineS().split('=')[1])

lst = []
x = 0
for i in range(303, -1, -1):
    p.sendlineafter(b": ", str(i))
    c = int(p.recvlineS().split('=')[1])
    if pow(x, e, n) == c:
        lst.append(0)
    else:
        lst.append(1)
        x += 1
    x *= 2
    print(i, lst)

p.close()

print(long_to_bytes(int(''.join(map(str, lst)), 2)))
