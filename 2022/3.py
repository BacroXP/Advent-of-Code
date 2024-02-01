
rucksacks = open("input.txt").read().strip().split("\n")
groups = []
wrong = []
ids = []


def letter_to_id(letter):
    if 'a' <= letter <= 'z':
        return ord(letter) - ord('a') + 1
    elif 'A' <= letter <= 'Z':
        return ord(letter) - ord('A') + 27
    else:
        raise ValueError("Input must be a letter.")


for rucksack in rucksacks:
    lenR = len(rucksack)

    com1 = list(rucksack[:lenR // 2])
    com2 = list(rucksack[lenR // 2:])

    for item in com1:
        if item in com2:
            wrong.append(letter_to_id(item))
            break

for i, rucksack in enumerate(rucksacks):
    if i // 3 >= len(groups):
        groups.append([])

    groups[i // 3].append(rucksack)

for group in groups:
    for item in group[0]:
        if item in group[1] and item in group[2]:
            ids.append(letter_to_id(item))
            break

print(sum(wrong))
print(sum(ids))
