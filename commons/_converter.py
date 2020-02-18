import base64
import bitarray


def bytes_to_hex(bytes_value):
    return bytes_value.hex()


def hex_to_bytes(hex_value):
    return bytes.fromhex(hex_value)


def bytes_to_base64(byte_value):
    return base64.standard_b64encode(byte_value)


def base64_to_bytes(base64_value):
    return base64.standard_b64decode(base64_value)


def to_string(str):
    return str.decode()


def string_to_bits(s):
    b = bitarray.bitarray()
    b.fromstring(s)
    return b.tolist()
