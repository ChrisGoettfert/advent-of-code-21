import numpy as np
data = open('Input.txt','r').read().strip().split('\n')
x = []
y = []
folds = []
for line in data:
    if(',') in line:
        x.append(int(line.split(",")[0]))
        y.append(int(line.split(",")[1]))
    elif('fold') in line:
        folds.append([line.split("=")])

grid = np.zeros(shape=(max(y) + 1, max(x) + 1), dtype="bool")

# fil grid first time # 14 is out of range bc starting at 0
for i in range(len(x)):
    grid[y[i]][x[i]] = True
g1 = []
g2 = []
for f in enumerate(folds):
    axis = f[1][0][0][-1]
    pos = int(f[1][0][1])
    if axis == 'x':
        half_1 = grid[...,0:pos]
        half_2 = np.flip(grid[..., pos+1:], axis=1)
    elif axis == 'y':
        half_1 = grid[0:pos, ...]
        half_2 = np.flip(grid[pos+1:, ...], axis=0)
        print()
    grid = half_1 | half_2
    print()
    dots_count = np.count_nonzero(grid)
    print(f"Part 1: {dots_count} dots")
    print()
dots_count = np.count_nonzero(grid)
print(f"Part 1: {dots_count} dots")

output = ""
for row in grid:
    line = ""
    for valid in row:
        line += "#" if valid else " "
    output += line + "\n"

print(output)