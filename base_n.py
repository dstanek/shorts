"""Convert between base-10 integers and base-N strings."""

import string


def encode(number, alphabet):
    """Returns a base-N encoded string for a base-10 integer.

    Base is determined by the provided alphabet.
    """

    base = len(alphabet)
    values = []
    while True:
        number, remainder = divmod(number, base)
        values.append(alphabet[remainder])
        if number == 0:
            break
    return ''.join(reversed(values))


def decode(string, alphabet):
    """Returns a base-10 integer for a base-N encoded string.

    Base is determined by the provided alphabet.
    """

    base = len(alphabet)
    number = 0
    for char in string:
        number = number * base + alphabet.index(char)
    return number


# convenience functions for bases I know I'm going to use
BASE62_ALPHABET = string.digits + string.ascii_letters
base62_encode = lambda n: encode(n, BASE62_ALPHABET)
base62_decode = lambda s: decode(s, BASE62_ALPHABET)
