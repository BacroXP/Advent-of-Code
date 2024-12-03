cmds = open("input.txt").read().strip().split("\n")
x, y, sol2 = 0, 0, 0

for cmd in cmds:
    cmd, var = cmd.split()
    var = int(var)
    
    if cmd == "forward":
        x += var
        sol2 += y * var
    elif cmd == "down":
        y += var
    elif cmd == "up":
        y -= var
    
print(x * y)
print(x * sol2)