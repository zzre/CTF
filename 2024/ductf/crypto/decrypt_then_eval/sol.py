from pwn import *
from Crypto.Cipher import AES

# p = process(['python3', 'decrypt-then-eval.py'])
p = remote("2024.ductf.dev", 30020)

def go(pay):
    p.sendlineafter(b'ct: ', pay.encode())
    return p.recvline()

pay = None
enc_iv = []
for i in range(256):
    res = go(hex(i)[2:].rjust(2, '0'))
    if res != b'invalid ct!\n':
        enc_iv.append(i ^ res[0])
        break

pay = enc_iv[0] ^ ord('I')

for i in range(256):
    res = go((p8(pay) + p8(i)).hex())
    if res != b'invalid ct!\n':
        enc_iv.append(i ^ ord('V'))
        IV = eval(res)
        break

pay = xor(enc_iv, b'KE')
for i in range(256):
    res = go((pay + p8(i)).hex())
    if res != b'invalid ct!\n':
        KEY = eval(res)
        break

aes = AES.new(KEY, AES.MODE_CFB, IV, segment_size=128)
enc = aes.decrypt(b'\x00'*4)
pay = xor(enc, b'FLAG')

print(go(pay.hex()))

p.interactive()

# DUCTF{should_have_used_authenticated_encryption!}