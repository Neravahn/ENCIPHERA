from .utils import inv_sub_bytes, add_round_key, inv_shift_rows


def decrypt(data:bytes, key:list) -> bytes:
    decrypted = bytearray()
    for i in range(0, len(data), 16):
        block = list(data[i:i + 16])

        #REVERSING ROUNDS
        for i in range(14):
            block = add_round_key(block, key)
            block = inv_shift_rows(block)
            block = inv_sub_bytes(block)

        decrypted.extend(block)

    return bytes(decrypted).rstrip(b'\x00')