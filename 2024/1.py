sol1, sol2 = 0, 0
file = open("input.txt").read().split()
right = [int(n) for n in file[1::2]]

for l, r in zip(sorted([int(n) for n in file[::2]]), sorted(right)):
    sol1 += abs(l - r)
    sol2 += l * right.count(l)

print(sol1)
print(sol2)
