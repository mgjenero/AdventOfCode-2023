def polygon_area(vertices):
    # shoelace formula
    ret = 0
    for i in range(len(vertices)):
        ret += ((vertices[i][0] * (vertices[i - 1][1] -
                vertices[(i + 1) % len(vertices)][1])))
    return abs(ret) // 2


def total_volume_v2(lines):
    vertices = []
    edge_count = 0
    curr = (0, 0)
    vertices.append(curr)
    num_to_direction = {0: "R", 1: "D", 2: "L", 3: "U"}
    for line in lines:
        _, _, color = line.split()
        color = color[2:-1]
        num = int(color[:5], 16)
        direction = num_to_direction[int(color[-1])]
        edge_count += num
        if direction == "R":
            curr = curr[0], curr[1] + num
            vertices.append(curr)
        if direction == "L":
            curr = curr[0], curr[1] - num
            vertices.append(curr)
        if direction == "D":
            curr = curr[0] + num, curr[1]
            vertices.append(curr)
        if direction == "U":
            curr = curr[0] - num, curr[1]
            vertices.append(curr)
    area = polygon_area(vertices)
    # apply pick's theorem
    # A = i + (b / 2) - 1
    # where A is area, i are interior points, b are boundary points
    i = area - (edge_count//2) + 1
    total = i + edge_count
    return total


# Testing
test1 = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""
ans1 = 952408144115
assert total_volume_v2(test1.splitlines()) == ans1

# Read input
with open("day18.txt", "r") as f:
    lines = f.read().splitlines()
    print(total_volume_v2(lines))
