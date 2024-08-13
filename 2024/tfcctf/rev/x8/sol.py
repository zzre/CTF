import gdb
import string
import shlex

gdb.execute("file ./x8")
gdb.execute("b*0x0000555555567080") # <<x8::instruction::CmpReg8Reg8 as x8::instruction::Instruction>::execute>

flag = 'TFCCTF{'

while flag[-1] != '}':
    for c in string.printable.strip():
        gdb.execute(f"r --file program.bin <<< {shlex.quote(flag + c)}")
        for i in range(len(flag)):
            gdb.execute("continue")

        try:
            rsi = int(gdb.parse_and_eval('$rsi'))
            a = gdb.execute(f"x/b $rsi+1025+3", to_string=True).split()[-1]
            b = gdb.execute(f"x/b $rsi+1025+5", to_string=True).split()[-1]
            if a == b:
                flag += c
                print('[*]', flag)
                break
            else:
                print("!", flag+c)
        except KeyboardInterrupt:
            exit()

    else:
        break

print(flag)