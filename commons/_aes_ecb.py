from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from ._pkcs_padding import pkcs_padding, remove_pkcs_padding

BLOCK_LENGTH = 16

class AES_ECB:
    def __init__(self, key):
        self._cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())

    def decrypt(self, ciphertext):
        decryptor = self._cipher.decryptor()
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        return remove_pkcs_padding(plaintext, BLOCK_LENGTH)

    def encrypt(self, plaintext):
        encryptor = self._cipher.encryptor()
        ciphertext = encryptor.update(pkcs_padding(plaintext, BLOCK_LENGTH)) + encryptor.finalize()
        return ciphertext


def aes_ecb_detect(ciphertext):
    for j in range(0, len(ciphertext), 32):
        count = 0
        for i in range(0, len(ciphertext), 32):
            if i != j:
                if ciphertext[i:i + 8] == ciphertext[j:j + 8]:
                    count = count + 1

        if count > 0:
            return True

    return False
