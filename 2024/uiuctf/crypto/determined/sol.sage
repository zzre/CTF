from pwn import *
from Crypto.Util.number import *
from itertools import permutations

def fun(M):
    def sign(sigma):
        l = 0
        for i in range(5):
            for j in range(i + 1, 5):
                if sigma[i] > sigma[j]:
                    l += 1
        return (-1)**l

    res = 0
    for sigma in permutations([0,1,2,3,4]):
        curr = 1
        for i in range(5):
            curr *= M[sigma[i]][i]
        res += sign(sigma) * curr
    return res

# f1 = p, f9 = q, f10 = r
f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12 = var('f1 f2 f3 f4 f5 f6 f7 f8 f9 f10 f11 f12')

'''
M = [
    [f1, 0, f2, 0, f3],
    [0, f4, 0, f5, 0],
    [f6, 0, f7, 0, f8],
    [0, f9, 0, f10, 0],
    [f11, 0, f12, 0, 0]
]

>>> print(fun(M))
f10*f12*f3*f4*f6 - f10*f11*f3*f4*f7 - f1*f10*f12*f4*f8 + f10*f11*f2*f4*f8 - f12*f3*f5*f6*f9 + f11*f3*f5*f7*f9 + f1*f12*f5*f8*f9 - f11*f2*f5*f8*f9

r*C1 - r*C2 - p*r*C3 + r*C4 - q*C5 + q*C6 + p*q*C7 - q*C8
'''

equations = []
for i in range(3):
    p = process('openssl s_client -connect determined.chal.uiuc.tf:1337'.split(), stdin=PTY)
    p.recvuntil(b'[DET] Welcome')

    consts = [random.randint(1, 100) for _ in range(9)]
    mat = [
        [f1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, f9, 0, f10, 0],
        [0, 0, 0, 0, 0],
    ]

    mat[0][2] = consts[0]
    mat[0][4] = consts[1]

    mat[1][1] = consts[2]
    mat[1][3] = consts[3]

    mat[2][0] = consts[4]
    mat[2][2] = consts[5]
    mat[2][4] = consts[6]

    mat[4][0] = consts[7]
    mat[4][2] = consts[8]

    for c in consts:
        p.sendlineafter(b' = ', str(c))

    p.recvuntil(b'Have fun: ')
    res = int(p.recvlineS())
    equations.append(fun(mat) == res)
    p.close()

solutions = solve(equations, [f1, f9, f10])

sol = list(filter(lambda sol: all(x.rhs().is_integer() for x in sol), solutions))[0]
p, q, r = [i.rhs() for i in sol]

n = 158794636700752922781275926476194117856757725604680390949164778150869764326023702391967976086363365534718230514141547968577753309521188288428236024251993839560087229636799779157903650823700424848036276986652311165197569877428810358366358203174595667453056843209344115949077094799081260298678936223331932826351
e = 65535
c = 72186625991702159773441286864850566837138114624570350089877959520356759693054091827950124758916323653021925443200239303328819702117245200182521971965172749321771266746783797202515535351816124885833031875091162736190721470393029924557370228547165074694258453101355875242872797209141366404264775972151904835111

assert p*q == n

phi_n = (p-1)*(q-1)
d = int(inverse(int(e), int(phi_n)))
pt = pow(c, d, n)

print(long_to_bytes(int(pt)))

