import libs.input

file = libs.input.word_file()
file2 = libs.input.file()
file.reverse()
sol1, sol2 = 0, 0
ops, ends, groups = [], [], []

for i, op in enumerate(file[0]):
    acc = 0 if op == "+" else 1

    for r in file[1:]:
        v = int(r[i])
        acc = acc + v if op == "+" else acc * v

    sol1 += acc

for i, c in enumerate(file2[-1]):
    if c in "+*":
        ops.append(c)
        ends.append(i)
        groups.append([])

ends.append(len(file2[0]))

for row in file2[:-1]:
    for idx in range(len(ops)):
        segment = row[ends[idx]:ends[idx + 1]]
        g = groups[idx]

        for j, ch in enumerate(segment):
            if len(g) <= j:
                g.append([])

            g[j].append(ch)

for idx, op in enumerate(ops):
    acc = 0 if op == "+" else 1
    nums = []

    for chars in groups[idx]:
        s = "".join(c for c in chars if c.isdigit())
        nums.append(int(s) if s else 0)

    if nums and nums[-1]:
        nums.append(0)

    for n in nums[:-1]:
        acc = acc + n if op == "+" else acc * n

    sol2 += acc

print(sol1)
print(sol2)
