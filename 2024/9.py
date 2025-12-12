import libs.input
from collections import deque

data = libs.input.file()[0]

def solve(part2):
    allocations = deque()
    empty_spaces = deque()
    final_layout = []
    position = 0
    file_id = 0

    for idx, char in enumerate(data):
        count = int(char)

        if idx % 2 == 0:
            if part2:
                allocations.append((position, count, file_id))
            for _ in range(count):
                final_layout.append(file_id if not part2 else file_id)
                if not part2:
                    allocations.append((position, 1, file_id))
                position += 1
            file_id += 1
        else:
            empty_spaces.append((position, count))
            for _ in range(count):
                final_layout.append(None)
                position += 1

    for pos, size, fid in reversed(allocations):
        for idx, (space_pos, space_size) in enumerate(empty_spaces):
            if space_pos < pos and size <= space_size:
                for offset in range(size):
                    assert final_layout[pos + offset] == fid
                    final_layout[pos + offset] = None
                    final_layout[space_pos + offset] = fid
                empty_spaces[idx] = (space_pos + size, space_size - size)
                break

    result = sum(idx * c for idx, c in enumerate(final_layout) if c is not None)
    return result

print(solve(False))
print(solve(True))
