# Define the Polybius Square grid
grid = [
    [' ', '5', '4', '3', '2', '1'],
    ['5', 'a', 'b', 'c', 'd', 'e'],
    ['4', 'f', 'g', 'h', 'i/j', 'k'],
    ['3', 'l', 'm', 'n', 'o', 'p'],
    ['2', 'q', 'r', 's', 't', 'u'],
    ['1', 'v', 'w', 'x', 'y', 'z']
]

# Create a dictionary to map letters to values
polybius_dict = {}
for row in range(1, len(grid)):
    for col in range(1, len(grid[0])):
        letter = grid[row][col]
        value = grid[row][0] + grid[0][col]
        polybius_dict[letter] = value

# Handle the case of 'i' and 'j' mapping to the same value '42'
polybius_dict['i'] = '42'
polybius_dict['j'] = '42'

# Example usage:
input_string = "harbkdgsnpo"
values = [polybius_dict[char.lower()] for char in input_string if char.lower() in polybius_dict]
print("Values for each letter:", ' '.join(values))
