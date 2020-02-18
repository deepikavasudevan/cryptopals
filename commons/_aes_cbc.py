from ._aes_ecb import AES_ECB
from ._blocks import get_blocks
from ._xor import xor
from ._pkcs_padding import pkcs_padding

BLOCK_SIZE = 16


class AES_CBC:
    def __init__(self, key, iv):
        self._aes_ecb = AES_ECB(key)
        self._iv = iv

    def encrypt(self, plaintext):
        plaintext_blocks = get_blocks(plaintext, BLOCK_SIZE)
        previous_ciphertext = self._iv
        full_ciphertext = b""

        for p in plaintext_blocks:
            if len(p) != 16:
                p = pkcs_padding(p, BLOCK_SIZE)
            actual_plaintext = xor(p, previous_ciphertext)
            previous_ciphertext = self._aes_ecb.encrypt(actual_plaintext)
            full_ciphertext = full_ciphertext + previous_ciphertext

        return full_ciphertext

    def decrypt(self, ciphertext):
        split_ciphertext = get_blocks(ciphertext, 16)
        previous_ciphertext = self._iv
        full_plaintext = b""

        for c in split_ciphertext:
            plaintext = self._aes_ecb.decrypt(c)
            actual_plaintext = xor(plaintext, previous_ciphertext)
            previous_ciphertext = c
            full_plaintext = full_plaintext + actual_plaintext

        return full_plaintext
