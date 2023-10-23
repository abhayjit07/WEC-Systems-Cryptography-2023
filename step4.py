ciphertext = "kdueviahezvguddeilqngjrhywnfxlys4lqvsludo"
plaintext = ""
for char in ciphertext:
        if char.isalpha():
            # Shift the character back by 3
            char_code = ord(char) - 3
            # Handle wraparound
            if char.isupper():
                if char_code < ord('A'):
                    char_code += 26
            else:
                if char_code < ord('a'):
                    char_code += 26
            plaintext += chr(char_code)
        else:
            plaintext += char
print(plaintext)
