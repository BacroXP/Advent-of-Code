file = open("input.txt").read().strip()

for part2 in [False, True]:
    ans = 0

    for grid in file.split('\n\n'):
        chars = [[c for c in row] for row in grid.split('\n')]
        len_row = len(chars)
        len_column = len(chars[0])

        for c in range(len_column - 1):
            incorrect = 0
            for dc in range(len_column):
                left = c - dc
                right = c + 1 + dc
                if 0 <= left < right < len_column:
                    for r in range(len_row):
                        if chars[r][left] != chars[r][right]:
                            incorrect += 1

            if incorrect == (1 if part2 else 0):
                ans += c + 1

        for r in range(len_row - 1):
            incorrect = 0
            for dr in range(len_row):
                up = r - dr
                down = r + 1 + dr
                if 0 <= up < down < len_row:
                    for c in range(len_column):
                        if chars[up][c] != chars[down][c]:
                            incorrect += 1

            if incorrect == (1 if part2 else 0):
                ans += 100 * (r + 1)

    print(ans)
