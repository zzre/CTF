from pwn import *

wordlist = open('wordlist.txt', 'r').read().split('\n')

# p = process(['python3', 'main.py'])
p = remote('betta.utctf.live', 7496)

def guess(answer):
    p.recvuntil(b'?\n')
    p.sendline(answer)
    return int(p.recvlineS())

# lst = b'abcdefghijklmnopqrstuvwxyz'
# ans = b''
# for i in range(5):
#     answer = list(b'a'*5)
#     answer[i] = b'b'
#     ans = lst[guess(b''.join(answer))]

def get_response(word, ans):
    response = 1
    for x in range(5):
        a = ord(ans[x]) - ord('a')
        b = ord(word[x]) - ord('a')
        response = (response * (a-b)) % 31
    return response

def filt(wlist, ans, response):
    return list(filter(lambda x: get_response(x, ans) == response, wlist))

def go(wlist, word):
    return filt(wlist, word, guess(word))

for i in range(3):
    wlist = wordlist[:]
    wlist = go(wlist, 'a'*5)
    wlist = go(wlist, 'b'*5)
    wlist = go(wlist, 'c'*5)
    wlist = go(wlist, 'd'*5)
    wlist = go(wlist, 'e'*5)

    assert len(wlist) == 1

    p.sendline(wlist[0])
    p.recvline()

p.interactive()