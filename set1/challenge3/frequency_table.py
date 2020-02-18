from bs4 import BeautifulSoup
from urllib import request
from commons import hex_to_bytes, decode
from collections import Counter


def find_frequency(page_source):
    """
    Pride and Prejudice FTW
    :return: frequency table
    """
    html_page = request.urlopen(page_source)
    soup = BeautifulSoup(html_page, features="html.parser")

    text = soup.get_text().replace(" ", "").lower()

    frequency_table = Counter()

    for c in text:
        if c.isalpha() or c.isspace():
            frequency_table[c] = frequency_table[c] + 1

    for c in frequency_table:
        frequency_table[c] = round(frequency_table[c] / sum(frequency_table.values()) * 100, 2)

    return frequency_table


def main():
    frequency_table = find_frequency("https://www.gutenberg.org/files/1342/1342-h/1342-h.htm")
    print(frequency_table)
    encoded_ciphertext = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    ciphertext = hex_to_bytes(encoded_ciphertext)
    for k in sorted(decode(ciphertext, frequency_table)):
        print(k[1])


if __name__ == "__main__":
    main()
