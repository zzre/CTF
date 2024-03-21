from pwn import *
from Crypto.Util.number import *

# p = process(['python3', 'chal.py'])
p = remote('integral-communication.chal.irisc.tf', 10103)

payload = b'00'*(16*5)
p.sendlineafter(b'> ', b'2')
p.sendlineafter(b'IV: ', b'00'*16)
p.sendlineafter(b'Command: ', payload)
data1 = bytes.fromhex(p.recvlineS().split(': ')[1])

target = b'{"from": "admin", "act": "flag"}'
payload = xor(data1[16:32], target[16:32])
p.sendlineafter(b'> ', b'2')
p.sendlineafter(b'IV: ', b'00'*16)
p.sendlineafter(b'Command: ', payload.hex().encode())
data2 = bytes.fromhex(p.recvlineS().split(': ')[1])

IV = xor(data2[:16], target[:16])
payload += b'\x00'*16
p.sendlineafter(b'> ', b'2')
p.sendlineafter(b'IV: ', IV.hex().encode())
p.sendlineafter(b'Command: ', payload.hex().encode())

p.interactive()