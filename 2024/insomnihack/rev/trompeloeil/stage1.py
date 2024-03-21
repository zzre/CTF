import string
from winpwn import *
context.windbg = "C:\\Users\\zzre\\AppData\\Local\\Microsoft\\WindowsApps\\WinDbgX.exe"

p = process([".\\Trompe-Loeil.exe"])

script = '''
bp Trompe_Loeil+0x456A ".printf \\"%mu\\n\\", @rax+0xc;";
bp Trompe_Loeil+0x45E7 ".printf \\"%mu\\n\\", @rax+0xc;";
'''
p.recvuntil('Guess the flag:')
p.sendline(string.printable.strip())
windbg.attach(p, script=script) # attach 후 go로 breakpoint에 진입해 비교 문자열 획득

p.close()
