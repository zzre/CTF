import random
import string

from Crypto.Random.random import shuffle
from secrets import randbelow


class BitOfShuffling:
    def __init__(self, key_length):
        self.perm = [x for x in range(key_length)]
        shuffle(self.perm)

    def shuffle_int(self, input_int: int):
        shuffled_int = 0
        for x in range(len(self.perm)):
            shuffled_int |= ((input_int >> x) & 1) << self.perm[x]
        return shuffled_int

    def shuffle_bytes(self, input_bytes):
        return self.shuffle_int(int.from_bytes(input_bytes, 'big'))


def rand_string(length):
    return ''.join(
        random.choices(string.digits + string.ascii_letters + r"""!"#$%&'()*+,-./:;<=>?@[\]^_`|~""", k=length))


def pad_flag(flag, length):
    pad_size = length - len(flag)
    if pad_size == 0:
        return flag
    left_size = randbelow(pad_size)
    right_size = pad_size - left_size
    return rand_string(left_size) + flag + rand_string(right_size)


KEY_LENGTH = 128
trials = 10
if __name__ == "__main__":
    # with open("flag.txt", "r") as f:
        # FLAG = f.read()
    FLAG = 'UMASS{test_flag}'
    FLAG = pad_flag(FLAG, KEY_LENGTH)
    flag = int.from_bytes(FLAG.encode(), 'big')
    print(FLAG.index('UMASS{test_flag}'))
    shuffler = BitOfShuffling(KEY_LENGTH * 8)
    output_int = shuffler.shuffle_bytes(FLAG.encode())
    # print(flag ^ output_int)

    # print(bytes.fromhex(hex(output_int)[2:]))
    # print(shuffler.perm)
    print("Quite a bit of shuffling gave us this hex string: ")
    print(f'{output_int:0{KEY_LENGTH * 2}x}')
    print(f"You too can shuffle your hexed bits with our {trials} free trials!")
    for i in range(trials):
        trial = input(f"Input {i + 1}:")
        # trial = '01'*128
        bits_from_hex = bytes.fromhex(trial)
        res = shuffler.shuffle_bytes(bits_from_hex)
        print(f'{res:0{KEY_LENGTH * 2}x}')
        # print(f'{(res & flag):0{KEY_LENGTH * 2}x}')
    print("See you next time!")