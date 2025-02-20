#!/usr/bin/env python3

import sys

def xor_data(data: bytes, key: bytes) -> bytes:
    """XOR every byte in data with the repeating key bytes."""
    key_len = len(key)
    result = bytearray()
    for i, byte in enumerate(data):
        result.append(byte ^ key[i % key_len])
    return bytes(result)

def main():
    if len(sys.argv) != 4:
        print("Usage: python xor_xor.py <input_file> <key> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    key_str = sys.argv[2]
    output_file = sys.argv[3]

    # Convert the key from string to bytes. You can also allow hex input if needed.
    key = key_str.encode('utf-8')

    # Read the input file as binary data.
    with open(input_file, "rb") as f:
        data = f.read()

    # Process data with XOR operation.
    processed = xor_data(data, key)

    # Write the resulting data to the output file.
    with open(output_file, "wb") as f:
        f.write(processed)

if __name__ == "__main__":
    main()

