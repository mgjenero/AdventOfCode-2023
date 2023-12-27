from collections import deque


def find_start(lines):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "S":
                return (i, j)
    return (-1, -1)


def find_farthest_distance(lines):
    start = find_start(lines)
    matrix = []
    for line in lines:
        matrix.append([char for char in line])
    # use bfs to find cycle
    visited = set()
    queue = deque([start])
    while queue:
        r, c = queue.popleft()
        if (r, c) in visited:
            continue
        else:
            visited.add((r, c))
        # check 4 neighbors
        # for each neighbor, check if neighbor is valid and can go to current position,
        # then check if current position can go to neighbor
        # if both are true, add neighbor to queue
        # Since there is only one valid path, every position will be stored in visited
        if r-1 >= 0 and matrix[r-1][c] in "F7|" and (r-1, c) not in visited:
            if matrix[r][c] in "|LJS":
                queue.append((r-1, c))
        if r+1 <= len(matrix) - 1 and matrix[r+1][c] in "LJ|" and (r+1, c) not in visited:
            if matrix[r][c] in "|F7S":
                queue.append((r+1, c))
        if c-1 >= 0 and matrix[r][c-1] in "FL-" and (r, c-1) not in visited:
            if matrix[r][c] in "-7JS":
                queue.append((r, c-1))
        if c+1 <= len(matrix[0]) - 1 and matrix[r][c+1] in "J7-" and (r, c+1) not in visited:
            if matrix[r][c] in "-LFS":
                queue.append((r, c+1))

    return len(visited)//2


# Testing
test1 = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""
ans1 = 4
assert find_farthest_distance(test1.splitlines()) == ans1

# Read input
with open("day10.txt", "r") as file:
    data = file.read().splitlines()
    print(find_farthest_distance(data))
