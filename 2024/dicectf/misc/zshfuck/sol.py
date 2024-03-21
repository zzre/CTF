path = '/y0u/w1ll/n3v3r_g3t/th1s/getflag'.split('/')
ch = '[^.]'

res = '.'

for c in path:
    res += ch*len(c) + '/'

print(res)
