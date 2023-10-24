string = "43 55 24 54 41 52 44 23 33 31 32"  

# Convert the hexadecimal string to bytes
bytes_data = bytes.fromhex(string)

# Decode the bytes as ASCII
ascii_string = bytes_data.decode("ascii")

print(f"String obtained: {ascii_string}")

