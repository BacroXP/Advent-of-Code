import libs.input
import libs.vars
import libs.maze
import libs.efficiency

import math
import sys


def divisors(n):
    divs = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
    return divs


sys.setrecursionlimit(10**7)

inputs = open("input.txt").read().strip().split(",")
sol = 0
sol2 = 0

for inp in inputs:
    inp = inp.split("-")

    if inp[0].startswith("0") or inp[1].startswith("0"):
        continue

    for i in range(int(inp[0]), int(inp[1]) + 1):

        if str(i)[:len(str(i)) // 2] == str(i)[len(str(i)) // 2:]:
            sol += i
        
        for d in divisors(len(str(i))):
            if d == len(str(i)):
                continue

            if str(i)[:d] * (len(str(i)) // d) == str(i):
                sol2 += i
                break

print(sol)
print(sol2)