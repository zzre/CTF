from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import random
from tqdm import tqdm
from pwn import *
from collections import defaultdict

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
    return key.hex(), ciphertext.hex()

def decrypt(message):
    key = b''
    for i in range(8):
        key += (get_random_number() % (2 ** 16)).to_bytes(2, 'big')
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(message)
    return plaintext

def next_seed(seed):
    for i in range(8):
        seed = int(str(seed * seed).zfill(12)[3:9])
    return seed

seed_tbl = defaultdict(list) # next_seed : [prev_seed]
tbl = []
for seed in tqdm(range(10 ** 6)):
    seed_tbl[next_seed(seed)].append(seed)
    tbl.append(encrypt(b'')[1])

# p = process(['python3', 'main.py'])
p = remote('betta.utctf.live', 2435)
context.log_level='debug'

for i in range(3):
    p.recvline()
    p.sendlineafter(b'?', b'2')
    p.sendlineafter(b'?\n', b'')
    enc = p.recvline().split()[-1].decode()
    s1 = tbl.index(enc)

    p.sendlineafter(b'?\n', b'1')
    print(s1, seed_tbl[s1])
    for seed in seed_tbl[s1]:
        encrypt(b'')
        key = encrypt(b'')[0]
        p.sendlineafter(b'?\n', key.encode())
        if 'You found the key!' in p.recvlineS():
            break

p.interactive()
