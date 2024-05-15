from Crypto.Util.number import *
from Crypto.Random import random
from pwn import *
from tqdm import tqdm
context.log_level = 'critical'

class MT19937Recover:
    """Reverses the Mersenne Twister based on 624 observed outputs.

    The internal state of a Mersenne Twister can be recovered by observing
    624 generated outputs of it. However, if those are not directly
    observed following a twist, another output is required to restore the
    internal index.

    See also https://en.wikipedia.org/wiki/Mersenne_Twister#Pseudocode .

    """
    def unshiftRight(self, x, shift):
        res = x
        for i in range(32):
            res = x ^ res >> shift
        return res

    def unshiftLeft(self, x, shift, mask):
        res = x
        for i in range(32):
            res = x ^ (res << shift & mask)
        return res

    def untemper(self, v):
        """ Reverses the tempering which is applied to outputs of MT19937 """

        v = self.unshiftRight(v, 18)
        v = self.unshiftLeft(v, 15, 0xefc60000)
        v = self.unshiftLeft(v, 7, 0x9d2c5680)
        v = self.unshiftRight(v, 11)
        return v

    def go(self, outputs, forward=True):
        """Reverses the Mersenne Twister based on 624 observed values.

        Args:
            outputs (List[int]): list of >= 624 observed outputs from the PRNG.
                However, >= 625 outputs are required to correctly recover
                the internal index.
            forward (bool): Forward internal state until all observed outputs
                are generated.

        Returns:
            Returns a random.Random() object.
        """

        result_state = None

        assert len(outputs) >= 624       # need at least 624 values

        ivals = []
        for i in range(624):
            ivals.append(self.untemper(outputs[i]))

        if len(outputs) >= 625:
            # We have additional outputs and can correctly
            # recover the internal index by bruteforce
            challenge = outputs[624]
            for i in range(1, 626):
                state = (3, tuple(ivals+[i]), None)
                r = random.Random()
                r.setstate(state)

                if challenge == r.getrandbits(32):
                    result_state = state
                    break
        else:
            # With only 624 outputs we assume they were the first observed 624
            # outputs after a twist -->  we set the internal index to 624.
            result_state = (3, tuple(ivals+[624]), None)

        rand = random.Random()
        rand.setstate(result_state)

        if forward:
            for i in range(624, len(outputs)):
                assert rand.getrandbits(32) == outputs[i]

        return rand

r = process(['python3', 'server.py'])
# r = remote('0.cloud.chals.io', 18312)
# r = remote('ctf.dev.tbtl.io', 8002)

r.recvuntil(b' = ')
N = int(r.recvlineS())
r.recvuntil(b' = ')
e = int(r.recvlineS())
r.recvuntil(b' = ')
flag_enc = int(r.recvlineS(), 2)

print(f"[+] N = {N}")
print(f"[+] e = {e}")
print(f"[+] flag_enc = {flag_enc}")

def encrypt(data: int):
    return pow(data, e, N)

context.log_level='debug'
mtb = MT19937Recover()
lst = []
data = int('1'*256, 2) # 256 bits
data_enc = encrypt(data)

for _ in tqdm(range(32*624//256)):
    r.sendlineafter(b': ', bin(data_enc)[2:].encode())
    rcvd = int(r.recvlineS().split()[1], 2)
    lst.append(rcvd)

test = list(filter(lambda x: x&1, lst))
print(len(test))
exit()

rnd = mtb.go(lst)

# decrypt flag
r.sendlineafter(b': ', bin(flag_enc)[2:].encode())
pt = list(map(int, r.recvlineS().split()[1]))
pt_len = len(pt)
dec = pt
x = rnd.getrandbits(pt_len)

otp_key = list(map(int, bin(x)[2:]))
for i in range(len(otp_key)):
    dec[i] ^= otp_key[i]

print(long_to_bytes(int("".join(list(map(str, dec))), 2)))

r.interactive()