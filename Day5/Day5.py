import numpy as np
with open('Input.txt') as f:
    data = [line.rstrip().split("->")for line in f]

field = np.zeros(shape=(1000,1000), dtype=int)
for coords in data:
    startx = int(coords[0].split(",")[0])
    starty = int(coords[0].split(",")[1])
    endx = int(coords[1].split(",")[0])
    endy = int(coords[1].split(",")[1])


    #if(startx == endx or starty == endy):
    for x in range(min(startx, endx), max(startx, endx) + 1):
        for y in range(min(starty, endy), max(starty, endy) + 1):
            field[x][y] += 1
            

print(len([a for a in field.flatten() if (a > 1)]))


print()