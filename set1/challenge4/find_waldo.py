from commons import get_frequency_table, decode


def find_line(encoded_ciphertext):
    frequency = get_frequency_table()
    ciphertext = bytes.fromhex(encoded_ciphertext.replace("\n", ""))
    result = decode(ciphertext, frequency)
    for k in sorted(result, reverse=True):
        if k[0] > 120:
            print(str(k[1]))


def main():
    with open("4.txt", "r") as f:
        for line in f:
            find_line(line)


if __name__ == "__main__":
    main()
