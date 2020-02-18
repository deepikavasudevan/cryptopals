def decode(ciphertext, frequency_table):
    result = []
    for i in range(255):
        plaintext = "".join(chr(c ^ i) for c in ciphertext)
        plaintext = plaintext.replace("\n", "")
        freq = 0
        for p in plaintext:
            if p.upper() in frequency_table.keys():
                freq += frequency_table[p.upper()]
        if " " in plaintext and plaintext.isprintable():
            result.append([freq, plaintext])

    return result
