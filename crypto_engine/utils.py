SBOX = [(i ^ 0xAA) for i in range(256)]

def sub_bytes(block):
    return [SBOX[b] for b in block]

def inv_sub_bytes(block):
    inv = {SBOX[i]: i for i in range(256)}
    return [inv[b] for b in block]


def shift_rows(block):
    b = block[:]
    return [
        b[0],  b[5],  b[10], b[15],
        b[4],  b[9],  b[14], b[3],
        b[8],  b[13], b[2],  b[7],
        b[12], b[1],  b[6],  b[11]
    ]

def inv_shift_rows(block):
    b = block[:]
    return [
        b[0],  b[13], b[10], b[7],
        b[4],  b[1],  b[14], b[11],
        b[8],  b[5],  b[2],  b[15],
        b[12], b[9],  b[6],  b[3]
    ]

def add_round_key(block, key):
    return [(b ^ k) for b, k in zip(block, key)]
