import string
with open('intro.txt', 'rb') as f:
    pt = f.read().lower()

with open('ct.txt', 'rb') as f:
    ct = f.read().lower()

lst = []
for i in range(len(pt)):
    if chr(pt[i]) in string.ascii_lowercase:
        lst.append((ct[i] - pt[i]) % 26)

idx = lst.index(6)
key = lst[idx:]
ct = 'ropgf{qvjal_dfuxaxzbk_gbq_jeci_hdt_nr_hdr_eexij}'

i = 0
for c in ct:
    try: 
        print(string.ascii_lowercase[(string.ascii_lowercase.index(c) - key[i]) % 26], end='')
        i += 1
    except:
        print(c, end='')