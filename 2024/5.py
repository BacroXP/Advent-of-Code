import libs.input

cmds, data = open("input.txt").read().strip().split("\n\n")
cmds = [cmd.split("|") for cmd in cmds.split("\n")]
sol1, sol2 = 0, 0


def permute(arr, c=None, p=None):
    if c is None:
        c = []
    if p is None:
        p = []
    if not arr:
        p.append(c[:])
        return p
    else:
        for i, el in enumerate(arr):
            temp = c + [el]
            temp2 = arr[:i] + arr[i+1:]
            permute(temp2, temp, p)
        return p


for pages in [d.split(",") for d in data.split("\n")]:
    if all(not (cmd[0] in pages and cmd[1] in pages) or pages.index(cmd[0]) < pages.index(cmd[1]) for cmd in cmds):
        sol1 += int(pages[len(pages) // 2])
    else:
        for var in permute(pages):
            if all(not (cmd[0] in var and cmd[1] in var) or var.index(cmd[0]) < var.index(cmd[1]) for cmd in cmds):
                sol2 += int(var[len(var) // 2])
                break

print(sol1)
print(sol2)
