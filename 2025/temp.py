import libs.input
import libs.vars
import libs.maze
import libs.efficiency

import math
import sys

sys.setrecursionlimit(10**7)

inp = libs.input.file()
nums = libs.input.nums(inp)
sol1 = 0
sol2 = 0

for line, num in zip(inp, nums):
    print(f"Line: {line}, Number: {num}")
