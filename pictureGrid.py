grid = [
['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']
]

# Calculate the dimensions of the grid
num_rows = len(grid)
num_cols = len(grid[0])

# Loop through the grid and print characters row by row
for y in range(num_cols):
    for x in range(num_rows):
        print(grid[x][y], end='')
    print()  # Print a newline to move to the next row
    