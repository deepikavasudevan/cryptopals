from commons import hex_to_bytes, bytes_to_base64, to_string


def main():
    hex_value = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    raw_bytes = hex_to_bytes(hex_value)

    expected_base64_string = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

    assert to_string(bytes_to_base64(raw_bytes)) == expected_base64_string


if __name__ == "__main__":
    main()
