#!/usr/bin/python3
"""Task 0
"""


def validUTF8(data):
    """Determines if the dataset represents a valid UTF-8 encoding
    """
    n_bytes = 0

    for byte in data:
        byte = byte & 0xFF  # Consider only the least significant 8 bits

        if n_bytes == 0:
            if (byte >> 5) == 0b110:
                n_bytes = 1
            elif (byte >> 4) == 0b1110:
                n_bytes = 2
            elif (byte >> 3) == 0b11110:
                n_bytes = 3
            elif (byte >> 7):
                return False  # Invalid 1-byte character
        else:
            if (byte >> 6) != 0b10:
                return False
            n_bytes -= 1

    return n_bytes == 0
