def xor(v1, v2):
    return bytes(a ^ b for a, b in zip(v1, v2))
