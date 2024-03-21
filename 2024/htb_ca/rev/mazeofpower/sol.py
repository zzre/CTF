'''
h : left
j : down
k : up
l : right
q : quit
b : solve -> prints answer. if once it called, cannot get flag
if ( !maze.Finished ) // blocked here
      {
        for ( i = 0LL; i < main_keyDirs.len; ++i )
'''

import subprocess
from pwn import *

def solve(PoW):
    r = process(['go', 'run', '.'])
    r.sendline(PoW)
    lines = r.recvall().decode().split('\n')[2:-4]

    maze = [[] for _ in range(len(lines))]
    for i, line in enumerate(lines):
        for j in range(2, len(line), 2):
            maze[i].append(line[j:j+2])

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dd = ['l', 'j', 'h', 'k']

    cur = [0, 1] # y, x
    path = []
    while 1:
        if cur == [48, 99]:
            break

        for i in range(4):
            nx = cur[1] + dx[i]
            ny = cur[0] + dy[i]

            if nx < 0 or nx >= 100 or ny < 0 or ny >= 49:
                continue

            if maze[ny][nx] != '::':
                continue

            path.append(dd[i])
            maze[ny][nx] = '  '
            nx += dx[i]
            ny += dy[i]
            maze[ny][nx] = '  '
            cur = [ny, nx]
            break

    return path


# p = process('./main')
p = remote('83.136.249.138', 33145)

result = subprocess.run(p.recvlineS().split("proof of work:")[1], shell=True, capture_output=True, text=True)
p.sendlineafter('solution:', result.stdout)

ans = solve(result.stdout)
p.sendline(''.join(ans))

p.interactive()