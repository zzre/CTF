'''
Plaintext keyword: CONNOLLYROCKS
Indicator keyword: HSCTF
Indicator position: A
Ciphertext: LZXORNZBUYWNRARNOVGCLSQWJEFJFE
'''

import string

alpha = string.ascii_uppercase
pt = 'CONLYRKS'

x = list(set(alpha) - set(pt))
x.sort()

pt += ''.join(x)
print(pt)

indicator = 'HSCTF'
keys = []

for c in indicator:
    idx = alpha.index(c)
    key = alpha[idx:] + alpha[:idx]
    
    idx = pt.index('A')
    key = key[-idx:] + key[:-idx]
    print(key)

    keys.append(key)

ct = 'LZXORNZBUYWNRARNOVGCLSQWJEFJFE'

flag = ''
for i, c in enumerate(ct):
    idx = keys[i % 5].index(c)
    flag += pt[idx]

print("flag{"+flag+"}")