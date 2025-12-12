ranges, nums = [area.split("\n") for area in open("input.txt").read().strip().split("\n\n")]
ranges = [r.split("-") for r in ranges]
sol1, sol2, biggest = 0, 0, 0

for r in ranges:
    if int(r[1]) > biggest:
        biggest = int(r[1])

for num in nums:
    num = int(num)
    spoiled = True

    for r in ranges:
        if int(r[0]) <= num <= int(r[1]):
            spoiled = False

    if not spoiled:
        sol1 += 1

for i in range(biggest):
    spoiled = True

    for r in ranges:
        if int(r[0]) <= i <= int(r[1]):
            spoiled = False

    if not spoiled:
        sol2 += 1

print(sol1)
print(sol2)
