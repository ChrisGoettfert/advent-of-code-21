import numpy as np
with open('Input.txt', 'r') as f:
    data = [[int(y) for y in x.strip()] for x in f]



for row in range(len(data)):
    data[row].insert(0, 99)
    data[row].append(99)

t = [99] * (len(data[0]))
data.insert(0, t)
data.append(t)

r = 0
for row in range(1, len(data) - 1):
    for col in range(1, len(data[0]) - 1):
        if data[row][col] < min([data[row -1][col], data[row][col -1], data[row + 1][col], data[row][col+1]]):
            r += data[row][col] + 1


print(r)
