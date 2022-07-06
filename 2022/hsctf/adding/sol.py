i = 2
s = 2
ans = 10

for ii in range(1, 214):
    i = 2*(i+1)
    s += i
    ans += 10*(ii+1)

print(s*20 + ans)