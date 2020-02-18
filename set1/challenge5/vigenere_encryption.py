def encrypt(plaintext, key):
    n = len(plaintext) // len(key)
    if len(plaintext) % len(key) != 0:
        n = n + 1

    key = key * n
    key = key[: len(plaintext)]

    ciphertext = "".join(chr(ord(p) ^ ord(k)) for p, k in zip(plaintext, key))
    return ciphertext.encode("ascii").hex()


def main():
    plaintext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    expected_ciphertext = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    key = "ICE"

    assert encrypt(plaintext, key) == expected_ciphertext


if __name__ == "__main__":
    main()
