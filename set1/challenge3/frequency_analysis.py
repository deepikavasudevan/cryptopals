from commons import get_frequency_table, decode

frequency = get_frequency_table()


def main():
    encoded_ciphertext = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    ciphertext = bytes.fromhex(encoded_ciphertext)
    for k in sorted(decode(ciphertext, frequency), reverse=True):
        print(k[1])


if __name__ == "__main__":
    main()
