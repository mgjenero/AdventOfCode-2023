def total_load(input):
    matrix = [[char for char in line] for line in input]
    matrix = list(list(l) for l in zip(*matrix))
    for r in range(len(matrix)):
        prev = 0
        count = 0
        for c in range(len(matrix[0])):
            if matrix[r][c] == "O":
                matrix[r][c] = "."
                count += 1
            elif matrix[r][c] == "#":
                matrix[r][prev:prev+count] = ["O"]*count
                count = 0
                prev = c+1
        if count > 0:
            matrix[r][prev:prev+count] = ["O"]*count
    points = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == "O":
                points += len(matrix[0])-c

    return points


# Testing
test1 = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""
ans1 = 136
assert total_load(test1.splitlines()) == ans1

# Read input
with open("day14.txt") as f:
    input = f.read().splitlines()
    print(total_load(input))
