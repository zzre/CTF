from pwn import *

p = remote("travelling-salesman.hsctf.com", 1337)

p.recvuntil(b"==\n")

while True:
    try:
        p.recvuntil("[")
        arr = list(map(int, p.recvline()[:-2].decode().split(',')))

        print(arr)
        arr.sort()

        p.sendline(' '.join(map(str, arr)))

    except:
        p.interactive()