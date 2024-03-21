import gdb
from pwn import xor

gdb.execute("file ./nano")
gdb.execute("set follow-fork-mode parent")
gdb.execute("start")
gdb.execute("code")

bp = gdb.Breakpoint(f'*{gdb.parse_and_eval("$code+0x137b")}')
gdb.execute("r "+"A"*0x28)

KEY = []
for i in range(0x30):
    try:
        val = gdb.parse_and_eval('*(unsigned char*)0x7fffffffe2a7')
        KEY.append(int(val))
        if i > 0x22 and val == 0:
            break
        gdb.execute('continue', to_string=True)
    except:
        break

flag = bytes.fromhex('0C5C60206963640F4F1E333A682A7CD9D5D0C9E7C3F0BCAB9BD7988BAFB0F84749164968')
print(xor(KEY[1:], flag[:len(KEY)]))