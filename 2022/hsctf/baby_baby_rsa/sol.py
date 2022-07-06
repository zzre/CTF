from Crypto.Util.number import *
from itertools import permutations

ct = 54794426723900547461854843163768660308115034417111329528183606035659639395104723918632912086419836023341428265596988959206660015436864401403237748771765948022232575597127381504670391300908215025163138869313954305720403722718214862988965792884236612959443476803344992121865817757791519151566895512058656532409472494022672998848036223706004788146906885182892250477746430460414866512005225936680732094537985671236900243908114730784290372829952741399684135984046796
e = 0x10001
parts = ['0100101100001100010110110001000001001110010110110011101111100001101100000101000011111000101110011010010100101100011111000000101010011101100101010000101101110100100010101011100110001010001000000001000110000111011110011001101111110000100010000110000001110011', '1100001100001100111110011110110101001100100000000100000100011110110010010101000011111111000100001000111001100110010010010011110110110010010110110100010110100011011100101001100001010111000100000110101010101011011110110110101010110100011110010000101010000111', '1000100010110110010100111010100100111000100111100101100001011111100011000111110011101011011011100000101011000111010110010010011110100100110000001101110111001000000111100111011011000101010001111101000111100111110010011101011111100100111111011011110110101111', '1111001101111101111111111111001010001111100010100000010110011011100000000110010110000011011110101110001000001111110101101101111000000111101111111000011101011010000110111100000110000001001101101010100000010011000100010111100001011000101101111000101101110100', '1100100000100001010111110010000011000010100110101111100100011010111111110100011011111100001011101001010000100111100011100111000101110001001011110000000000000000000110111100000111100000111111010110010011000010011000110111001010000110011011111101011110000101', '0001101000011011010011100100000011010101110110111001111011000001010101101111110100011011010011111010001111011011100011111110101110101101111100100011111110011111010100001100011000111011010111110101000011110101011110110001011110001111011001101100110100000101']
parts = list(map(lambda x: int(x, 2), parts))
s = 768 // 3

for A, B, C, D, E, F in permutations(parts):
    p = A | (B << s) | (C << (s*2))
    q = D | (E << s) | (F << (s*2))
    n = p*q

    phi = (p-1)*(q-1)
    d = inverse(e, phi)
    pt = long_to_bytes(pow(ct,d,n))
    if b'flag' in pt:
        print(pt)
        break
