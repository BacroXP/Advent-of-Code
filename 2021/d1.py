depths = [int(d) for d in open("input.txt").read().strip().split()]
sol1, sol2 = 0, 0

for x, item in enumerate(depths):
    if x >= 1 and item > depths[(x - 1)]:
        sol1 += 1
    if x >= 3 and item > depths[(x - 3)]:
        sol2 += 1

print(str(sol1) + "\n" + str(sol2))