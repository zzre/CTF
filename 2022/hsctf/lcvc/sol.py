from Crypto.Util.number import inverse

ct = "mawhxyovhiiupukqnzdekudetmjmefkqjgmqndgtnrxqxludegwovdcdmjjhw"

state = 1
s = []
for i in range(len(ct)):
    state = (15*state+18)%29
    s.append(state)

print(s)

flag = ""
alphabet = "abcdefghijklmnopqrstuvwxyz"

print('================')
for i, c in enumerate(ct[::-1]):
    idx = alphabet.index(c)
    print(s[-(i+1)])
    idx = (idx - s[-(i+1)]) % 26
    flag += alphabet[idx]

print("flag{"+flag[::-1]+"}")