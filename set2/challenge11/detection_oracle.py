from commons import get_random_bytes_of_size, AES_ECB, AES_CBC, pkcs_padding, aes_ecb_detect
from random import randint

CBC = 0
ECB = 1


def encryption_oracle(data, key):
    plaintext = get_random_bytes_of_size(randint(5, 10)) + data + get_random_bytes_of_size(randint(5, 10))

    encryption_method = randint(0, 1)

    if encryption_method == CBC:
        print("CBC")
        cbc = AES_CBC(key, get_random_bytes_of_size(16))
        ciphertext = cbc.encrypt(plaintext)
    else:
        print("ECB")
        ecb = AES_ECB(key)
        ciphertext = ecb.encrypt(plaintext)

    return ciphertext


def main():
    values = get_random_bytes_of_size(16)
    ciphertext = encryption_oracle(pkcs_padding(b"HelloWorldWhatIsThisIsTheWayWeDoHelloWorldWhatIsThisIsTheWayWeDoHelloWorldWhatIsThisIsTheWayWeDo", 32), values)

    if aes_ecb_detect(ciphertext):
        print("AES_ECB")
    else:
        print("AES_CBC")


if __name__ == "__main__":
    main()
