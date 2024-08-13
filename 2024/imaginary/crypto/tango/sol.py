from pwn import *
from zlib import crc32
from Crypto.Util.number import bytes_to_long, long_to_bytes

# p = process(['python3', 'server.py'])
p = remote('tango.chal.imaginaryctf.org', 1337)

def encrypt_command(command):
    p.sendlineafter(b"> ", b'e')
    p.sendlineafter(b'Your command: ', command)
    packet = bytes.fromhex(p.recvlineS().split(': ')[1])
    print(packet.hex())
    return packet[:8], packet[8:12], packet[12:]

def run_command(command):
    print(command)
    p.sendlineafter(b"> ", b'r')
    p.sendlineafter(b"Your encrypted packet (hex): ", command)

crc32_linear = lambda x: crc32(x) ^ crc32(b'\x00' * len(x))

nonce, checksum, ct = encrypt_command('fla')

ct = list(ct)

# "user": "root"
ct[10] ^= ord('u') ^ ord('r')
ct[11] ^= ord('s') ^ ord('o')
ct[12] ^= ord('e') ^ ord('o')
ct[13] ^= ord('r') ^ ord('t')

# "command": "flag"
ct[32] ^= ord('"') ^ ord('g')
ct[33] ^= ord(',') ^ ord('"')
ct[34] ^= ord(' ') ^ ord(',')

# bypass crc
# {"user": "root", "command": "flag","nonce": "????????????????"}
data = b'{"user": "root", "command": "flag","nonce": "????????????????"}'

# get crc32 of nonce
prefix = b'{"user": "user", "command": "fla", "nonce": "'.ljust(len(data), b'\x00')
suffix = b'"}'.rjust(len(data), b'\x00')
tmp = xor(prefix, suffix)

nonce_crc = bytes_to_long(checksum) ^ crc32_linear(tmp)

# calc crc
prefix = b'{"user": "root", "command": "flag","nonce": "'.ljust(len(data), b'\x00')
suffix = b'"}'.rjust(len(data), b'\x00')
tmp = xor(prefix, suffix)
new_checksum = nonce_crc ^ crc32_linear(tmp)

run_command((nonce + long_to_bytes(new_checksum) + bytes(ct)).hex())

p.interactive()
