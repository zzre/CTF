from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import random
from tqdm import tqdm
from pwn import *

def get_random_number():
    global seed
    seed = int(str(seed * seed).zfill(12)[3:9])
    return seed

def encrypt(message):
    key = b''
    for i in range(8):
        key += (get_random_number() % (2 ** 16)).to_bytes(2, 'big')
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(message, AES.block_size))
    return ciphertext.hex()

def decrypt(message):
    key = b''
    for i in range(8):
        key += (get_random_number() % (2 ** 16)).to_bytes(2, 'big')
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(message)
    return plaintext

tbl = []
for seed in tqdm(range(10 ** 6)):
    tbl.append(encrypt(b''))

# p = process(['python3', 'main.py'])
p = remote('betta.utctf.live', 7356)
# context.log_level='debug'

p.sendlineafter(b'?', b'2')
p.sendlineafter(b'?\n', b'')
enc = p.recvline().split()[-1].decode()

seed = tbl.index(enc)
encrypt(b'')

p.sendlineafter(b'?\n', b'1')
flag_enc = bytes.fromhex(p.recvline().split()[-1].decode())
flag = decrypt(flag_enc)
print(flag)

p.close()
