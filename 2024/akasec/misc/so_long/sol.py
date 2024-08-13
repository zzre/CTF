import base64
from pwn import *
import maze2
# context.log_level='debug'

p = remote("20.80.240.190", 4442)

'''
Welcome to so_long!

Your goal is to find the shortest path from the start point (green square) to the end point (red square).
You can move up, down, left, right, up-left, up-right, down-left, and down-right.
Insert your moves separated by spaces. For example: "up down-right right down".

Good luck!

Round 1/1000:
'''

for i in range(1000):
    print(i)
    p.recvuntil('1000:\n')
    data = p.recvline()
    with open("maze2.png", "wb") as f:
        f.write(base64.b64decode(data))

    res = maze2.solve("maze2.png")
    p.sendlineafter(b'Enter your moves:\n', ' '.join(res[1:]))
    # print(' '.join(res[1:]))
    print(p.recvline())

p.interactive()