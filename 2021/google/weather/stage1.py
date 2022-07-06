import gdb
import string

gdb.execute("file ./weather")
gdb.execute("start")
gdb.execute("code")
gdb.execute("b*$code+0x214c")

for c in string.printable:
    print(f"[-] {c}")
    gdb.execute(f"r <<< {c} > /dev/null")
    
    if gdb.parse_and_eval("$eax") == 0:
        print(f"[+] found! {c}")
        #gdb.execute("q")
        break