
tasks = open("input.txt").read().strip().split("\n")
in_it = 0
overlapping = 0

for task in tasks:
    elf1, elf2 = [elf.split("-") for elf in task.split(",")]
    off1 = int(elf1[0]) - int(elf2[0])
    off2 = int(elf1[1]) - int(elf2[1])

    if off1 <= 0 <= off2 or off1 >= 0 >= off2:
        in_it += 1

    if int(elf1[0]) <= int(elf2[0]) <= int(elf1[1]):
        overlapping += 1

    elif int(elf1[0]) <= int(elf2[1]) <= int(elf1[1]):
        overlapping += 1

    elif int(elf2[0]) <= int(elf1[0]) <= int(elf2[1]):
        overlapping += 1

    elif int(elf2[0]) <= int(elf1[1]) <= int(elf2[1]):
        overlapping += 1

print(in_it)
print(overlapping)
