from base64 import b64decode, b64encode
import requests

s = requests.Session()
URL = 'https://cookiecutter.chal.cyberjousting.com'

# data = {'email': '1111111111'+'111111111111'}
data = {'email': '1111111111'}

res = s.post(URL + '/login', data=data)
cookie = b64decode(res.cookies['cookie'])
prefix = cookie[:32] # email=1111111111&uid=?????&role=

data = {'email': '1111111111' + 'admin'}
res = s.post(URL + '/login', data=data)
cookie = b64decode(res.cookies['cookie'])
suffix = cookie[16:32] # admin&uid=?????&

data = {'email': '111111'}
res = s.post(URL + '/login', data=data)
cookie = b64decode(res.cookies['cookie'])
pad16 = cookie[-16:] # 16 bytes pad

# cookie: email=1111111111&uid=?????&role=admin&uid=?????&email=1111111111
cookies = {'cookie': b64encode(prefix+suffix+prefix[:16]+pad16).decode()}
res = requests.get(URL + '/authenticate', cookies=cookies)
print(res.text)

