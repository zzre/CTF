import base64
from pwn import *
# context.log_level='debug'

gdb = process(['gdb'])
execute = lambda x: gdb.sendlineafter(b'(gdb)', x)
execute(b'catch syscall')
def get_value(i):
    execute(f'file chal{i}')
    execute(b'run')
    execute(b'x/24xb $rsp')
    res = ''
    for i in range(3):
        x = gdb.recvlineS().split(':')[1].split()
        res += ''.join(map(lambda z: z[2:].rjust(2, '0'), x))
    print(res)
    return res.encode()

p = remote("83.136.254.221", 44120)

for i in range(128):
    p.recvuntil(b'ELF:  ')
    data = p.recvline()
    with open(f"chal{i}", "wb") as f:
        f.write(base64.b64decode(data))
    p.sendlineafter(b"Bytes?", get_value(i))

p.interactive()