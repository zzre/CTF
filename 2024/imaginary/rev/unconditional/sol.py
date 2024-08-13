import string

target = 'b4,31,8e,02,af,1c,5d,23,98,7d,a3,1e,b0,3c,b3,c4,a6,06,58,28,19,7d,a3,c0,85,31,68,0a,bc,03,5d,3d,0b'.split(',')
target = list(map(lambda x: int(x, 16), target))

table1 = [0x52, 0x64, 0x71, 0x51, 0x54, 0x76]
table2 = [1, 3, 4, 2, 6, 5]

def iterate(a1, v3, counter1, counter2):
    v4 = (a1 & 1) != 0
    v1 = v3 > 0x60 and v3 <= 0x7A
    
    if v4:
        if v1:
            res = v3 ^ table1[counter1]
        else:
            res = ((4 * v3) | (v3 >> 6)) & 0xFF
    else:
        if v1:
            res = ((v3 >> table2[counter2]) | (v3 << (8 - table2[counter2]))) & 0xFF
        else:
            res = (((v3 << 6) | (v3 >> 2)) ^ table1[counter1]) & 0xff

    counter1 = (v4 + counter1) % 6
    counter2 = (v4 + counter2) % 6

    return res, counter1, counter2

def dfs(flag, counter1, counter2):
    if len(flag) == len(target):
        if flag.startswith('ictf{'):
            print(flag)
        return

    for c in string.printable.strip():
        res, ctr1, ctr2 = iterate(len(flag), ord(c), counter1, counter2)
        if res == target[len(flag)]:
            dfs(flag+c, ctr1, ctr2)

dfs('', 0, 0) # ictf{m0r3_than_1_way5_t0_c0n7r0l}
