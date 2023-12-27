from heapq import heappush, heappop


def min_heat_loss_v2(input):
    matrix = [[int(i)for i in line] for line in input]
    # (heat_count, r, c, dr, dc, direction_count)
    priority_queue = [(0, 0, 0, 0, 0, 0)]
    visited = set()

    while priority_queue:
        heat_count, r, c, dr, dc, direction_count = heappop(priority_queue)
        if r == len(matrix) - 1 and c == len(matrix[0]) - 1 and direction_count >= 4:
            return heat_count
        if (r, c, dr, dc, direction_count) not in visited:
            visited.add((r, c, dr, dc, direction_count))
        else:
            continue
        if direction_count < 10 and (dr or dc):
            new_r = r + dr
            new_c = c + dc
            if 0 <= new_r < len(matrix) and 0 <= new_c < len(matrix[0]):
                heappush(priority_queue, (heat_count +
                         matrix[new_r][new_c], new_r, new_c, dr, dc, direction_count + 1))
        if direction_count >= 4 or (dr == 0 and dc == 0):
            for direction_r, direction_c in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                # forward is already handled,so we skip it and we cannot go backwards
                # only possible ways are left and right
                if (direction_r, direction_c) != (dr, dc) and (direction_r, direction_c) != (-dr, -dc):
                    new_r = r + direction_r
                    new_c = c + direction_c
                    if 0 <= new_r < len(matrix) and 0 <= new_c < len(matrix[0]):
                        heappush(priority_queue, (heat_count +
                                 matrix[new_r][new_c], new_r, new_c, direction_r, direction_c, 1))
    return -1


# Testing
test1 = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""
ans1 = 94
assert min_heat_loss_v2(test1.splitlines()) == ans1

# Read input
with open("day17.txt") as f:
    input = f.read().splitlines()
    print(min_heat_loss_v2(input))
