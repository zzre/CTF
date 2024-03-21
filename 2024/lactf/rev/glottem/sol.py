from e import e
import sys
sys.setrecursionlimit(10**6)

alpha="abcdefghijklmnopqrstuvwxyz_"
candi = [[set() for j in range(len(alpha))] for i in range(len(e))]

for i in range(len(e)):
    for c in alpha:
        try:
            for idx, val in enumerate(e[i][alpha.index(c)]):
                if val == 10:
                    candi[i][alpha.index(c)].update(alpha[idx])
        except:
            pass

def check(flag):
    d = 0
    for c in flag:
        d=(d*31+ord(c)) % 93097
    
    return d == 61343

def dfs(cur, c, idx, d):
    if idx == 32 and d == 260 and check('lactf{' + cur + '}'):
        print('lactf{' + cur + '}')

    if d > 260 or idx == 32:
        return
    
    try:
        for next_char in candi[idx-6][alpha.index(c)]:
            dfs(cur+next_char, next_char, idx+1, d+e[idx-6][alpha.index(c)][alpha.index(next_char)])
    except:
        print(idx-6, alpha.index(c))

for c in alpha:
    dfs(c, c, 6, 0)
    