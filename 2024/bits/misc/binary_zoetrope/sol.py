from Crypto.Util.number import long_to_bytes as l2b

for i in range(1540):
    filename = str(i).rjust(4, '0')
    with open(f'./data/{filename}.txt', 'r') as f:
        data1 = f.read().split()

    filename = str(i+1).rjust(4, '0')
    with open(f'./data/{filename}.txt', 'r') as f:
        data2 = f.read().split()

    with open(f'./xored/{filename}.bin', 'wb') as f:
        for x, y in zip(data1, data2):
            f.write(l2b(int(x, 2) ^ int(y, 2)))

