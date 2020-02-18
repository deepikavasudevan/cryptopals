from commons import AES_ECB, base64_to_bytes


def main():
    with open("7.txt") as f:
        text = f.read().replace("\n", "")

    ciphertext = base64_to_bytes(text)
    key = b"YELLOW SUBMARINE"
    aes = AES_ECB(key)
    print(aes.decrypt(ciphertext).decode())


if __name__ == "__main__":
    main()
