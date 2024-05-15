import base64
from Crypto.PublicKey import RSA
from Crypto.Util.number import *
from pwn import *
# from math import gcd

context.log_level='debug'
N = []
MSG = []
r = remote('0.cloud.chals.io', 13998)

while True:
    r.sendlineafter(b'>', b'RETRIEVE')
    r.recvuntil(b'-----BEGIN RSA PUBLIC KEY-----\n')
    key = base64.b64decode(r.recvuntilS('-----END RSA PUBLIC KEY-----', drop=True).replace('\n', ''))
    n = RSA.importKey(key).n
    N.append(n)

    r.recvuntil(b'MESSAGE:\r\n')
    msg = bytes_to_long(base64.b64decode(r.recvline()[:-2]))
    MSG.append(msg)

    for nn in N:
        if n != nn and GCD(n, nn) != 1:
            p = GCD(n, nn)
            q = n // p
            phi_n = (p-1)*(q-1)
            d = pow(0x10001, -1, phi_n)
            pt = pow(msg, d, n)
            print(long_to_bytes(pt))
            r.close()
            exit()
    else:
        print(len(N))
