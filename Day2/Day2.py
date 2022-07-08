import numpy as np

with open('Input2.txt', 'r') as f:
    data = np.array(f.read().split('\n'))


startPos = 0
startDepth = 0

for dataPoint in data:
    if("forward" in dataPoint):
        startPos += int(dataPoint[-1])
    else:
        if("up" in dataPoint):
            startDepth -= int(dataPoint[-1])
        elif("down" in dataPoint):
            startDepth += int(dataPoint[-1])

print(startPos)
print(startDepth)
print(startPos * startDepth)


def part2():
    startPos = 0
    startDepth = 0
    aim = 0
    for dataPoint in data:
        if ("forward" in dataPoint):
            startPos += int(dataPoint[-1])
            startDepth += int(dataPoint[-1]) * aim
        else:
            if ("up" in dataPoint):
                #startDepth -= int(dataPoint[-1])
                aim -= int(dataPoint[-1])
            elif ("down" in dataPoint):
                #startDepth += int(dataPoint[-1])
                aim += int(dataPoint[-1])
    print(startPos * startDepth)

part2()
