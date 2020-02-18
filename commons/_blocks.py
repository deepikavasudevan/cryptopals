def get_blocks(ciphertext, key_size):
    return [ciphertext[0 + i : key_size + i] for i in range(0, len(ciphertext), key_size)]
