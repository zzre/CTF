with open("s.dump", "rb") as f:
    S = list(f.read())

D = [0]*32
mask = (1 << 32) - 1

def S200():
    D[4] = 5000
    D[0] = 13200
    S337()
    D[0] = 0
    S500()
    S1262()
    print(D[0])
    if D[0] == 0:
        S653()

def S253():
    D[1] = 0

def S261():
    while True:
        D[3] = D[0]
        D[3] %= D[2]
        if D[3] == 0:
            S253()
        D[2] = (D[2] + 1) & mask
        D[3] = D[2]
        D[3] = (D[3] * D[3]) & mask 
        D[3] = (D[3] - D[0]) & mask
        D[3] = (D[3] - 1) & mask
        if D[3] < 0x80000000:
            break

def S322():
    S[D[4]:D[4]+4] = list(int.to_bytes(D[0], 4, 'little'))
    D[4] = (D[4] + 2) & mask

def S337():
    while True:
        D[1] = 1
        D[2] = 2
        S261()
        if 0 < D[1] < 0x80000000:
            S322()
        D[0] = (D[0] + 1) & mask
        D[1] = 13600
        D[1] = (D[1] - D[0]) & mask
        if D[1] >= 0x80000000 or D[1] == 0:
            break

def S397():
    D[0] = 0

def S405():
    D[0] //= 2

def S413():
    D[0] = (D[0] * 3 + 1) & mask

def S428():
    D[1] = D[0]
    D[1] %= 2
    if D[1] == 0:
        S405()
    if 0 < D[1] < 0x80000000:
        S413()
    S470()
    D[0] = (D[0] + 1) & mask

def S470():
    D[1] = (D[0] - 1) & mask
    if D[1] == 0:
        S397()
    if 0 < D[1] < 0x80000000:
        S428()

def S500():
    D[2] = D[0]
    D[2] = (D[0] + 4096) & mask
    D[4] = int.from_bytes(bytes(S[D[2]:D[2]+4]), 'little')
    D[4] &= 255
    if 0 < D[4] < 0x80000000:
        S540()

def S540():
    D[2] = D[0]
    D[2] = (D[2] * 2 + 5000) & mask
    D[2] = int.from_bytes(bytes(S[D[2]:D[2]+4]), 'little')
    D[2] &= 255
    # print(D[2], end=', ')
    # print(D[4])
    D[4] ^= D[2]                        # 입력값에 상수 xor
    D[0] = (D[0] + 1) & mask
    D[2] = D[0]
    S470()
    # print(D[0], end=', ')
    D[4] = (D[4] + D[0]) & 255          # 입력값에 상수 +
    D[0] = D[2]
    D[2] = (D[2] - 1 + 4500) & mask
    S[D[2]:D[2]+4] = list(int.to_bytes(D[4], 4, 'little'))  # 4500 ~ 4528에 D[4] 넣음
    S500()

def S653():
    D[0] = 123456789
    
    D[1] = int.from_bytes(bytes(S[4096:4096+4]), 'little')
    D[0] ^= D[1]
    D[2] = 846786818
    D[2] ^= D[0]
    S[6144:6144+4] = list(int.to_bytes(D[2], 4, 'little'))

    D[1] = int.from_bytes(bytes(S[4096+4:4096+8]), 'little')
    D[0] ^= D[1]
    D[2] = 1443538759
    D[2] ^= D[0]
    S[6144+4:6144+8] = list(int.to_bytes(D[2], 4, 'little'))

    D[1] = int.from_bytes(bytes(S[4096+8:4096+12]), 'little')
    D[0] ^= D[1]
    D[2] = 1047515510 ^ D[0]
    S[6144+8:6144+12] = list(int.to_bytes(D[2], 4, 'little'))

    D[1] = int.from_bytes(bytes(S[4096+12:4096+16]), 'little')
    D[0] ^= D[1]
    D[2] = (359499514 + 1724461856) ^ D[0]
    S[6144+12:6144+16] = list(int.to_bytes(D[2], 4, 'little'))

    D[1] = int.from_bytes(bytes(S[4096+16:4096+20]), 'little')
    D[0] ^= D[1]
    D[2] = 241024035 ^ D[0]
    S[6144+16:6144+20] = list(int.to_bytes(D[2], 4, 'little'))

    D[1] = int.from_bytes(bytes(S[4096+20:4096+24]), 'little')
    D[0] ^= D[1]
    D[2] = 222267724 ^ D[0]
    S[6144+20:6144+24] = list(int.to_bytes(D[2], 4, 'little'))

    D[1] = int.from_bytes(bytes(S[4096+24:4096+28]), 'little') # 도시는 최대 28 바이트
    D[0] ^= D[1]
    D[2] = 844096018 ^ D[0]
    S[6144+24:6144+28] = list(int.to_bytes(D[2], 4, 'little'))

def S1262():
    D[0] = 0

    D[1] = int.from_bytes(bytes(S[4500:4500+4]), 'little')
    D[1] ^= (1374542625 + 1686915720 + 1129686860)
    D[0] |= D[1]

    D[1] = int.from_bytes(bytes(S[4500+4:4500+8]), 'little')
    D[1] ^= (842217029 + 1483902564)
    D[0] |= D[1]

    D[1] = int.from_bytes(bytes(S[4500+8:4500+12]), 'little')
    D[1] ^= 1868013731
    D[0] |= D[1]

    D[1] = int.from_bytes(bytes(S[4500+12:4500+16]), 'little')
    D[1] ^= (584694732 + 1453312700)
    D[0] |= D[1]

    D[1] = int.from_bytes(bytes(S[4500+16:4500+20]), 'little')
    D[1] ^= 223548744
    D[0] |= D[1]

    D[1] = int.from_bytes(bytes(S[4500+20:4500+24]), 'little')
    D[1] ^= (1958883726 + 1916008099)
    D[0] |= D[1]

    D[1] = int.from_bytes(bytes(S[4500+24:4500+28]), 'little')
    D[1] ^= (1829937605 + 1815356086 + 253836698)
    D[0] |= D[1]


city = 'TheNewFlagHillsByTheCtfWoods'
S[4096:4096+28] = list(city.encode())

S200()

print(f"Flag : {bytes(S[6144:6144+28])}")
