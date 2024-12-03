def sol(address):
    cmds = open(address).read().strip()
    santa = True
    sol1 = 0
    sol2 = 0

    santa_x, santa_y = 0, 0
    santa_positions = set()
    santa_positions.add((santa_x, santa_y))

    for char in cmds:
        if char == '^':
            santa_y += 1
        elif char == 'v':
            santa_y -= 1
        elif char == '>':
            santa_x += 1
        elif char == '<':
            santa_x -= 1

        santa_positions.add((santa_x, santa_y))

    sol1 = len(santa_positions)

    santa_x = 0
    santa_y = 0
    elf_x = 0
    elf_y = 0
    
    positions = set()
    positions.add((0, 0))
    
    for char in cmds:
        if char == '^':
            if santa:
                santa_y += 1
            else:
                elf_y += 1
        elif char == 'v':
            if santa:
                santa_y -= 1
            else:
                elf_y -= 1
        elif char == '>':
            if santa:
                santa_x += 1
            else:
                elf_x += 1
        elif char == '<':
            if santa:
                santa_x -= 1
            else:
                elf_x -= 1
        
        positions.add((santa_x, santa_y) if santa else (elf_x, elf_y))
        
        santa = not santa
    
    sol2 = len(positions)

    print("Solution 1: " + str(sol1))
    print("Solution 2: " + str(sol2))


test_link = "test.txt"
real_link = "input.txt"

sol(test_link)
sol(real_link)
