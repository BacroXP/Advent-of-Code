import libs.input

nums = libs.input.word_file()[0]
sol1, sol2 = 0, 0
data_reaccourances = {}


def solve(x, t):
    if (x, t) in data_reaccourances:
        return data_reaccourances[(x, t)]

    if t == 0:
        ret = 1

    elif x == 0:
        ret = solve(1, t - 1)

    elif len(str(x)) % 2 == 0:
        dstr = str(x)
        left = dstr[:len(dstr)//2]
        right = dstr[len(dstr)//2:]
        left, right = (int(left), int(right))
        ret = solve(left, t-1) + solve(right, t-1)

    else:
        ret = solve(x*2024, t-1)

    data_reaccourances[(x,t)] = ret
    return ret


print(sum(solve(int(x), 25) for x in nums))
print(sum(solve(int(x), 75) for x in nums))
