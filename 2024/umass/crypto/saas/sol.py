from pwn import *
context.log_level = 'critical'

FLAG = b'UMASS{6Huff3d_2_b1t5'
prefix = FLAG.hex()

while True:
    flag_bits = []
    while True:
        # p = process(['python3', 'saas.py'])
        p = remote('shuffling-as-a-service.ctf.umasscybersec.org', 1337)

        p.recvuntil(b': \n')
        shuffled = int(p.recvlineS(), 16)

        offset = 10

        p.sendlineafter(b':', '00'*offset + prefix + '00'*(128 - offset - len(prefix)//2))
        res = int(p.recvlineS(), 16)

        if shuffled & res == res:
            break

        p.close()

    for i in range(8):
        pay = '00'*offset + prefix + hex(1 << i)[2:].zfill(2)
        pay += pay.ljust(128*2, '0')
        p.sendlineafter(b':', pay)
        res = int(p.recvlineS(), 16)
        if shuffled & res == res:
            flag_bits = [1] + flag_bits
        else:
            flag_bits = [0] + flag_bits

    p.close()

    print(flag_bits, int.to_bytes(int(''.join(str(i) for i in flag_bits), 2), len(flag_bits)//8, 'big'))
    FLAG = FLAG + int.to_bytes(int(''.join(str(i) for i in flag_bits), 2), len(flag_bits)//8, 'big')
    prefix = FLAG.hex()
    print(FLAG)

    if FLAG.endswith(b'}'):
        break

print(f'Flag : {FLAG.decode()}')
