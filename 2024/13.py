import libs.input
import re
from fractions import Fraction

def read_machines(lines):
    it = iter(lines)
    while True:
        nums = []
        nums += re.fullmatch(r'Button A: X\+(\d+), Y\+(\d+)', next(it)).groups()
        nums += re.fullmatch(r'Button B: X\+(\d+), Y\+(\d+)', next(it)).groups()
        nums += re.fullmatch(r'Prize: X=(\d+), Y=(\d+)', next(it)).groups()
        yield tuple(map(int, nums))

        sep = next(it, None)
        if sep is None:
            break
        assert sep == ''

def tokens_spent(lines, prize_shift=0):
    total_tokens = 0

    for a_dx, a_dy, b_dx, b_dy, target_x, target_y in read_machines(lines):
        target_x += prize_shift
        target_y += prize_shift

        denom = a_dy * b_dx - a_dx * b_dy
        assert denom != 0

        presses_a = Fraction(-(b_dy * target_x - b_dx * target_y), denom)
        presses_b = Fraction((a_dy * target_x - a_dx * target_y), denom)

        if presses_a.denominator != 1 or presses_b.denominator != 1:
            continue

        if prize_shift == 0:
            assert presses_a.numerator < 100 and presses_b.numerator < 100

        total_tokens += 3 * presses_a + presses_b

    return total_tokens

lines = libs.input.file()

print(tokens_spent(lines))
print(tokens_spent(lines, 10_000_000_000_000))
