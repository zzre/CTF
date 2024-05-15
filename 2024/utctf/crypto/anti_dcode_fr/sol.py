import string

def shift(data):
    cset = string.ascii_lowercase
    new = ''
    for c in data:
        if c in cset:
            new += cset[(cset.index(c) + 1) % len(cset)]
            # print(c, cset[(cset.index(c) + 1) % len(cset)])
        else:
            new += c
    
    return new

with open('LoooongCaesarCipher.txt', 'r') as f:
    data = f.read()

for i in range(len(string.ascii_letters)):
    data = shift(data)
    idx = data.find('utflag{')
    if idx != -1:
          print(data[idx:].split('}')[0] + '}')


