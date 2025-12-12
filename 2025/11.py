import libs.input
from libs.efficiency import memoization

edges = {}

for line in libs.input.file():
    node, children_str = line.split(':')
    children = children_str.split()
    edges[node] = children


@memoization
def count_paths(node):
    if node == 'out':
        return 1
    return sum(count_paths(child) for child in edges[node])


@memoization
def count_special_paths(node, seen_dac, seen_fft):
    if node == 'out':
        return 1 if seen_dac and seen_fft else 0

    total = 0
    for child in edges[node]:
        next_seen_dac = seen_dac or (child == 'dac')
        next_seen_fft = seen_fft or (child == 'fft')
        total += count_special_paths(child, next_seen_dac, next_seen_fft)
    return total


print(count_paths('you'))
print(count_special_paths('svr', False, False))