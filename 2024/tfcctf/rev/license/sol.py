from pwn import *

license = []
s1 = 'Xsl3BDxP'

for i, c in enumerate(s1.encode()):
    tmp = c ^ 0x33

    if i % 3 == 2:
        license.append((tmp + 37) & 0xff)
    elif i % 3 == 1:
        license.append((tmp - 16) & 0xff)
    else:
        license.append(tmp ^ 0x5a)

license.append(ord('-'))

s2 = 'mzXaPLzR'

for i, c in enumerate(s2):
    tmp = 0

    if c in string.ascii_uppercase:
        tmp = string.ascii_uppercase.index(c) + 48
        while chr(tmp) not in string.ascii_uppercase:
            tmp += 26

    else:
        tmp = string.ascii_lowercase.index(c) + 92
        while chr(tmp) not in string.ascii_lowercase:
            tmp += 26

    license.append(tmp)

print(license)

# p = process("./license")
p = remote("challs.tfcctf.com", 30378)

p.sendline(bytes(license))

p.interactive()
