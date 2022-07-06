from pwn import *

def decode(str, len):
    res = [0]*len
    arr = b'cFUgdW9ZIGV2aUcgYW5ub0cgcmV2ZU4='
    for i in range(len):
        res[i] = arr[i & 0x1f] ^ str[i]

    return ''.join(map(chr, res))

with open("./libnative-lib.so", 'rb') as f:
    e = f.read()

start = [0xAD884, 0xAD89A, 0xAD8A4, 0xAD8AC, 0xAD8B4, 0xAD8BC]
length = [0x15, 9, 7, 7, 7, 9]
for i in range(6):
    print(decode(e[start[i]:start[i]+22], length[i]))
print()

start = [0xAD9DC, 0xAD9F7, 0xADA50, 0xAD9B4, 0xADA03, 0xADA7A]
length = [0x13, 0xb, 0x29, 3, 4, 0x17]
for i in range(6):
    print(decode(e[start[i]:start[i]+0x29], length[i]))
print()

start = [0xAD9BC, 0xAD9F0, 0xADA38, 0xAD9B4]
length = [0x1f, 6, 0x17, 3]
for i in range(4):
    print(decode(e[start[i]:start[i]+0x29], length[i]))
print()

start = [0xADA08]
length = [7]
for i in range(1):
    print(decode(e[start[i]:start[i]+0x29], length[i]))
print()

start = [0xAF141, 0xAD9F0, 0xADA10, 0xAD9F7, 0xADA92, 0xAD9B8, 0xADA29, 0xADAC1, 0xAD9DC, 0xAD9F7, 0xADA50, 0xAD9B8, 0xADA03, 0xADA7A]
length = [0x25, 6, 0x18, 0xb, 0x2e, 3, 0xe, 0x37, 0x13, 0xb, 0x29, 3, 4, 0x17]
for i in range(len(length)):
    print(decode(e[start[i]:start[i]+0x37], length[i]))
print()


print(decode(bytes([0x0a, 0x35, 0x14, 0x03, 0x09, 0x3e, 0x57]), 7))
print(decode(bytes([0x0f, 0x27, 0x26, 0x13, 0x31, 0x27, 0x5d, 0x3b, 0x3d, 0x22]), 10))
print(decode(bytes([0x20, 0x2a, 0x3c, 0x02, 0x0a, 0x23, 0x7a, 0x35, 0x27, 0x21, 0x3f, 0x55]), 12))
print(decode(bytes([0x07, 0x27, 0x21, 0x06]), 4))
print(decode(bytes([0x0a, 0x35, 0x0a, 0x06, 0x00, 0x3a, 0x50, 0x34]), 8))
print()

print(decode(bytes([12, 53, 10, 17, 1, 37, 74, 51, 38, 41]), 10))
print(decode(bytes([2, 54, 60, 56, 8, 50, 79, 63, 37]), 9))
print(decode(bytes([7, 35, 35, 14, 7, 50]), 6))
print(decode(bytes([13, 39, 56, 2]), 4))
print(decode(bytes([10, 53, 10, 6, 0, 58, 80, 52]), 8))
print(decode(bytes([7, 35, 35, 14, 7, 50, 102, 51, 39, 33, 57]), 11))
print(decode(bytes([15, 47, 54, 2, 10, 36, 92]), 7))
print()

print(decode(bytes([32, 42, 60, 2, 10, 35, 122, 53, 39, 33, 63, 85]), 12))
print(decode(bytes([15, 39, 38, 19, 49, 39, 93, 59, 61, 34]), 10))
print(decode(bytes([10, 53, 20, 3, 9, 62, 87]), 7))
print()

print(decode(bytes([0, 43, 49]), 3))
print(decode(bytes([7, 39, 33, 6]), 4))