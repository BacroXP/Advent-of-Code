
jam = open("input.txt").read().strip()
chars = []
diff = False
i = 0

for l in [4, 14]:
    diff = False

    while not diff:
        if len(chars) == l:
            print(i + l - 1)
            diff = True

        chars = []

        for char in jam[i: i + l]:
            if char not in chars:
                chars.append(char)

        i += 1
