import re

test_link = "test.txt"
real_link = "input.txt"


def sol(address):
    input = open(address).read().strip()
    cmds = re.findall(r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", input)
    do = True
    sol1 = 0
    sol2 = 0
    
    for value in cmds:
        
        if value == "do()":
            do = True
        elif value == "don't()":
            do = False
        else:
            value = value.replace("mul(", "").replace(")", "")

            if do:
                sol2 += int(value.split(",")[0]) * int(value.split(",")[1])
            
            sol1 += int(value.split(",")[0]) * int(value.split(",")[1])
    
    print("Solution 1: " + str(sol1))
    print("Solution 2: " + str(sol2))


sol(test_link)
sol(real_link)
