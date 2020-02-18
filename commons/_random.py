import random


def get_random_bytes_of_size(size):
    values = b""
    for i in range(16):
        values = values + bytes([random.getrandbits(8)])

    return values
