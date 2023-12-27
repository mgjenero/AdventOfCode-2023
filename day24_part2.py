from sympy import symbols, solve


def find_rock_start(lines):
    hailstones = []
    for line in lines:
        line = line.replace(" @ ", ",  ").strip()
        x, y, z, vx, vy, vz = line.split(", ")
        hailstones.append([int(x), int(y), int(z), int(vx), int(vy), int(vz)])
    # we need to find:
    # x + vx * t = x_rock + vx_rock * t
    # y + vy * t = y_rock + vy_rock * t
    # z + vz * t = z_rock + vz_rock * t
    # we can transform this to:
    # x - x_rock = (vx_rock - vx) * t
    # (x - x_rock) / (vx_rock - vx) = t

    # (x - x_rock) / (vx_rock - vx) = (y - y_rock) / (vy_rock - vy)
    # and for z axis accordingly

    # so we have 6 unknowns and need 6 lienarly independent equations
    # e.g. loooking for matrix rank 6
    # Here we use math solver to find the answer
    equations = []
    x_rock, y_rock, z_rock, vx_rock, vy_rock, vz_rock = symbols(
        "x_rock y_rock z_rock vx_rock vy_rock vz_rock")

    for i, hailstone in enumerate(hailstones):
        x, y, z, vx, vy, vz = hailstone
        # use multiplication instead of division to avoid errors
        equations.append((x-x_rock)*(vy_rock-vy) - (y-y_rock)*(vx_rock-vx))
        equations.append((y-y_rock)*(vz_rock-vz) - (z-z_rock)*(vy_rock-vy))
        if i >= 2:
            answer = solve(equations)
            if len(answer) == 1:
                break
    answer = answer[0]
    # return sum of starting coodinates of the rock
    return answer[x_rock] + answer[y_rock] + answer[z_rock]


# Testing
test1 = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""
ans1 = 47
assert find_rock_start(test1.splitlines()) == ans1

# Read input
with open("day24.txt") as f:
    input = f.read().splitlines()
    print(find_rock_start(input))
