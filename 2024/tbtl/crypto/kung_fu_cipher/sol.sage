# run on sage
import z3
from pwn import *
from Crypto.Util.number import *
context.log_level = 'critical'

candi = []

def factorize(p, q, target, depth = 0):
    if depth == 80:
        candi.append((p, q))
        return
    m = 10**(depth+1)
    s = z3.Solver()
    x = z3.Int('x')
    y = z3.Int('y')
    s.add((target - (x*(10**depth) + p)*(y*(10**depth) + q)) % m == 0)
    s.add(z3.Or(z3.Or(x == 5, x == 7), x == 9))
    s.add(z3.Or(z3.Or(y == 5, y == 7), y == 9))

    ans = []
    while True:
        if s.check() != z3.sat:
            break
        model = s.model()
        xx, yy = model[x].as_long(), model[y].as_long()
        ans.append((xx*(10**depth) + p, yy*(10**depth) + q))
        s.add(z3.Or(x != xx, y != yy))

    for x, y in ans:
        factorize(x, y, target, depth+1)

r = remote("0.cloud.chals.io", int(30461))

r.recvuntil(b'n = ')
n = int(r.recvlineS(), 16)
print(f'[*] n = {n}')

print(f'[-] factoring n ...')
factorize(0, 0, n, 0)
p, q = next(filter(lambda x: x[0]*x[1] == n, candi))
print(f'[*] n = {p}, {q}')

# get e
'''
if A = P*J*P^(-1)
then A^k = P*(J^k)*P^(-1)
'''
A = matrix(ZZ, 2, 2, [2, 1, 0, 2]).apply_map(lambda x: x % n)
r.sendlineafter(b'> ', b'2')
r.sendlineafter(b'= ', b'2')
r.sendlineafter(b'= ', b'1')
r.sendlineafter(b'= ', b'0')
r.sendlineafter(b'= ', b'2')

lst = [int(r.recvlineS().split(' = ')[1], 16) for i in range(4)]

B = matrix(ZZ, 2, 2, lst).apply_map(lambda x: x % n)

e = (A[0][0] * B[0][1] / B[0][0]) % n

assert isPrime(int(e))
print(f'[*] e = {e}')

# get flag
r.sendlineafter(b'> ', b'1')
ct = [int(r.recvlineS().split(' = ')[1], 16) for i in range(4)]
p_order = (p^2 - 1)*(p^2 - p)
p_d = pow(e, -1, p_order)

q_order = (q^2 - 1)*(q^2 - q)
q_d = pow(e, -1, q_order)

p_mat = matrix(GF(p), 2, 2, ct)
p_pt = p_mat ^ int(p_d)
q_mat = matrix(GF(q), 2, 2, ct)
q_pt = q_mat ^ int(q_d)

for i in range(2):
    for j in range(2):
        print(long_to_bytes(int(crt([int(p_pt[i][j]), int(q_pt[i][j])], [p, q]))).decode(), end='')
print()

r.close()
