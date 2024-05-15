import string
cs = string.ascii_lowercase

enc = 'k_1h3S40s309}jS25l{S1sXJ0fLV6U!'
# enc = 'O94woI936wia82ltxNI14NiB60rzK8wbvILjiZ'
prefix = set('spartan')
for offset in range(len(cs)):
    res = set()
    for c in enc:
        if c in cs:
            res.add(cs[(cs.index(c)+offset) % len(cs)])
    print(offset, res, res & prefix == prefix)

offset = 8
pt = ''

for c in enc:
    if c in string.ascii_lowercase:
        pt += string.ascii_lowercase[(string.ascii_lowercase.index(c) + offset) % len(string.ascii_lowercase)]
    elif c in string.ascii_uppercase:
        pt += string.ascii_uppercase[(string.ascii_uppercase.index(c) + offset) % len(string.ascii_uppercase)]
    elif c in string.digits:
        pt += string.digits[(string.digits.index(c) + offset) % len(string.digits)]
    else:
        pt += c

print(pt)

# https://www.geeksforgeeks.org/rail-fence-cipher-encryption-decryption/
def decryptRailFence(cipher, key):
    rail = [['\n' for i in range(len(cipher))]
                for j in range(key)]
    
    dir_down = None
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        rail[row][col] = '*'
        col += 1
         
        if dir_down:
            row += 1
        else:
            row -= 1
             
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and
            (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1
         
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False
             
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
             
        if dir_down:
            row += 1
        else:
            row -= 1
    return("".join(result))

from pwn import ror

offset = 0
rail = 8

# for rail in range(2, len(pt)):
#     for offset in range(len(pt)):
#         print(rail, offset, decryptRailFence(ror(pt, offset), rail))

print(decryptRailFence(ror(pt, 0), 8))
