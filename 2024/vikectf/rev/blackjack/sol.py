import ctypes
from pwn import *
context.log_level='debug'

def random():
    global time0, res, turn
    if turn:
        ret = res[0]
    else:
        time0 = (0x348882AF * time0 + 0x394804E7) & 0xffffffff
        tmp = (time0 >> 16) & 0x7fff
        res = [tmp >> 8, tmp & 0xff]
        ret = res[1]
    turn ^= 1
    return ret % 0x34

def get():
    x = random()
    # shape = 'schd'[(x // 0xD) & 0x1F]
    num = (x % 0xD) + 1
    if num > 10:
        num = 10
    return num

def bet():
    global time0, turn
    player = get() + get()
    house = get() + get()
    cur_time = time0
    cur_turn = turn
    cnt = 0
    while player <= 21:
        r = get()
        if player + r > 21:
            break
        else:
            cnt += 1
            player += r

    time0 = cur_time
    turn = cur_turn
    for _ in range(cnt): get()

    while house <= 0x10:
        house += get()

    if house > 21 or player > house:
        return 1, cnt
    elif house == player:
        return -1, cnt
    else:
        return 0, cnt
    
p = process('./blackjack')
# p = remote("35.94.129.106", 3002)
# sleep(0.1)
libc = ctypes.CDLL(None)
time0 = libc.time(None)
turn = 0
res = [0]*2 # high low

n = 0
while True:
    n += 1
    b, cnt = bet()
    p.recvuntil(b'balance: ')
    balance = p.recvlineS()[:-1]
    bal = int(balance)
    if bal*2 > 100000000:
        balance = str(100000000-bal+1)
    while b == -1:
        n += 1
        p.sendlineafter(b'place your bet: ', balance.encode())
        for i in range(cnt):
            p.sendlineafter(b'[h]it or [s]tand?', b'h')
        p.sendlineafter(b'[h]it or [s]tand?', b's')
        b, cnt = bet()
        
    if b == 0:
        balance = '0'
    p.sendlineafter(b'place your bet: ', balance.encode())
    for i in range(cnt):
        p.sendlineafter(b'[h]it or [s]tand?', b'h')
    p.sendlineafter(b'[h]it or [s]tand?', b's')
            
    if b and bal*2 > 100000000:
        break

for i in range(n, 50):
    p.sendlineafter(b'place your bet: ', b'0')
    p.sendlineafter(b'[h]it or [s]tand?', b's')

p.interactive()