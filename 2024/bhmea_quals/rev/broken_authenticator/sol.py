from wincrypto import CryptCreateHash, CryptHashData, CryptDeriveKey, CryptEncrypt, CryptDecrypt
from wincrypto.constants import CALG_AES_128, CALG_MD5
from tqdm import tqdm

for i in tqdm(range(100000000)):
    key = str(i).zfill(8).encode()
    h = CryptCreateHash(CALG_MD5)
    CryptHashData(h, key)
    aes_key = CryptDeriveKey(h, CALG_AES_128)
    target = "73E3679507CC8197F665FD5B46F55321CF89BB828CD7BB424B181734D468709709D49085868CDA1B9892B947999E4F64"

    res = CryptDecrypt(aes_key, bytes.fromhex(target))

    if res.startswith(b"BHFlagY"):
        print(key, res)
        break
