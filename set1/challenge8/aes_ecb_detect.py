from commons import aes_ecb_detect, AES_ECB


def main():
    line_number = 0

    with open("8.txt", "r") as f:
        for line in f:
            line_number = line_number + 1
            ciphertext = line.replace("\n", "")
            if aes_ecb_detect(ciphertext):
                print(f"{line_number} {line}")



if __name__ == "__main__":
    main()
