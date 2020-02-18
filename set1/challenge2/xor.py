from commons import xor, hex_to_bytes, bytes_to_hex


def main():
    expected_value = "746865206b696420646f6e277420706c6179"
    computed_value = xor(
        hex_to_bytes("1c0111001f010100061a024b53535009181c"), hex_to_bytes("686974207468652062756c6c277320657965")
    )
    assert expected_value == bytes_to_hex(computed_value)


if __name__ == "__main__":
    main()
