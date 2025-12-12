import math

*presents, regions = open("input.txt").read().split('\n\n')
sizes = {}
ans = 0

for present in presents:
    sizes[int(present.splitlines()[0][:-1])] = sum(row.count("#") for row in present.splitlines()[1:])

for region in regions.splitlines():
    grid_size, count = region.split(': ')

    if sum(n * sizes[i] for i, n in enumerate([int(x) for x in count.split()])) * 1.3 < math.prod([int(x) for x in grid_size.split('x')]):
        ans += 1

print(ans)