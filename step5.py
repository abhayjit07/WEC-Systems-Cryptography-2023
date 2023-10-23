def route_decipher(ciphertext, width):
    height = len(ciphertext) // width
    plaintext = ""
    #create a 2d array of empty strings
    grid = [["" for _ in range(width)] for _ in range(height)]
    #populate the grid with the ciphertext in spiral manner
    #set the initial values
    row = 0
    col = 0
    delta_row = 0
    delta_col = 1

    for char in ciphertext:
        grid[row][col] = char
        #check if the next cell is already occupied
        if grid[(row + delta_row) % height][(col + delta_col) % width]:
            #change direction
            delta_row, delta_col = delta_col, -delta_row
        #move to the next cell
        row += delta_row
        col += delta_col
    
    #read the grid line by line
    for row in grid:
        plaintext += "".join(row)

    return plaintext

    
ciphertext = "harbsfxebwsdraabfinkdgoevtkcuivp"
width = 4
plaintext = route_decipher(ciphertext, width)
print(F"The string obtained is {plaintext}")

print(f"The text to be used for next step: {plaintext[:-21]}")
print(f"Hint: {plaintext[-21:]}")