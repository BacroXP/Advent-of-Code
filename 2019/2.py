

def do_calc(op, pos1, pos2, sol, code):
    if op == 99:
        if i == 12 and j == 2:
            print(opcode[0])

        if opcode[0] == 19690720:
            print(str(i) + str(j))
    elif op == 1:
        opcode[sol] = int(code[pos1]) + int(code[pos2])
    elif op == 2:
        opcode[sol] = int(code[pos1]) * int(code[pos2])


for i in range(99):
    for j in range(99):
        opcode = open("input.txt").read().strip().split(",")

        opcode[1] = i
        opcode[2] = j

        for ii in range(len(opcode) // 4):
            jj = ii * 4

            do_calc(int(opcode[jj]), int(opcode[jj + 1]), int(opcode[jj + 2]), int(opcode[jj + 3]), opcode)
