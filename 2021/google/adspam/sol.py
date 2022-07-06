import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from pwn import *
import json
from Crypto.Util.number import *

def decode(str, len):
    res = [0]*len
    arr = b'cFUgdW9ZIGV2aUcgYW5ub0cgcmV2ZU4='
    for i in range(len):
        res[i] = arr[i & 0x1f] ^ str[i]

    return ''.join(map(chr, res))

def encrypt(pt):
    cipher = AES.new(key, AES.MODE_ECB)
    return base64.b64encode(cipher.encrypt(pad(json.dumps(pt).encode(), 16)))

def decrypt(ct):
    cipher = AES.new(key, AES.MODE_ECB)
    return unpad(cipher.decrypt(base64.b64decode(ct)), 16)

def declicstr(encrypted):
    modulus = 123596194752125979169492805898717739603063620825567453811699517077883880522042319510992511000584675998759365763564255380979966851592871801417286328813040909357944964680643572428136557634939634304256208583286122710159831699682677545905872084440840115646364525758632063374092374969271133111500901869640594407799
    exponent = 65537
    encrypted = bytes_to_long(base64.b64decode(encrypted))
    return long_to_bytes(pow(encrypted, exponent, modulus))

key = b'eaW~IFhnvlIoneLl'

# R.raw.lic
licenses = '''QIknTsIjeUEF9yJjeZ/kPPfTlSm8vzMU4LWjzfSXvN+OSqBu3iNgZJgeW7fc8oltH9MprO9nI8vxgsjO/VA4t7YuNm16a7elPVAHqD4dXtzngnZPpsbek3Rc/We/WQ5YxXHgUt7YJ6tcd4wH3fhduC9tl/E5elwJL/YAcbD4mT8=
o9kjqYWCBKMgodl1JvDiscUeRjh9Ip9HcC7tHskoYqNQfAPE0XvSAKBSOFgleNHzVY9BVkfxmutgn/kVXUs3yl/qAurc4jokg0eA/v3flnnkWxqTOh4vv0yfr7PGXqwHk4qUFK1SldZ4VsLhd8PAb0aHj22E5b4U5jeJ16z187E=
gpDbCb0BmUZfdKVIZgF08lQ80K9SeUsRadZG+UUjE7wI1NRZ1evLk2GQ3sqskGHFKlPg8cTR2Xy69WedNu4QLboOWm/w13ocOvHwCoiQ1ZdmibgnhMQBznqpjpBnL083YMRYskcUX68R2PFaXY3taV7MoG1DyQWFRfdr/CnLyS8=
ZBLhwMu0DbgpUANm2ukYldrppJERiH1Tgp02CRB5I4dDP8n4+ZCv33ScspELtgAKHhiwIVksQVsnwDLsQRi6nqq9nrIwqSHMR0TwOe6UKTpAegbH53FXtriopPHfLuI2M45SzJ88GFjXy7wfOOjwDYe4KKO9KU8+LGD15Au73EM=
Hygv+bTtsnI9IBf44GkvoF38r3g5zBB7uyYT7PTlbjhCdgYRwRayutI3vY+n66xM7GOFgUFVIBI5+OBDnvazLNttjGomPED/OXlImndWvrZxYcaKaE3vYGPezorV0xwPahGGq/DWafPKdYxLxwICq1GXKYNAckCZIqfpGbJRRwg=
GARMZAX7fQN7i7Wnp4J6HxMTLe9+VM/wGJs+zN6b9IOmynh2gIkGjmssfOA9KdYydqBLEOJymayH8HeyrtInhhQNR3el8A5n8GMEMkyF1gUFAiSEPyhNeWWOj2IAHGNNwccmF7QywdfOUGjsTNFbrW6Yl5QLLAmMbA95qF0IERk=
YWlx8Cok1x/3ZsW9JKIsKj9UpBaCNkXSPiVXUrNX1IDZE0B8iNr3iliOr90TW0BvsIaFEwvDTlcESXJ8kLc3iZq0fm1lgujfM7Z156VdxEPjr9LplcEZ9ZVhYGNtVyGIRcouUDJHu3FVfXQ1XesaNlNHOb50hADprsw3RnTAGbU=
I3dsx2vSfXxZ1/QlMbwYPRFEZBtOuB8qLEY8cqFVtYjMluNWSkbHAYB+kwCBEv3yuoOjkdQEfqq4pS+K0ka1+pFDyss8sSbV3OiZdpRf40SS/pZxw2duJr9uDd1DdX8mST7fdjqj0V1a2ZBMpqaEI2gFlCwzXlfZBC47LKNiM+8=
ow7r5VJMGfSf0odNKxzBpUtSJdj8gHdt+Z7Xu54MAdsnUParSjrtRI4yJYzcW4toOFmDdSs5SERR289yohYI5hHSWLElv/44O+g4M08F5qpwCmOp5otW32qRG1RnhqR95evH44nOyK24UnpvWlebNwVhniSu4A7znjluGRrao/U=
TeGqGWv8ZmsY/rFq1puW9N+01TWTKJm8qzUuY/7JUCPDJ1AR6Y3XsPb73FuSVHPL63sjiuCTiKTRSUDzBE0VBfo59rtOKI05k64Jrz88nODD7BiK7ssacsOr2dAFGQKgBaWV2jitSAdxtCmh9sDpYsfs0/vXBBfVLqfVZDfAVGQ=
Al3QWY+nNFoLezt+rSdbWmqp7iZ+rR9pnM35IJNZ63bLQeM3CUvULVczhrM3toXNLCY7xmAT4jg+u0uDAjanaKMB+T1Tmym7aaCqwCfHYVFn5nw+tw54e13CLxj7OO+e847+XH8DtK/BiA+n03vPnt/cEDPvIM59sPsjHThJvpk=
VOGr60qxiO1r0YlKnrIWbQu7UhBmtBeNw2NDQnoNU3H1mjVEs/ji3AYuEGc2HGKINByq7Mpb4mWKD2oH5ii/UZDpxbzCFlJrjvjEG25c9Hhf2fiQHvRXmJd8iA8YdffBii3csCjaydLFSX6Vn7XPg+/PF/TdM1zUiLTJZX4LXRw=
ELL9maLDpdmmEgaT76qtw9IugtaQX2r7V7QVqMKXQcbwq7o0dvaO3+yMt6m5K5Milm4JSNwX/810YUaoAsHNuaIavuLRsxbP3b6KnKxaKz3EDgyhye2en3U1EZouiLljBB0bKz8rAtyGdolWDdNoKjvLhv7x2edc05HQZOt3aiA='''.split()

license = b''
for l in licenses:
    license += declicstr(l)

# print(license)

def a(arr, i):
    return arr[i+1:arr[i]+i+1]

p = remote("adspam.2021.ctfcompetition.com", 1337)

license = b''
go = '::'.join(licenses[:-1] + [licenses[10]]*100)
for l in go.split("::"):
    license += declicstr(l)

name = a(license, 0)
is_admin = a(license, len(a(license, len(name)+1)) + 1 + len(name) + 1)
print(license[49] + 50, len(license))
print(name, is_admin)

payload = {"name":f"{name.decode()}", "is_admin":0, "device_info":{"os_version":123, "api_level":30, "device":"generic_x86"}, "license":f"{go}"}
# print(payload)
p.sendlineafter(b'\n', encrypt(payload))

encrypted = p.recvline()[:-1]
print(decrypt(encrypted))

p.close()
