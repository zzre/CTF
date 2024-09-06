from pwn import *
import json
from Crypto.Util.number import *

# p1 = process(['python3', 'challenge.py'])
# p2 = process(['python3', 'challenge.py'])
p1 = remote("54.78.163.105", 32333)
p2 = remote("54.78.163.105", 32333)

p1.sendlineafter(b'>', b'd')
pay = {"f":"flag", "i":0, "j":100}
p1.sendlineafter(b'>', json.dumps(pay))
p1.recvuntil(b'updated to ')

sleep(2)

p1.sendlineafter(b'>', b'i')
x = '\x00'*len("BHFlagY{AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA}")
pay1 = {"f":"flag", "i":0, "j":x}

p2.sendlineafter(b'>', b'i')
pay2 = {"f":"flag", "i":0, "j":""}
context.log_level='debug'

p1.sendlineafter(b'>', json.dumps(pay1))
p2.sendlineafter(b'>', json.dumps(pay2))

p1.recvuntil(b'updated to ')
p2.recvuntil(b'updated to ')

null_enc = int(p1.recvlineS(), 16)
flag_enc = int(p2.recvlineS(), 16)

print(long_to_bytes(null_enc ^ flag_enc))

p1.interactive()