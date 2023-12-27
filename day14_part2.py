def spin_cycle(matrix):
    for i in range(4):
        matrix = ["".join(column) for column in zip(*matrix)]
        matrix = ["#".join(["".join(sorted(tuple(group), reverse=True))
                           for group in row.split("#")]) for row in matrix]
        matrix = [row[::-1]for row in matrix]

    return matrix


def total_load_v2(input):
    matrix = [line for line in input]
    # we will always solve to the left so we will rotate matrix 90 degrees to the left(counter-clockwise)
    # after that in each cycle we will rotate it 90 degrees to the right(clockwise)
    # matrix = rotate_matrix_counter_clockwise(matrix)

    upper_limit = 1000000000
    counter = 0
    visited = {tuple(matrix): counter}
    matrices = [matrix]
    while upper_limit > counter:
        counter += 1
        matrix = spin_cycle(matrix)
        key = tuple(matrix)
        if key in visited:
            break
        else:
            visited[key] = counter
            matrices.append(matrix)
    last = (upper_limit - counter) % (counter - visited[key]) + visited[key]
    return sum(row.count("O") * (len(matrix)-i) for i, row in enumerate(list(matrices[last])))


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
ans1 = 64
assert total_load_v2(test1.splitlines()) == ans1

# Read input
with open("day14.txt") as f:
    input = f.read().splitlines()
    print(total_load_v2(input))
