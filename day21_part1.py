from collections import deque


def find_start(lines):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "S":
                return (i, j)
    return (-1, -1)


def reachable_garden_plots(lines):
    r_start, c_start = find_start(lines)
    matrix = []
    for line in lines:
        matrix.append([char for char in line])
    initial_steps = 64

    queue = deque([(r_start, c_start, initial_steps)])
    matrix[r_start][c_start] = "."
    visited = set([(r_start, c_start)])
    possible = set()

    while queue:
        r, c, steps_left = queue.popleft()
        if steps_left % 2 == 0:
            possible.add((r, c))
        if steps_left == 0:
            continue

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_r = r + dr
            new_c = c + dc
            if 0 <= new_r < len(matrix) and 0 <= new_c < len(matrix[0]) and matrix[new_r][new_c] != "#" and (new_r, new_c) not in visited:
                queue.append((new_r, new_c, steps_left - 1))
                visited.add((new_r, new_c))
    return len(possible)


# Read input
with open("day21.txt", "r") as f:
    lines = f.read().splitlines()
    print(reachable_garden_plots(lines))
