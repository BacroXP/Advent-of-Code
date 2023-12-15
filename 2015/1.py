import sys

distr = {"(": 1, ")": -1}
commands = []

with open(sys.argv[1]) as file:
    for line in file:
        for char in line:
            if char != "\n":
                commands.append(distr[char])

print(sum(commands))

floor = 0
sols = []

for i, c in enumerate(commands):
    floor += c
    
    if floor == -1:
        sols.append(i + 1)

sols.sort()
print(sols[0])
