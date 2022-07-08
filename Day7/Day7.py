import numpy as np
with open('Input.txt', 'r') as f:
    data = np.array(f.read().strip(), dtype='int')

median = np.median(data)

res = 0
for pos in data:
    res += abs(median - pos)
print(int(res))

# part 2
avg = int(np.mean(data))
res = 0
for pos in data:
    t = 0
    for i in range(0, abs(avg - pos) + 1):
        t += i
    res += t
print(res)
