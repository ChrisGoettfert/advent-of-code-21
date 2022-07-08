import numpy as np
from collections import Counter
with open('input3.txt') as f:
    data = [line.rstrip() for line in f]

gamma_ar = []
epsilon_arr = []
for i in range(0,12):
    s = ""
    for line in data:
        s += str(line[i])
    gamma_ar.append(Counter(s).most_common(1)[0][0])
    epsilon_arr.append(Counter(s).most_common()[-1][0])
gamma = int(''.join(n for n in gamma_ar if n.isdigit()), 2)
epislon = int(''.join(k for k in epsilon_arr if k.isdigit()), 2)
print(gamma * epislon)


oxygen_ar = []
data2 = data.copy()
for i in range(0,12):
    s = ""
    for line in data:
        s += str(line[i])
    s = list(s)
    desired_array = [int(numeric_string) for numeric_string in s]
    avg = sum(desired_array)/len(desired_array)
    if(avg) == 0.5:
        most_common = 1
    else:
        if(avg > 0.5):
            most_common = 1
        else:
            most_common = 0
    for l in data[:]:
        if(int(l[i]) is not int(most_common)):
            data.remove(l)
        if(len(data) == 1):
            oxygen = int(''.join(n for n in data if n.isdigit()), 2)
            print(oxygen)
            break

    print(data)

for i in range(0,12):
    s = ""
    for line in data2:
        s += str(line[i])
    s = list(s)
    desired_array = [int(numeric_string) for numeric_string in s]
    avg = sum(desired_array) / len(desired_array)
    if (avg) == 0.5:
        most_common = 0
    else:
        if (avg > 0.5):
            most_common = 0
        else:
            most_common = 1
    for l in data2[:]:
        if(int(l[i]) is not int(most_common)):
            data2.remove(l)
        if(len(data2) == 1):
            co2 = int(''.join(n for n in data2 if n.isdigit()), 2)
            print(co2)
            print("res ", oxygen * co2)
            break

    print(data2)

#print(oxygen * co2)
print(3871 * 613)
#print()