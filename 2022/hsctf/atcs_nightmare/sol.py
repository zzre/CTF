def inv_ll():
    ipt = "1234567890abcdefghijklmnopqr"
    res = "efghijklmnopqrdcba0987654321"

    idx = []
    for c in res:
        idx.append(ipt.index(c))

    return idx    

def inv_recurses():
    ipt = "1234567890abcdefghijklmnopqr"
    res = "rpnljhfdb0864213579acegikmoq"

    idx = []
    for c in res:
        idx.append(ipt.index(c))

    return idx

secret = b"20_a1qti0]n/5f642kb\\2`qq4\\0q"
perm = inv_ll()
x = [0] * len(secret)
for i in range(len(secret)):
    x[perm[i]] = secret[i]


perm = inv_recurses()
res = [0] * len(secret)
for i in range(len(secret)):
    res[perm[i]] = x[i]

ans = []
for i, c in enumerate(res):
    ans.append(c + (i % 4))

print(bytes(ans[::-1]))