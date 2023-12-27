from collections import deque


def find_start(lines):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "S":
                return (i, j)
    return (-1, -1)


def count_enclosed_tiles(lines):
    start = find_start(lines)
    matrix = []
    for line in lines:
        matrix.append([char for char in line])
    # use bfs to find cycle
    visited = set()
    queue = deque([start])

    possible_s = {"|", "F", "7", "-", "J", "L"}
    while queue:
        curr = queue.popleft()
        r, c = curr
        if curr in visited:
            continue
        else:
            visited.add(curr)
        # check 4 neighbors
        # for each neighbor, check if neighbor is valid and can go to current position,
        # then check if current position can go to neighbor
        # if both are true, add neighbor to queue
        # Since there is only one valid path, every position will be stored in visited
        if r-1 >= 0 and matrix[r-1][c] in "F7|" and (r-1, c) not in visited:
            if matrix[r][c] in "|LJS":
                queue.append((r-1, c))
            if matrix[r][c] == "S":
                possible_s = possible_s.intersection({"|", "J", "L"})
        if r+1 <= len(matrix) - 1 and matrix[r+1][c] in "LJ|" and (r+1, c) not in visited:
            if matrix[r][c] in "|F7S":
                queue.append((r+1, c))
            if matrix[r][c] == "S":
                possible_s = possible_s.intersection({"|", "F", "7"})
        if c-1 >= 0 and matrix[r][c-1] in "FL-" and (r, c-1) not in visited:
            if matrix[r][c] in "-7JS":
                queue.append((r, c-1))
            if matrix[r][c] == "S":
                possible_s = possible_s.intersection({"-", "7", "J"})
        if c+1 <= len(matrix[0]) - 1 and matrix[r][c+1] in "J7-" and (r, c+1) not in visited:
            if matrix[r][c] in "-LFS":
                queue.append((r, c+1))
            if matrix[r][c] == "S":
                possible_s = possible_s.intersection({"-", "F", "L"})

    matrix[start[0]][start[1]] = possible_s.pop()

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (i, j) not in visited:
                matrix[i][j] = "."

    # left/right sweep
    # ray casting algorithm / point in polygon
    # odd number of edge crossings = inside, even = outside
    # count only one edge when iterating "on edge" where wall keeps its direction after horizontal lines like up->right->up, e.g. use "|LJ"
    # count both edges wehn iterating "on edge" where wall changes its direction after horizontal lines like up->right->down

    count = 0
    for r in range(len(matrix)):
        crossing = 0
        for c in range(len(matrix[r])):
            if matrix[r][c] in "|JL":
                crossing += 1
            elif matrix[r][c] == "." and crossing % 2 == 1:
                count += 1
    return count


# Testing
test1 = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""
ans1 = 1
assert count_enclosed_tiles(test1.splitlines()) == ans1

# Read input
with open("day10.txt", "r") as file:
    data = file.read().splitlines()
    print(count_enclosed_tiles(data))
