from pwn import *

# flag : 37bytes
# state[48] ~ state[59]: 0 -> leak 8 bytes

flag = b''
for i in range(5):
    # p = process(['python3', 'chal.py'])
    p = remote('babycha.chal.irisc.tf', 10100)

    p.sendlineafter(b'> ', b'1')
    p.sendlineafter(b'? ', b'A'*(48 - 8*i))

    p.sendlineafter(b'> ', b'2')
    flag_enc = bytes.fromhex(p.recvlineS()[:-1])
    flag += flag_enc[8*i:8*(i+1)]
    p.close()

print(flag)
