file = open("input.txt").read().strip()
lines = file.split('\n')

data = {}


def f(space, fountains, i, bi, current):
    key = (i, bi, current)
    if key in data:
        return data[key]

    if i == len(space):
        if bi == len(fountains) and current == 0:
            return 1
        elif bi == len(fountains)-1 and fountains[bi] == current:
            return 1
        else:
            return 0

    anz = 0

    for c in ['.', '#']:
        if space[i] == c or space[i] == '?':
            if c == '.' and current == 0:
                anz += f(space, fountains, i+1, bi, 0)
            elif c == '.' and current > 0 and bi < len(fountains) and fountains[bi] == current:
                anz += f(space, fountains, i+1, bi+1, 0)
            elif c == '#':
                anz += f(space, fountains, i+1, bi, current + 1)

    data[key] = anz
    return anz


for part2 in [False, True]:
    ans = 0
    for line in lines:
        dots, blocks = line.split()
        if part2:
            dots = '?'.join([dots, dots, dots, dots, dots])
            blocks = ','.join([blocks, blocks, blocks, blocks, blocks])

        blocks = [int(x) for x in blocks.split(',')]
        data.clear()
        score = f(dots, blocks, 0, 0, 0)
        ans += score
    print(ans)
