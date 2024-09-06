from pwn import *
import base64
import sudokum
import ctypes
from Crypto.Util.number import *
# context.log_level='debug'

lib = ctypes.CDLL('libc.so.6')
p = remote("magnum-opus.chals.sekai.team", 1337, ssl=True)
# p = process(['python3.11', 'magnum_opus.py'])

for t in range(10):
    print(t+1)
    x = p.recvlineS()
    sleep(0.5)
    data = list(map(int, str(bytes_to_long(base64.b64decode(x))).zfill(81)))
    lib.srand(lib.time(0) - 1)

    M = [data[i:i+9] for i in range(0, 81, 9)]
    sol = sudokum.solve(M)[1]

    for _ in range(11):
        i = lib.rand() % 9
        j = lib.rand() % 9
        val = lib.rand() % 9
        sol[i][j] = val + 1

    pay = base64.b64encode(long_to_bytes(int(''.join([''.join(list(map(str,x)))for(x)in sol]))))

    p.sendlineafter(b'> ', pay)

p.interactive()