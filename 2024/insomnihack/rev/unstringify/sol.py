import copy

s_box = [
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
    0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
    0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
    0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
    0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
]

def sub_bytes(state):
    for i in range(4):
        for j in range(4):
            state[i][j] = s_box[state[i][j]]

    return state

def inv_sub_bytes(state):
    for i in range(4):
        for j in range(4):
            state[i][j] = s_box.index(state[i][j])

    return state

def shift_rows(state):
    for i in range(1, 4):
        state[i] = state[i][i:] + state[i][:i]
    return state

def inv_shift_rows(state):
    for i in range(1, 4):
        state[i] = state[i][-i:] + state[i][:-i]
    return state

def galois_mult(a, b):
    """
    Multiplication in the Galois field GF(2^8).
    """
    p = 0
    hi_bit_set = 0
    for i in range(8):
        if b & 1 == 1: p ^= a
        hi_bit_set = a & 0x80
        a <<= 1
        if hi_bit_set == 0x80: a ^= 0x1b
        b >>= 1
    return p % 256

def mix_column(column):
    """
    Mix one column by by considering it as a polynomial and performing
    operations in the Galois field (2^8).
    """
    # XOR is addition in this field
    temp = copy.copy(column) # Store temporary column for operations
    column[0] = galois_mult(temp[0], 2) ^ galois_mult(temp[1], 3) ^ \
                galois_mult(temp[2], 1) ^ galois_mult(temp[3], 1)
    column[1] = galois_mult(temp[0], 1) ^ galois_mult(temp[1], 2) ^ \
                galois_mult(temp[2], 3) ^ galois_mult(temp[3], 1)
    column[2] = galois_mult(temp[0], 1) ^ galois_mult(temp[1], 1) ^ \
                galois_mult(temp[2], 2) ^ galois_mult(temp[3], 3)
    column[3] = galois_mult(temp[0], 3) ^ galois_mult(temp[1], 1) ^ \
                galois_mult(temp[2], 1) ^ galois_mult(temp[3], 2)

def mix_columns(state, nb):
    """
    Perform a mixing operation which operates on the columns of the states,
    combining the four bytes in each column.
    """
    for i in range(nb):
        # Create column from the corresponding array positions
        column = []
        for j in range(nb): column.append(state[i][j])

        # Mix the extracted column
        mix_column(column)

        # Set the new column in the state
        for j in range(nb): state[i][j] = column[j]

def inv_mix_column(column):
    """
    Inverse mix one column by considering it as a polynomial and performing
    operations in the Galois field (2^8).
    """
    # XOR is addition in this field
    temp = copy.copy(column)  # Store temporary column for operations
    column[0] = galois_mult(temp[0], 0x0e) ^ galois_mult(temp[1], 0x0b) ^ \
                galois_mult(temp[2], 0x0d) ^ galois_mult(temp[3], 0x09)
    column[1] = galois_mult(temp[0], 0x09) ^ galois_mult(temp[1], 0x0e) ^ \
                galois_mult(temp[2], 0x0b) ^ galois_mult(temp[3], 0x0d)
    column[2] = galois_mult(temp[0], 0x0d) ^ galois_mult(temp[1], 0x09) ^ \
                galois_mult(temp[2], 0x0e) ^ galois_mult(temp[3], 0x0b)
    column[3] = galois_mult(temp[0], 0x0b) ^ galois_mult(temp[1], 0x0d) ^ \
                galois_mult(temp[2], 0x09) ^ galois_mult(temp[3], 0x0e)

def inv_mix_columns(state, nb):
    """
    Perform an inverse mixing operation which operates on the columns of the states,
    combining the four bytes in each column.
    """
    for i in range(nb):
        # Create column from the corresponding array positions
        column = []
        for j in range(nb):
            column.append(state[i][j])

        # Inverse mix the extracted column
        inv_mix_column(column)

        for j in range(nb):
            state[i][j] = column[j]

def xor_states(state1, state2):
    result = [[state1[i][j] ^ state2[i][j] for j in range(4)] for i in range(4)]
    return result

def print_state_hex(state):
    for row in state:
        hex_row = [hex(byte) for byte in row]
        print(hex_row)

def transpose(state):
    return [list(i) for i in zip(*state)]

def print_state_str(state):
    for i in range(4):
        print(''.join(map(chr, state[i])))

def encrypt(state):
    shift_rows(state)
    sub_bytes(state)
    state = transpose(state)
    mix_columns(state, 4)
    state = transpose(state)
    state = xor_states(state, round_key)
    return state

def decrypt(state):
    state = xor_states(state, round_key)
    state = transpose(state)
    inv_mix_columns(state, 4)
    state = transpose(state)
    inv_sub_bytes(state)
    inv_shift_rows(state)
    return state

def concat_flag(flag):
    ret = ''
    for state in flag:
        tmp = []
        for i in range(4):
            tmp.append(''.join(map(chr, state[i])))
        ret = tmp[2] + tmp[3] + tmp[0] + tmp[1] + ret

    return ret

flag = []

state = [
    [0x51, 0xa0, 0x6d, 0xec],
    [0xcc, 0x26, 0x75, 0xfd],
    [0x0f, 0x2a, 0x89, 0x46],
    [0xbe, 0x14, 0x30, 0x1c]
]

round_key = [
    [0x00, 0x5B, 0x00, 0x5C],
    [0x03, 0x00, 0x03, 0x09],
    [0x19, 0x59, 0x15, 0x01],
    [0x5A, 0x02, 0x01, 0x5E]
]

state = decrypt(state)
# print_state_hex(state)
flag.append(transpose(state))

state = [
    [0x0F, 0x8B, 0x68, 0x2A],
    [0xA3, 0x62, 0xEA, 0xC7],
    [0xB4, 0xC9, 0x03, 0xF2],
    [0x79, 0x06, 0xBE, 0xC4]
]

round_key = [
    [0x42, 0x4D, 0x27, 0x63],
    [0x53, 0x06, 0x52, 0x0B],
    [0x0D, 0x42, 0x42, 0x54],
    [0x16, 0x0D, 0x3A, 0x0F]
]

state = decrypt(state)
# print_state_hex(state)
flag.append(transpose(state))

print(concat_flag(flag))
