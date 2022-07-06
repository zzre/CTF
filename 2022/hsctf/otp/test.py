from Crypto.Util.number import *
from tqdm import tqdm
import random

s = 24900000000
l = 328
flag = 444466166004822947723119817789495250410386698442581656332222628158680136313528100177866881816893557


for i in tqdm(range(200000000)):
    random.seed(s+i)
    k = random.getrandbits(l)
    fl = long_to_bytes(flag ^ k) # super secure encryption

    if fl.startswith(b'flag{'):
        print(i)		
        print(fl)

# 24900000000 + 100205129 : seed