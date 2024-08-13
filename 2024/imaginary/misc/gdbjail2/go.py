from pwn import *

a = "/usr/bin/cat"
b = "/home/user/W4GbJUuvbTGypTHrXAeD.txt"

print('''set debug threads 1
break *read+16
continue
set $rax=59
set $rdi=$rsi
set $rsi=0
set $rdx=0''')

print(f'set $rsi=$rdi')

print(f'set *$rdi=$rsi+32')
print(f'set $rdi=$rdi+4')
print(f'set *$rdi=$rsi>>32')

print(f'set $rdi=$rdi+4')
print(f'set *$rdi=$rsi+256')
print(f'set $rdi=$rdi+4')
print(f'set *$rdi=$rsi>>32')

print(f'set $rdi=$rdi+8')
print(f'set $rdi=$rdi+8')
for i in range(0,len(a), 4):
    x = u32((a[i:i+4]).encode().ljust(4, b"\x00"))
    print(f'set *$rdi={x}')
    print(f'set $rdi=$rdi+4')

print(f'set $rdi=$rsi')

print(f'set $rdi=$rdi+256')
for i in range(0,len(b), 4):
    x = u32((b[i:i+4]).encode().ljust(4, b"\x00"))
    print(f'set *$rdi={x}')
    print(f'set $rdi=$rdi+4')

print(f'set $rdi=$rsi+32')
