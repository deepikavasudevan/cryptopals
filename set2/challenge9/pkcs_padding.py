from commons import pkcs_padding

BLOCK_LENGTH = 20
UNPADDED_TEXT = b"YELLOW SUBMARINE"


def main():
    padded_text = pkcs_padding(UNPADDED_TEXT, BLOCK_LENGTH)
    print(padded_text)


if __name__ == "__main__":
    main()
