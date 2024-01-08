from z3 import *
import time

offset = time.time()

D = open("input.txt").read().strip()
L = D.split('\n')
G = [[c for c in row] for row in L]
R = len(G)
C = len(G[0])

S = []
for line in L:
    pos, vel = line.split('@')
    x, y, z = map(int, pos.split(', '))
    vx, vy, vz = map(int, vel.split(', '))
    S.append((x, y, z, vx, vy, vz))

# Part 1: Pairwise Intersection Calculation
ans = 0
for i in range(len(S)):
    for j in range(i + 1, len(S)):
        x1, x2 = S[i][0], S[i][0] + S[i][3]
        x3, x4 = S[j][0], S[j][0] + S[j][3]
        y1, y2 = S[i][1], S[i][1] + S[i][4]
        y3, y4 = S[j][1], S[j][1] + S[j][4]

        den = ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
        if den != 0:
            px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / den
            py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / den
            validA = (px > x1) == (x2 > x1)
            validB = (px > x3) == (x4 > x3)

            if 200000000000000 <= px <= 400000000000000\
                    and 200000000000000 <= py <= 400000000000000\
                    and validA and validB:
                ans += 1

print("Part 1:", ans)
print(time.time() - offset)
offset = time.time()

# Part 2: Z3 Solver
x, y, z, vx, vy, vz = Int('x'), Int('y'), Int('z'), Int('vx'), Int('vy'), Int('vz')
T = [Int(f'T{i}') for i in range(len(S))]
SOLVE = Solver()

for i in range(len(S)):
    SOLVE.add(x + T[i] * vx - S[i][0] - T[i] * S[i][3] == 0)
    SOLVE.add(y + T[i] * vy - S[i][1] - T[i] * S[i][4] == 0)
    SOLVE.add(z + T[i] * vz - S[i][2] - T[i] * S[i][5] == 0)

res = SOLVE.check()
M = SOLVE.model()
print("Part 2:", M.eval(x + y + z))
print(time.time() - offset)
