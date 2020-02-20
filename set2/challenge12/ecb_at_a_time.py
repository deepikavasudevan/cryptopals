from commons import get_random_bytes_of_size, base64_to_bytes, AES_ECB

aes = AES_ECB(get_random_bytes_of_size(16))
entries = {}


def find_block_size(unknown_string):
    previous_ciphertext = ""
    for i in range(1, 16):
        plaintext = b"A" * i + unknown_string
        ciphertext = aes.encrypt(plaintext)

        if previous_ciphertext != "" and abs(len(ciphertext) - len(previous_ciphertext)) > 1:
            return abs(len(ciphertext) - len(previous_ciphertext))

        previous_ciphertext = ciphertext


def generate_dictionary(block_size):
    for j in range(0, 255):
        new_plaintext = b"A" * (block_size - 1)
        new_plaintext = new_plaintext + bytes([j])
        entries[aes.encrypt(new_plaintext)] = chr(j)


def main():
    base64_encoded_plaintext = b"Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"
    unknown_string = bytearray(base64_to_bytes(base64_encoded_plaintext))
    block_size = find_block_size(unknown_string)

    generate_dictionary(block_size)

    guessed_plaintext = ""
    for i in range(0, len(unknown_string)):
        new_plaintext = b"A" * (block_size - 1) + bytes([unknown_string[i]])
        ciphertext = aes.encrypt(new_plaintext)

        guessed_plaintext = guessed_plaintext + entries[ciphertext]

    print(guessed_plaintext)


if __name__ == "__main__":
    main()
