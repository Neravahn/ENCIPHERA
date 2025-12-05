from .utils import shift_rows, sub_bytes, add_round_key



def encrypt(data: bytes, key: list) -> bytes:

    encrypted = bytearray()
    while len(data) % 16 != 0:
        data += b'\00'

    for i in range(0, len(data), 16):
        block = list(data[i:i+16])

        for _ in range(14):
            block = sub_bytes(block)
            block = shift_rows(block)
            block = add_round_key(block, key)

        encrypted.extend(block)

    return bytes(encrypted)






