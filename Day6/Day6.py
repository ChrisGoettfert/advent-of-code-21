import numpy as np
with open('Input.txt', 'r') as f:
    data = np.array(f.read().split(','), dtype='int')

fishes = dict.fromkeys((range(9)), 0)

for e in data:
    fishes[e] += 1

for i in range(256):
    temp = fishes[0]
    fishes[0] = fishes[1]
    fishes[1] = fishes[2]
    fishes[2] = fishes[3]
    fishes[3] = fishes[4]
    fishes[4] = fishes[5]
    fishes[5] = fishes[6]
    fishes[6] = fishes[7] + temp
    fishes[7] = fishes[8]
    fishes[8] = temp
    print()

a = 0
for e in fishes:
    a += fishes[e]
print(a)

print()