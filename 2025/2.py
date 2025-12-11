

def divisors(n):
    divs = set()

    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)

    return divs


sol1, sol2 = 0, 0

for inp in open("input.txt").read().strip().split(","):
    inp = inp.split("-")

    if inp[0].startswith("0") or inp[1].startswith("0"):
        continue

    for i in range(int(inp[0]), int(inp[1]) + 1):

        if str(i)[:len(str(i)) // 2] == str(i)[len(str(i)) // 2:]:
            sol1 += i
        
        for d in divisors(len(str(i))):
            if d == len(str(i)):
                continue

            if str(i)[:d] * (len(str(i)) // d) == str(i):
                sol2 += i
                break

print(sol1)
print(sol2)
