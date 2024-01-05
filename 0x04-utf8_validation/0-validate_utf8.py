#!/usr/bin/python3
"""UTF-8 Validation"""

def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.
    """
    remaining_bytes = 0
    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for byte in data:
        mask_byte = 1 << 7

        if remaining_bytes == 0:
            # Count the number of leading 1s to determine the number of bytes
            while mask_byte & byte:
                remaining_bytes += 1
                mask_byte >>= 1

            if remaining_bytes == 0:
                continue

            # Check if the number of bytes is valid
            if remaining_bytes == 1 or remaining_bytes > 4:
                return False

        else:
            # Check if the byte follows the UTF-8 format
            if not (byte & mask_1 and not (byte & mask_2)):
                return False

        remaining_bytes -= 1

    return remaining_bytes == 0

# Test cases
data1 = [65]
print(validUTF8(data1))

data2 = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data2))

data3 = [229, 65, 127, 256]
print(validUTF8(data3))
