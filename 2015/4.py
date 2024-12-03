from hashlib import md5
from itertools import count


def solve(inp, target, start=1):
    for i in count(start):
        m = md5(f"{inp}{i}".encode()).hexdigest()
        if m.startswith(target):
            return i


test_link = open("test.txt").read().strip()
main_link = open("input.txt").read().strip()

print(solve(test_link, 5 * '0'))
print(solve(test_link, 6 * '0'))

print(solve(main_link, 5 * '0'))
print(solve(main_link, 6 * '0'))
