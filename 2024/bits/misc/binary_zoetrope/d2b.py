from Crypto.Util.number import long_to_bytes as l2b

for i in range(1541):
    filename = str(i).rjust(4, '0')
    with open(f'./data/{filename}.txt', 'r') as f:
        data = f.read().split()

    with open(f'./bins/{filename}.bin', 'wb') as f:
        for line in data:
            f.write(l2b(int(line, 2)))
