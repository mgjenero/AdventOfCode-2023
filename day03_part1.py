def sum_valid_numbers(lines: list[str]) -> int:
    lines = [line.strip() for line in lines]
    matrix = [[c for c in line] for line in lines]
    ROWS = len(matrix)
    COLS = len(matrix[0])
    total = 0
    for i in range(ROWS):
        prev = 0
        candidates = set()
        for j in range(COLS):
            if matrix[i][j].isdigit():
                prev = prev * 10 + int(matrix[i][j])
                candidates.add((i + 1, j + 1))
                candidates.add((i + 1, j - 1))
                candidates.add((i - 1, j + 1))
                candidates.add((i - 1, j - 1))
                candidates.add((i, j + 1))
                candidates.add((i, j - 1))
                candidates.add((i + 1, j))
                candidates.add((i - 1, j))
            else:
                if is_valid(candidates, matrix):
                    total += prev
                prev = 0
                candidates = set()
        if is_valid(candidates, matrix):
            total += prev
    return total


def is_valid(candidates: set, matrix: list[list[str]]) -> bool:
    for i, j in candidates:
        if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
            continue
        elif not matrix[i][j].isdigit() and matrix[i][j] != ".":
            return True
    return False

# Testing


test1 = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598.."
]
ans1 = 4361

assert (sum_valid_numbers(test1) == ans1)

# Read input
with open("day3.txt", "r") as f:
    lines = f.readlines()
    print(sum_valid_numbers(lines))


# Runtime = O(n*m)
# Space O(n*m) - could be O(1) if we do not parse the input into a matrix
# but working with matrix makes enhances readability
#
# where n is the number of rows
# where m is the number of columns/(characters in each row)

# ALTERNATIVES:
# - lines and matrix are roughly the same size, so we could just replace the matrix with lines to save memory
# - adapt algorithm to work with lines instead of matrix(not so easy to read but pretty much same syntax)
