import sys
from collections import deque

rules, parts = open(sys.argv[1]).read().strip().split('\n\n')
memory = {}

for rule in rules.split('\n'):
    name, rest = rule.split('{')
    memory[name] = rest[:-1]


def accepted(part):
    state = 'in'

    while True:
        rule = memory[state]

        for command in rule.split(','):
            applies = True
            result = command

            if ':' in command:
                condition, result = command.split(':')
                variable = condition[0]
                operator = condition[1]
                n = int(condition[2:])

                if operator == '>':
                    applies = part[variable] > n
                else:
                    applies = part[variable] < n

            if applies:
                if result == 'A':
                    return True
                if result == 'R':
                    return False
                state = result
                break


def new_range(operator, n, low, high):
    if operator == '>':
        low = max(low, n + 1)
    elif operator == '<':
        high = min(high, n - 1)
    elif operator == '>=':
        low = max(low, n)
    elif operator == '<=':
        high = min(high, n)
    else:
        assert False

    return (low, high)


def new_ranges(variable, operator, n,
               xlow, xhigh, mlow, mhigh, alow, ahigh, slow, shigh):
    if variable == 'x':
        xlow, xhigh = new_range(operator, n, xlow, xhigh)
    elif variable == 'm':
        mlow, mhigh = new_range(operator, n, mlow, mhigh)
    elif variable == 'a':
        alow, ahigh = new_range(operator, n, alow, ahigh)
    elif variable == 's':
        slow, shigh = new_range(operator, n, slow, shigh)
    return (xlow, xhigh, mlow, mhigh, alow, ahigh, slow, shigh)


answer = 0
Q = deque([('in', 1, 4000, 1, 4000, 1, 4000, 1, 4000)])

for part in parts.split('\n'):
    part = part[1:-1]
    part = {x.split('=')[0]:int(x.split('=')[1]) for x in part.split(',')}
    if accepted(part):
        answer += part['x'] + part['m'] + part['a'] + part['s']

print(answer)
answer = 0

while Q:
    state, xlow, xhigh, mlow, mhigh, alow, ahigh, slow, shigh = Q.pop()
    if xlow > xhigh or mlow > mhigh or alow > ahigh or slow > shigh:
        continue
    if state == 'A':
        score = (xhigh - xlow + 1) * (mhigh - mlow + 1) * (ahigh - alow + 1) * (shigh - slow + 1)
        answer += score
        continue
    elif state=='R':
        continue
    else:
        rule = memory[state]
        for command in rule.split(','):
            applies = True
            result = command
            if ':' in command:
                condition, result = command.split(':')
                variable = condition[0]
                operator = condition[1]
                n = int(condition[2:])
                Q.append((result, * new_ranges(variable, operator, n, xlow, xhigh, mlow, mhigh, alow, ahigh, slow, shigh)))
                xlow, xhigh, mlow, mhigh, alow, ahigh, slow, shigh = new_ranges(variable, '<=' if operator == '>' else '>=', n, xlow, xhigh, mlow, mhigh, alow, ahigh, slow, shigh)
            else:
                Q.append((result, xlow, xhigh, mlow, mhigh, alow, ahigh, slow, shigh))
                break

print(answer)
