l = 328
flag = 444466166004822947723119817789495250410386698442581656332222628158680136313528100177866881816893557

from Crypto.Util.number import *
from tqdm import tqdm
import random

f = bytes_to_long(long_to_bytes(flag)[-5:])

random.seed(24900000000 + 100212790)
k = random.getrandbits(l)
fl = long_to_bytes(flag ^ k) # super secure encryption

print(fl)    
