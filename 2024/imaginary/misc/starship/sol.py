from pwn import *

while True:
    p = remote("starship.chal.imaginaryctf.org", 1337)

    p.sendlineafter(b'> ', b'4')
    x = eval(p.recvlineS().split()[2])
    y = eval(p.recvlineS().split()[2])

    d = []
    for a, b in zip(x, y):
        d.append((a+b)//2)
    d.append('friendly')

    p.sendlineafter(b'> ', b'42')
    p.sendlineafter(b': ', ','.join(map(str, d)))

    p.sendlineafter(b'> ', b'2')
    p.sendlineafter(b'> ', b'4')

    if all('friendly' in x for x in [p.recvlineS(), p.recvlineS()]):
        p.interactive()

    p.close()