from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64


def main():
    with open("10.txt") as f:
        text = f.read().replace("\n", "")

    ciphertext = base64.standard_b64decode(text)
    KEY = b"YELLOW SUBMARINE"
    iv = b"\x00" * 16
    cipher = Cipher(algorithms.AES(KEY), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    print(plaintext.decode())


if __name__ == "__main__":
    main()
