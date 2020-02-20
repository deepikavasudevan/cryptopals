from commons import key_value_decode, key_value_encode, get_random_bytes_of_size, AES_ECB, pkcs_padding

aes = AES_ECB(get_random_bytes_of_size(16))

def profile_for(user_email):
    profile_info = {}
    profile_info["email"] = user_email.replace("&", "").replace("=", "")
    profile_info["uid"] = 10
    profile_info["role"] = "user"
    return key_value_encode(profile_info)


def encrypt_user_profile(profile):
    print(len(profile))
    return aes.encrypt(profile.encode())


def decrypt_user_profile(ciphertext):
    plaintext = aes.decrypt(ciphertext)
    return key_value_decode(plaintext.decode())


def main():
    #This to get email=aaaaaaaaaaaaa,uid=10,role=
    ciphertext1 = encrypt_user_profile(profile_for("a" * 13))


    #This is to get an encrypted blob of admin with the correct pkcs padding
    plaintext = ("a" * 10) + pkcs_padding(b"admin", 16).decode()
    ciphertext2 = encrypt_user_profile(profile_for(plaintext))

    print(decrypt_user_profile(ciphertext1[0:32] + ciphertext2[16:32]))


if __name__ == "__main__":
    main()
