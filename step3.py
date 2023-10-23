hex_string = "6b64756576696168657a766775646465696c716e676a726879776e66786c7973346c7176736c75646f657474756272757465"  

# Convert the hexadecimal string to bytes
bytes_data = bytes.fromhex(hex_string)

# Decode the bytes as ASCII
ascii_string = bytes_data.decode("ascii")

print(f"String obtained: {ascii_string}")

ascii_string_required = ascii_string[:-9] 
print(f"Sting to be used: {ascii_string_required}")

hint = ascii_string[-9:]
print(f"Hint: {hint}") 


