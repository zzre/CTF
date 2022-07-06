from pwn import *
from itertools import combinations
context.log_level='debug'

p = remote("vending-machine.hsctf.com", 1337)

p.recvuntil(b"==\n")

p.sendline("Display")
p.recvuntil(b"Items: \n")

items = p.recvuntil(b"\n\n").decode()
items = items.split(":")

items = list(map(lambda x: int(x[:-2]), items[1:]))
print(items)

p.recvuntil(b"Coins: \n")
coins = p.recvuntil(b"\n\n").decode()
coins = coins.split(":")

coins = list(map(lambda x: int(x[:-2]), coins[1:]))
print(coins)

item_backup = items.copy()
coin_backup = coins.copy()

items.sort()
items.reverse()

coins = set(coins)
ans = []

for item in items[:-1]:
    temp = 0
    d = 99999999999999999999
    for i in range(1, len(coins)):
        print(i)
        
        for li in combinations(coins, i):
            s = sum(li)
            if s > item and d > s - item:
                temp = list(li)
                d = s - item
    
    coins -= set(temp)
    print(coins)
    ans.append(temp)

assert sum(coins) > items[-1] # try again
ans.append(list(coins))

print(ans)

for i, li in enumerate(ans):
    for c in li:
        p.sendline(f"Insert {coin_backup.index(c) + 1}")
    p.sendline(f"Buy {item_backup.index(items[i]) + 1}")

p.interactive()