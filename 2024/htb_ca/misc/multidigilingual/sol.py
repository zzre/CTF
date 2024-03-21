from pwn import *
from base64 import b64encode

context.log_level = 'debug'

c = remote("94.237.57.161", 38771)

c.recvuntil(b'languages:')

payload = open("sol.c").read()

# print(payload)
c.sendline(b64encode(payload.encode()).decode())
c.interactive()