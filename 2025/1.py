import libs.input

pos = 50
p1, p2 = 0, 0

for line in libs.input.file():
    for _ in range(int(line[1:])):
        if line.startswith("L"):
            pos = (pos + 99) % 100
        else:
            pos = (pos+1) % 100

        if pos == 0:
            p2 += 1

    if pos == 0:
        p1 += 1

print(p1)
print(p2)
