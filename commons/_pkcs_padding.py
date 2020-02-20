def pkcs_padding(unpadded_text, block_length):
    padding_value = block_length - (len(unpadded_text) % block_length)
    padded_string = bytes([padding_value]) * padding_value
    return unpadded_text + padded_string


def remove_pkcs_padding(padded_text, block_length):
    padded_value = padded_text[-1]
    if padded_value <= block_length:
        return padded_text[0 : len(padded_text) - padded_value]

    return padded_text
