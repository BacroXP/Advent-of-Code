from collections import deque

def getDependencies(maze: list[list[str]], start="S", end="E") -> tuple[tuple[int, int], tuple[int, int]]:
    start_pos, end_pos = None, None
    for i, row in enumerate(maze):
        if start in row:
            start_pos = (i, row.index(start))
        if end in row:
            end_pos = (i, row.index(end))
    if start_pos is None or end_pos is None:
        raise ValueError("Start or End not found in the maze!")
    return start_pos, end_pos

def findAllPaths(maze: list[list[str]], start: tuple[int, int], end: tuple[int, int]) -> list[list[tuple[int, int]]]:
    rows, cols = len(maze), len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start, [start])])
    all_paths = []

    while queue:
        (current_row, current_col), path = queue.popleft()
        if (current_row, current_col) == end:
            all_paths.append(path)
            continue
        for dr, dc in directions:
            nr, nc = current_row + dr, current_col + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] in (".", "E") and (nr, nc) not in path:
                queue.append(((nr, nc), path + [(nr, nc)]))
    return all_paths

def findAllPathsLength(maze: list[list[str]], start: tuple[int, int], end: tuple[int, int]) -> list[int]:
    all_paths = findAllPaths(maze, start, end)
    return [len(path) for path in all_paths]

def findShortestPath(maze: list[list[str]], start: tuple[int, int], end: tuple[int, int]) -> list[list[str]]:
    maze_copy = [row[:] for row in maze]
    all_paths = findAllPaths(maze, start, end)

    if not all_paths:
        return maze_copy

    shortest_path = min(all_paths, key=len)
    for row, col in shortest_path:
        if maze_copy[row][col] == ".":
            maze_copy[row][col] = "?"
    return maze_copy

def findShortestPathLength(maze: list[list[str]], start: tuple[int, int], end: tuple[int, int]) -> int:
    all_paths = findAllPaths(maze, start, end)
    if not all_paths:
        return 0
    return len(min(all_paths, key=len))

def findLongestPath(maze: list[list[str]], start: tuple[int, int], end: tuple[int, int]) -> list[list[str]]:
    maze_copy = [row[:] for row in maze]
    all_paths = findAllPaths(maze, start, end)

    if not all_paths:
        return maze_copy

    longest_path = max(all_paths, key=len)
    for row, col in longest_path:
        if maze_copy[row][col] == ".":
            maze_copy[row][col] = "?"

    return maze_copy

def findLongestPathLength(maze: list[list[str]], start: tuple[int, int], end: tuple[int, int]) -> int:
    all_paths = findAllPaths(maze, start, end)

    if not all_paths:
        return 0

    return len(max(all_paths, key=len))
