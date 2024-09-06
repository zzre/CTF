from Crypto.Cipher import AES
from Crypto.Util.number import *
from Crypto.Util.Padding import unpad

enc = bytes.fromhex('03afaa672ff078c63d5bdb0ea08be12b09ea53ea822cd2acef36da5b279b9524')

KEY = b'react_native_expo_version_47.0.0'
IV = b'__sekaictf2023__'

cipher = AES.new(KEY, AES.MODE_CBC, IV)

pw = unpad(cipher.decrypt(enc), 16)
print(pw)

'''
id : admin@sekai.team
pw : s3cr3t_SEKAI_P@ss
'''