from Crypto.Cipher import DES
from Crypto.Hash import MD5
import base64

# https://any.run/cybersecurity-blog/reverse-engineering-snake-keylogger/
def lena_decrypt_snake(text, key_string):
  try:
      key = MD5.new(key_string.encode('ascii')).digest()[:8]
      cipher = DES.new(key, DES.MODE_ECB)
      decrypted_data = cipher.decrypt(base64.b64decode(text))
      decrypted_text = decrypted_data.decode('ascii', errors='ignore')
      padding_len = decrypted_data[-1]
      if padding_len < len(decrypted_data):
          return decrypted_text[:-padding_len]
      return decrypted_text

  except Exception as e:
    return str(e)

lena_key = "BsrOkyiChvpfhAkipZAxnnChkMGkLnAiZhGMyrnJfULiDGkfTkrTELinhfkLkJrkDExMvkEUCxUkUGr"
print(lena_decrypt_snake("FphMdFa3hOQv6jbOo+Di/krf6/KeCXcASv1A0PTZtTaqOQqu46FvhqM0pdqb8g0/", lena_key)) # base64 decode -> BHFlagY{t3legr4m_g0es_w!ld}
print(lena_decrypt_snake("xoZdbq0hO5UxEBQyS7nV0Q==", lena_key))
print(lena_decrypt_snake("ZyiAEnXWZP=====", lena_key))