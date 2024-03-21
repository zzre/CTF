from pwn import *
from Crypto.Util.number import *
import secrets

# p = process(['python3', 'chal.py'])
p = remote('dhash.chal.irisc.tf', 10101)

p.recvuntil(b'MySeededHash(')
rcvd = p.recvlineS()
N = int(rcvd.split(', ')[0])
e = 65537

payload = pow(0b110, inverse(e, N-1), N).to_bytes(256, "big")
payload += pow(0b100, inverse(e, N-1), N).to_bytes(256, "big")
payload += pow(0b010, inverse(e, N-1), N).to_bytes(256, "big")
p.sendlineafter(b'> ', payload.hex().encode())

p.interactive()