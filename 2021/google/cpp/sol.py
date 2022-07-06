from pwn import *
import string
context.log_level='error'

flag = 'CTF{'

l = 5
while l != 27:
    for c in string.printable[:-5]:
        print(f"[-] {flag+c}")
        p = process("./gogo") # gcc -o gogo gogo.c
        payload = flag+c
        p.sendlineafter("> ", payload)
        p.recvuntil(f"count_{l}")
        data = p.recvline()
        p.close()
        print(data)
        if b'00000000' in data:
            flag += c
            l += 1
            break

print(flag+"}")
