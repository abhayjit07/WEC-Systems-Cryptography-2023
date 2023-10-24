# WEC-Systems-Cryptography-2023

## Step 1: MD5 Hash

### About MD5 Hash
- MD5 (Message Digest Algorithm 5) is a widely used cryptographic hash function. 
- It takes an input (such as a string of text or a file) and produces a fixed-size 128-bit hash value, which is typically represented as a 32-character hexadecimal number.

### Hint to apply MD5 Hash
- Hint given in the question `Say hello and xor to MD5`.

### Application
- Perform MD5 hash of "hello."
- Text obtained: `5d41402abc4b2a76b9719d911017c592`

## Step 2: XOR Operations

### Hint to apply XOR operation.
- Hint given in the question `Say hello and xor to MD5`.

### Application
- XOR operation 1: `5d41402abc4b2a76b9719d911017c592` ^ `3625354fca224b1edc0bebf66573a1f7`
- Output of XOR operation 1: `6b64756576696168657a766775646465`
- XOR operation 2: `5d41402abc4b2a76b9719d911017c592` ^ `342d3144db21581ec006f3f7687bbce1`
- Output of XOR operation 2: `696c716e676a726879776e66786c7973`
- XOR operation 3: `5d41402abc4b2a76b9719d911017c592` ^ `346c2c373346c92f4513cd05e8f36262b1f7`
- Output of XOR operation 3: `346c7176736c75646f657474756272757465`

- Concatenate the 3 strings to obtain: `6b64756576696168657a766775646465696c716e676a726879776e66786c7973346c7176736c75646f657474756272757465`

## Step 3: Convert to ASCII

- Convert the string obtained in step 2 to ASCII.
- String obtained: `kdueviahezvguddeilqngjrhywnfxlys4lqvsludoettubrute`

## Step 4: Et tu Brute

- Using the hint "ettubrute," apply a Caesar decipher technique on the string to obtain: `harbsfxebwsdraabfinkdgoevtkcuivp4inspiral`

## Step 5: Route Decipher

- Using the hint "4inspiral" in the string `harbsfxebwsdraabfinkdgoevtkcuivp4inspiral`, apply route decipher with a width size of 4.
- The hint obtained after deciphering `fivexfivebutbackwards` 

## Step 6: Polybius Square
- Using this hint we apply the "Polybius Square Encryption" Technique on the string `harbkdgsnpo`.
- The number obtained is `43 55 24 54 41 52 44 23 33 31 32`

## Step 7: Converting Hexadecimal to ASCII 
- The ASCII String obtained is `CU$TARD#312`.
  


