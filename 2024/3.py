import re

input = open("input.txt").read().strip()
cmds = re.findall(r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", input)
do = True
sol1, sol2 = 0, 0
    
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
    
print(sol1)
print(sol2)
