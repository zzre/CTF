for i in range(0, 1540):
    filename = str(i+1).rjust(4, '0')
    with open(f'./xored/{filename}.bin', 'rb') as f:
        data = f.read()

    for j in range(0, len(data), 40):
        print(data[j:j+40])
    
    print(i)
    input()

# BITSCTF{n0w_u_c_m3}