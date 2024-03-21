import string
from pwn import *
context.log_level='critical'

def go(command):
    p.recvuntil("gdb-peda$")
    p.sendline(command)

flag = 'dice{would_you_like_to_try_the_windows_abi_next_time_685d'

while flag[-1] != '}':
    for c in string.digits + string.ascii_lowercase + '_?}':
        print(f'[-] trying {flag + c} ...')
        p = process(["gdb", "-q", "./pain-plus-plus"])

        go('start')
        go('code')
        go('b*$code+0x23c9')
        go(f'r <<< {flag + c}')
        for i in range(len(flag) + 1):
            go('c')

        res = p.recvuntil(b'wrong!', timeout=0.1)
        if not res:
            flag = flag + c
            print(flag)
            p.close()
            break

        p.close()


p.interactive()