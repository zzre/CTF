from z3 import *

xor = [161, 163, 173, 185, 193, 203, 211, 235, 241, 253, 1, 15, 19, 25, 27, 55, 69, 85, 87, 99, 105, 109, 129, 139, 145, 151, 157, 165]
add = [0, 1, 7, 2, 5, 8, 16, 3, 19, 6, 14, 9, 9, 17, 17, 4, 12, 20, 20, 7, 7, 15, 15, 10, 23, 10, 111, 18]
res = [1374542625 + 1686915720 + 1129686860, 842217029 + 1483902564, 1868013731, 584694732 + 1453312700, 223548744, 1958883726 + 1916008099, 1829937605 + 1815356086 + 253836698]

s = Solver()
city = [BitVec(f'x{i}', 32) for i in range(28)]

s.add(city[0] == ord('T'))

go = [0]*28
for i in range(28):
    s.add(Or(And(0x20 <= city[i],city[i] <= 0x7f), city[i] == 0))
    go[i] = ((city[i] ^ xor[i]) + add[i]) & 0xff
    
x = [0]*7

for i in range(7):
    # x[i] = ((go[i*4 + 3] << 24) | (go[i*4 + 2] << 16) | (go[i*4 + 1] << 8) | go[i*4]) ^ res[i]
    s.add(((go[i*4 + 3] << 24) | (go[i*4 + 2] << 16) | (go[i*4 + 1] << 8) | go[i*4]) == res[i])

# s.add(x[0]^x[1]^x[2]^x[3]^x[4]^x[5]^x[6] == 0)

print(s.check())

while True:
    if s.check() != sat:
        break

    m = s.model()
    res = [int(m[i].as_long()) for i in city]

    print(''.join(map(chr, [res[i] for i in range(28)])))
    check = And([city[i] == res[i] for i in range(28)])
    s.add(check == False)
