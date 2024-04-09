def linear_cryptanalysis(key, plaintext, ciphertext, s_box, p_box, round_key):
    # Initialize the correlation array
    correlation = [0] * 256

    # Iterate over all possible values of the intermediate value
    for intermediate in range(256):
        # Calculate the expected difference
        expected_diff = s_box[intermediate ^ p_box[0]] ^ s_box[intermediate]

        # Iterate over all possible values of the plaintext
        for plain in range(256):
            # Calculate the corresponding ciphertext
            cipher = s_box[plain ^ key] ^ round_key

            # Check if the difference matches the expected difference
            if cipher ^ s_box[plain ^ intermediate] == expected_diff:
                correlation[intermediate] += 1

    # Find the maximum correlation
    max_correlation = max(correlation)

    # Find the corresponding intermediate value
    for intermediate in range(256):
        if correlation[intermediate] == max_correlation:
            return intermediate

# Example usage
key = 0x12
plaintext = 0x34
ciphertext = 0x56
s_box = [0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xA, 0xB, 0xC, 0xD, 0xE, 0xF]
p_box = [0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7]
round_key = 0x78

intermediate = linear_cryptanalysis(key, plaintext, ciphertext, s_box, p_box, round_key)
print("Intermediate value:", hex(intermediate))