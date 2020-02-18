def pkcs_padding(unpadded_text, block_length):
    padding_value = block_length - (len(unpadded_text) % block_length)
    padded_string = bytes([padding_value]) * padding_value
    return unpadded_text + padded_string
