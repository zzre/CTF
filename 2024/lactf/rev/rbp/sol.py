# nums -> 1 0 4 3 0 0 3 1
import string

def go(c, i):
    for _ in range(i):
        c = string.ascii_lowercase[(string.ascii_lowercase.index(c) - 1) % 26]
    return c

# lactf{rub1sc0?b4s3d?ph0t0synth3s1s} -> lactf{rub1sc0_b4s3d_ph0t0synth3s1s}
go('v', 56) # r
go('w', 54) # u
go('b', 52) # b
# 1
go('o', 48) # s
go('w', 46) # c
# 0
# ?
go('p', 40) # b
# 4
go('c', 36) # s
# 3
go('j', 32) # d
# ?
go('r', 28) # p
go('h', 26) # h
# 0
go('p', 22) # t
# 0
go('k', 18) # s
go('o', 16) # y
go('b', 14) # n
go('f', 12) # t
go('r', 10) # h
# 3
go('y', 6) # s
# 1
go('u', 2) # s
