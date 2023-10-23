hex_key = "5d41402abc4b2a76b9719d911017c592"
hex1 = "3625354fca224b1edc0bebf66573a1f7"
hex2 = "342d3144db21581ec006f3f7687bbce1"
hex3 = "346c2c373346c92f4513cd05e8f36262b1f7"

# Convert hexadecimal strings to integers
int_key = int(hex_key, 16)
int1 = int(hex1, 16)
int2 = int(hex2, 16)
int3 = int(hex3, 16)

# Perform XOR operation
result = int_key ^ int1
result_2 = int_key ^ int2
result_3 = int_key ^ int3

# Convert the results back to hexadecimal strings
result_hex = hex(result)[2:]  # Remove the '0x' prefix
result_2_hex = hex(result_2)[2:]
result_3_hex = hex(result_3)[2:]

# Ensure the hexadecimal strings have the same length by padding with leading zeros
result_hex = result_hex.zfill(len(hex_key))
result_2_hex = result_2_hex.zfill(len(hex_key))
result_3_hex = result_3_hex.zfill(len(hex_key))

print(result_hex + result_2_hex + result_3_hex)
