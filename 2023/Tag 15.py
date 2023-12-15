D = open("input.txt").read().strip()
commands = D.split(',')

BOX = [[] for _ in range(256)]

part1 = 0
part2 = 0


def calc(string):
    h = 0

    for char in string:
        h += ord(char)
        h *= 17
        h %= 256

    return h


def find_order(c):
    if c[-1] == '-':
        name = c[:-1]
        hash = calc(name)
        BOX[hash] = [(n, v) for (n, v) in BOX[hash] if n != name]
    elif c[-2] == '=':
        name = c[:-2]
        hash = calc(name)
        len_ = int(c[-1])

        if name in [n for (n, v) in BOX[hash]]:
            BOX[hash] = [(n, len_ if name == n else v) for (n, v) in BOX[hash]]
        else:
            BOX[hash].append((name, len_))


for command in commands:
    part1 += calc(command)
    find_order(command)

for i, box in enumerate(BOX):
    for j, (n, v) in enumerate(box):
        part2 += (i + 1) * (j + 1) * v

print(part1)
print(part2)
