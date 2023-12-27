from collections import deque
# This solution in not general solution for this type of problem
# but in this case input is designed so the whole problem can be divided in just multiple grid searches
# those grid searches are:
# - full odd grid
# - full even grid
# - corners (4)
# - partial grid fills (like corners, there are multiple cases of this)
# triangles are grid searches starting at one edge but
# not having enough steps to check whole grid


def find_start(lines):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "S":
                return (i, j)
    return (-1, -1)


def reachable_garden_plots_infinite(lines):
    r_start, c_start = find_start(lines)
    matrix = []
    for line in lines:
        matrix.append([char for char in line])
    initial_steps = 26501365

    # check algorithm conditions
    # sqare grid
    assert len(matrix) == len(matrix[0])
    # start in the middle
    assert r_start == c_start == len(matrix) // 2
    # left, right, up and down goes all the way to the edge of last grid
    assert initial_steps % len(matrix) == len(matrix)//2

    def solve_for_matrix(r_start, c_start, steps):
        queue = deque([(r_start, c_start, steps)])
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

    grid_size = len(matrix)
    # number of additional grids to the side of original one
    # -1 is cause last grid is not fully searched
    grids_to_the_side = initial_steps//grid_size - 1
    # number of each grid search
    odd_grids_num = ((grids_to_the_side // 2) * 2 + 1) ** 2
    even_grids_num = (((grids_to_the_side + 1) // 2) * 2) ** 2

    total = 0

    total += odd_grids_num * \
        solve_for_matrix(r_start, c_start, 2 * grid_size + 1)
    total += even_grids_num * solve_for_matrix(r_start, c_start, 2 * grid_size)
    # add corners(top, bottom, left, right)
    top_corner = solve_for_matrix(grid_size-1, c_start, grid_size - 1)
    bottom_corner = solve_for_matrix(0, c_start, grid_size - 1)
    left_corner = solve_for_matrix(r_start, 0, grid_size - 1)
    right_corner = solve_for_matrix(r_start, grid_size-1, grid_size - 1)
    total += top_corner + bottom_corner + left_corner + right_corner
    # add partials
    small_partial_num = grids_to_the_side + 1
    top_right_small = solve_for_matrix(grid_size-1, 0, grid_size // 2 - 1)
    bottom_right_small = solve_for_matrix(0, 0, grid_size // 2 - 1)
    bottom_left_small = solve_for_matrix(0, grid_size-1, grid_size // 2 - 1)
    top_left_small = solve_for_matrix(
        grid_size-1, grid_size-1, grid_size // 2 - 1)
    total += small_partial_num * \
        (top_right_small + bottom_right_small + bottom_left_small + top_left_small)

    big_partial_num = grids_to_the_side
    top_right_big = solve_for_matrix(
        grid_size-1, 0, grid_size * 3 // 2 - 1)  # 2s -1 - 0.5s
    bottom_right_big = solve_for_matrix(0, 0, grid_size * 3 // 2 - 1)
    bottom_left_big = solve_for_matrix(0, grid_size-1, grid_size * 3 // 2 - 1)
    top_left_big = solve_for_matrix(
        grid_size-1, grid_size-1, grid_size * 3 // 2 - 1)
    total += big_partial_num * \
        (top_right_big + bottom_right_big + bottom_left_big + top_left_big)

    return total


# Read input
with open("day21.txt", "r") as f:
    lines = f.read().splitlines()
    print(reachable_garden_plots_infinite(lines))
