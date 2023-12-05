import sys


def read_file_content(filename):
    try:
        with open(filename, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)


def parse_function_string(function_string):
    lines = function_string.split('\n')[1:]  # throw away name
    tuples = [[int(x) for x in line.split()] for line in lines]
    return tuples


class Function:
    def __init__(self, function_string):
        self.tuples = parse_function_string(function_string)

    def apply_one(self, x):
        for (dst, src, sz) in self.tuples:
            if src <= x < src + sz:
                return x + dst - src
        return x

    def apply_range(self, ranges):
        new_ranges = []
        for (dest, src, sz) in self.tuples:
            src_end = src + sz
            temp_ranges = []
            while ranges:
                (st, ed) = ranges.pop()
                before = (st, min(ed, src))
                inter = (max(st, src), min(src_end, ed))
                after = (max(src_end, st), ed)
                if before[1] > before[0]:
                    temp_ranges.append(before)
                if inter[1] > inter[0]:
                    new_ranges.append((inter[0] - src + dest, inter[1] - src + dest))
                if after[1] > after[0]:
                    temp_ranges.append(after)
            ranges = temp_ranges
        return new_ranges + ranges


def main():
    filename = "input.txt"
    content = read_file_content(filename)

    parts = content.split('\n\n')
    seed, *function_strings = parts
    seed = [int(x) for x in seed.split(':')[-1].split()]

    functions = [Function(func_str) for func_str in function_strings]

    part1 = [x for x in seed]
    for func in functions:
        part1 = [func.apply_one(x) for x in part1]

    print("Part 1 Result:", min(part1))

    part2 = []
    pairs = list(zip(seed[::2], seed[1::2]))
    for st, sz in pairs:
        ranges = [(st, st + sz)]
        for func in functions:
            ranges = func.apply_range(ranges)
        part2.append(min(ranges)[0])

    print("Part 2 Result:", min(part2))


if __name__ == "__main__":
    main()
