import numpy as np

with open('Data.txt', 'r') as f:
    data = np.array(f.read().split('\n'), dtype='int')

result = 0

for idx, val in enumerate(data):

    if(val > data[idx - 1]):
        result+=1
print(result)
result = 0
oldSum = None

tuppleList = [data[i:i + 3] for i in range(0, len(data))]
for triplet in tuppleList:
    if len(triplet) < 3:
        break
    depth = sum(triplet)
    if oldSum and depth > oldSum:
        result += 1
    oldSum = sum(triplet)

print(result)
