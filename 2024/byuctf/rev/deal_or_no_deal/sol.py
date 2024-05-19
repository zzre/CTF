lst = [
    [],
    [('u', 3, 4), ('!', 2, -1), ('0', 5, 2), ('b', 0, 3)],
    [('t', 4, 1), ('u', 3, 2), ('_', 2, 3), ('c', 2, 4), ('u', 1, 2), ('_', 5, 3)],
    [('y', 1, 2), ('f', 4, 5), ('c', 2, 5), ('_', 4, 1), ('r', 2, 1)],
    [('t', 2, 3), ('n', 5, 3), ('S', 1, 5), ('s', 1, 2)],
    [('{', 3, 5), ('y', 5, 1), ('A', 3, 4), ('3', 4, 2)]
]

cur = 3
flag = 'b'

def go(prev, cur, flag):
    if len(flag) == 24:
        if cur == -1 and flag.startswith('byuctf{'):
            print(flag + '}')
        return
    for c, idx, nxt in lst[cur]:
        if idx == prev:
            go(cur, nxt, flag + c)

go(1, 3, 'b')
