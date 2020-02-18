def xor(val1, val2):
    assert len(val1) == len(val2)

    result = b"".join(bytes([a ^ b]) for a, b in zip(val1, val2))
    return result
