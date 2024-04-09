def differential_cryptanalysis(key, plaintext, ciphertext, s_box, p_box, round_key):
    # Initialize the difference distribution table
    ddt = [[0] * 256 for _ in range(256)]

    # Iterate over all possible input differences
    for input_diff in range(256):
        # Iterate over all possible output differences
        for output_diff in range(256):
            # Calculate the number of times the output difference occurs for the given input difference
            count = 0
            for plain in range(256):
                if s_box[plain ^ input_diff] ^ s_box[plain] == output_diff:
                    count += 1
            ddt[input_diff][output_diff] = count

    # Iterate over all possible key differences
    for key_diff in range(256):
        # Calculate the corresponding ciphertext difference
        cipher_diff = s_box[plaintext ^ key_diff] ^ s_box[plaintext] ^ ciphertext

        # Check if the ciphertext difference matches any entry in the DDT
        for input_diff in range(256):
            if ddt[input_diff][cipher_diff] > 0:
                # If so, the key difference is a possible candidate
                print("Possible key difference:", hex(key_diff))

# Example usage
key = 0x12
plaintext = 0x34
ciphertext = 0x56
s_box = [0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xA, 0xB, 0xC, 0xD, 0xE, 0xF]
p_box = [0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7]
round_key = 0x78

differential_cryptanalysis(key, plaintext, ciphertext, s_box, p_box, round_key)