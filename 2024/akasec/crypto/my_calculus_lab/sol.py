from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import sympy as sp
import random

'''
2*f'' - 6*f' + 3*f == 0
f(0) | f''(0) == 14
'''
x = sp.symbols('x')
C1, C2 = sp.symbols('C1 C2')
f = sp.Function('f')
deq = sp.Eq(2*f(x).diff(x, x) - 6*f(x).diff(x) + 3*f(x), 0)
f = sp.dsolve(deq).rhs

f_candi = []
for i in range(15):
    for j in range(15):
        if i | j == 14:
            eqs = [sp.Eq(sp.diff(f, x).subs(x, 0), i), sp.Eq(f.subs(x, 0), j)]
            sol = sp.solve(eqs)
            f_candi.append(f.subs(sol))

assert len(f_candi) != 0

key = 60
data = bytes.fromhex('805534c14e694348a67da0d75165623cf603c2a98405b34fe3ba8752ce24f5040c39873ec2150a61591b233490449b8b7bedaf83aa9d4b57d6469cd3f78fdf55')

def decrypt(func, ct, iv, key):
    point = func.subs(x, key).evalf(100)
    point_hash = hashlib.sha256(str(point).encode()).digest()[:16]
    cipher = AES.new(point_hash, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ct), AES.block_size)
    return plaintext

iv, ct = data[:16], data[16:]

for f in f_candi:
    try:
        res = decrypt(f, ct, iv, key)
        if b'AKASEC' in res:
            print(res)
    except:
        pass

# b'AKASEC{d1d_y0u_3nj0y_c41cu1u5_101?}'