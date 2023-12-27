def calculate_total_galaxy_distance(input):
    # find empty rows and columns
    empty_rows = [i for i in range(len(input)) if "#" not in input[i]]
    input_transposed = list(zip(*input))
    empty_cols = [i for i in range(
        len(input_transposed)) if "#" not in input_transposed[i]]

    galaxies = [(r, c) for r in range(len(input))
                for c in range(len(input[r])) if input[r][c] == "#"]
    total_distance = 0
    for i, (r, c) in enumerate(galaxies[:-1]):
        for r2, c2 in galaxies[i+1:]:

            # distance between two points is abs(r2-r) + abs(c2-c) + any expansion for empty rows and columns
            for i in range(min(r, r2), max(r, r2)):
                if i in empty_rows:
                    total_distance += 2
                else:
                    total_distance += 1
            for i in range(min(c, c2), max(c, c2)):
                if i in empty_cols:
                    total_distance += 2
                else:
                    total_distance += 1

    return total_distance


# Testing
test1 = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""
ans1 = 374

assert calculate_total_galaxy_distance(test1.splitlines()) == ans1

# Read input
with open("day11.txt") as f:
    lines = f.read().splitlines()
    print(calculate_total_galaxy_distance(lines))
