import base64
from commons import get_frequency_table, get_blocks, string_to_bits


def hamming_distance(bitarray1, bitarray2):
    if len(bitarray1) != len(bitarray2):
        return -1
    return sum(bit1 != bit2 for bit1, bit2 in zip(bitarray1, bitarray2))


def ciphertext_from_file(file_name):
    """
        Take the base64 encoded ciphertext and decode it to return the ciphertext
    :param file_name: name of the file containing the ciphertext
    :return: base64 decoded ciphertext
    """
    with open(file_name, "r") as f:
        text = f.read().replace("\n", "")

    return base64.b64decode(text)


def find_hamming_distance(ciphertext, key_size):
    """
    Finds the bit size hamming distance
    :param ciphertext:
    :param key_size:
    :return: the hamming distance
    """
    chunks = get_blocks(ciphertext, key_size)
    distances = [
        hamming_distance(
            string_to_bits("".join(chunk for chunk in chunks[0:5])),
            string_to_bits("".join(chunk for chunk in chunks[5:10])),
        )
    ]
    return sum(distances) // key_size


def get_key_size_with_smallest_distance(ciphertext):
    """
    Returns the 4 key sizes with the lowest Hamming distance
    :param ciphertext: the ciphertext
    :return: list of the 4 smallest key_sizes
    """
    result = []
    for key_size in range(4, 41):
        result.append([find_hamming_distance(ciphertext, key_size), key_size])

    result.sort()
    return [r[1] for r in result[0:4]]


def find_likely_plaintext(block):
    frequency = get_frequency_table()
    result = []

    for i in range(255):
        plaintext = "".join(chr(ord(c) ^ i) for c in block)
        freq = 0
        for p in plaintext:
            if p.upper() in frequency.keys():
                freq += frequency[p.upper()]
            # if plaintext.isalnum() or len(set(plaintext).intersection(set(string.punctuation))) > 0:
            result.append([freq, plaintext])

    result.sort(reverse=True)
    if len(result) > 0:
        return result[0][1]
    else:
        raise Exception("This block doesn't have a valid plaintext")


def assemble_plaintext(plaintexts, key_size):
    plaintext = ""
    for i in range(0, key_size):
        for j in range(0, len(plaintexts)):
            try:
                plaintext += plaintexts[j][i]
            except IndexError as i:
                print(i)
                break

    return plaintext


def transpose_ciphertext(ciphertext, size):
    blocks = [""] * size
    chunks = get_blocks(ciphertext, size)

    for i in range(0, size):
        for chunk in chunks:
            try:
                blocks[i] = blocks[i] + chunk[i]
            except IndexError as i:
                break
    return blocks


def main():
    ciphertext = ciphertext_from_file("6.txt").decode("utf-8")
    key_sizes = get_key_size_with_smallest_distance(ciphertext)
    for size in key_sizes:
        plaintexts = []
        blocks = transpose_ciphertext(ciphertext, size)
        for block in blocks:
            plaintexts.append(find_likely_plaintext(block))
        plaintext = assemble_plaintext(plaintexts, size)
        print(f"{size}\n{plaintext}")


if __name__ == "__main__":
    main()
