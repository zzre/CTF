from pwn import *

def go(i):
    with open(f'data{i}', 'rb') as f:
        data = f.read()

    target = b'\x00tac'
    ans = []
    for i in range(5):
        idx = data.index(target)
        q = idx // 0x74
        r = idx % 0x74
        ans = [r // 4] + ans
        target = p32(q)

    return [alpha[i] for i in ans]

alpha="abcdefghijklmnopqrstuvwxyz_{}"

ans = []
for i in range(1, 8):
    ans += go(i)

print(''.join(ans))
