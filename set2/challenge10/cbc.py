import base64
from commons import AES_CBC

if __name__ == "__main__":
    key = b"YELLOW SUBMARINE"
    iv = bytes(16)

    with open("10.txt") as f:
        text = f.read().replace("\n", "")

    ciphertext = base64.standard_b64decode(text)

    cbc = AES_CBC(key, iv)
    print(cbc.decrypt(ciphertext).decode())
