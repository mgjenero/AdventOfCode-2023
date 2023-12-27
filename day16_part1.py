from collections import deque


def energized_tiles(input):
    matrix = [list(line) for line in input]

    queue = deque([(0, 0, 0, 1)])
    seen = set()
    while queue:
        curr = queue.popleft()
        r, c, dr, dc = curr
        if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]):
            continue
        if curr not in seen:
            seen.add(curr)
        else:
            continue
        if matrix[r][c] in ".":
            queue.append((r+dr, c+dc, dr, dc))
        if matrix[r][c] == "-":
            if dc:
                queue.append((r, c+dc, dr, dc))
            if dr:
                queue.append((r, c+1, 0, 1))
                queue.append((r, c-1, 0, -1))
        if matrix[r][c] == "|":
            if dc:
                queue.append((r+1, c, 1, 0))
                queue.append((r-1, c, -1, 0))
            if dr:
                queue.append((r+dr, c, dr, dc))
        if matrix[r][c] == "\\":
            queue.append((r+dc, c+dr, dc, dr))
        if matrix[r][c] == "/":
            queue.append((r-dc, c-dr, -dc, -dr))
    return len({(r, c) for r, c, _, _ in seen})


# Testing ('\' is represented as '\\')
test1 = """.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|...."""
ans1 = 46
assert energized_tiles(test1.splitlines()) == ans1

# Read input
with open("day16.txt") as f:
    input = f.read().splitlines()
    print(energized_tiles(input))
