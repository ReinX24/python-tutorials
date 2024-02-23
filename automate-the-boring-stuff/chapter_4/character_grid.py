grid = [
    [".", ".", ".", ".", ".", "."],
    [".", "O", "O", ".", ".", "."],
    ["O", "O", "O", "O", ".", "."],
    ["O", "O", "O", "O", "O", "."],
    [".", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "."],
    ["O", "O", "O", "O", ".", "."],
    [".", "O", "O", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
]

width = 0
height = 0

for x in range(len(grid)):
    height += 1

for y in range(len(grid[0])):
    width += 1

for x in range(width):
    for y in range(height):
        print(grid[y][x], end="")
    print()
