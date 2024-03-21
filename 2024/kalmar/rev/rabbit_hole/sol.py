
from pwn import *

'''
0x403aab -> 0x7ffff7a4253e
0x7ffff7a3c89a -> 0x8007492
'''

'''
# stage 1
swap(5, 20)
swap(8, 9)
swap(5, 10)
swap(7, 18)

# stage 2
rol(ipt[0], 3, 64)
rol(ipt[1], 57, 64)
rol(ipt[2], 41, 64)

# stage 3
swap(13, 23)
swap(8, 10)
swap(11, 12)
swap(20, 7)

# stage 4
compare
'''

lst = [0xFAD96B0B6B630B5B, 0xE8CAC4D0CAEAC6EE, 0xE45AE66BDED0E4C2]

# swap
def swap(arr, x, y):
    arr[x], arr[y] = arr[y], arr[x]
    return arr

x = list(b''.join(map(p64, lst)))
x = swap(x, 20, 7)
x = swap(x, 11, 12)
x = swap(x, 8, 10)
x = swap(x, 13, 23)

# ror
x = bytes(x)
lst = [u64(x[i*8:(i+1)*8]) for i in range(3)]
lst[0] = ror(lst[0], 3, 64)
lst[1] = ror(lst[1], 57, 64)
lst[2] = ror(lst[2], 41, 64)

# swap
x = list(b''.join(map(p64, lst)))
x = swap(x, 7, 18)
x = swap(x, 5, 10)
x = swap(x, 8, 9)
x = swap(x, 5, 20)

flag = bytes(x).decode()
print(flag)
