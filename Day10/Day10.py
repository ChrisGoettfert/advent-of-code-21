data = open('Input.txt','r').read().strip().split('\n')
brackets = {')': '(', ']': '[', '}': '{', '>': '<'}

points = {')': 3, ']': 57, '}': 1197, '>': 25137}
r = 0
for line in data:
    pending = []
    for char in line:
        if char in brackets.values():
            pending.append(char)
        if char in brackets.keys():
            if(pending[-1] == brackets.get(char)):
                pending.pop()
            else:
                r += points.get(char)
                print()
                break

print(r)
