def is_next_to_gear(candidates, matrix):
    gears = []
    for i, j in candidates:
        if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
            continue
        if matrix[i][j] == '*':
            gears.append((i, j))
    return gears


def sum_gear_ratios(gears):
    total = 0
    for gear, nums in gears.items():
        if len(nums) == 2:
            total += nums[0] * nums[1]
    return total


def add_numbers_to_gears(lines):
    lines = [line.strip() for line in lines]
    matrix = [[c for c in line] for line in lines]
    ROWS = len(matrix)
    COLS = len(matrix[0])
    gears = dict()
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
                available_gears = is_next_to_gear(candidates, matrix)
                if len(available_gears) != 0:
                    for gear in available_gears:
                        if gear in gears:
                            gears[gear].append(prev)
                        else:
                            gears[gear] = [prev]
                prev = 0
                candidates = set()
        if is_next_to_gear(candidates, matrix):
            available_gears = is_next_to_gear(candidates, matrix)
            if len(available_gears) != 0:
                for gear in available_gears:
                    if gear in gears:
                        gears[gear].append(prev)
                    else:
                        gears[gear] = [prev]

    return sum_gear_ratios(gears)


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
ans1 = 467835
assert (add_numbers_to_gears(test1) == ans1)

# Read input
with open("day3.txt", "r") as f:
    lines = f.readlines()
    print(add_numbers_to_gears(lines))

# Runtime = O(n*m)
# Space O(n*m) - could be O(1) if we do not parse the input into a matrix
# but working with matrix makes enhances readability
#
# where n is the number of rows
# where m is the number of columns/(characters in each row)
