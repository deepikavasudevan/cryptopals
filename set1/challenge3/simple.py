from commons import hex_to_bytes


def main():
    encoded_ciphertext = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    ciphertext = hex_to_bytes(encoded_ciphertext)

    for i in range(255):
        plaintext = "".join(chr(c ^ i) for c in ciphertext)
        if " " in plaintext and plaintext.isprintable():
            print(plaintext)


if __name__ == "__main__":
    main()
