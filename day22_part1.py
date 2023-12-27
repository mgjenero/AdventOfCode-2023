def rectangle_overlap(rect1, rect2):
    """
    Check if two rectangles overlap on x and y axis.
    Ranges are inclusive so <= is used.
    """
    # rect1 = [x1, y1, z1, x2, y2, z2]
    return max(rect1[0], rect2[0]) <= min(rect1[3], rect2[3]) and max(rect1[1], rect2[1]) <= min(rect1[4], rect2[4])


def disintegrated_bricks(lines):
    bricks = []
    for line in lines:
        line = line.replace("~", ",")
        bricks.append([int(x) for x in line.split(",")])
    # sort by lower z of each brick
    bricks.sort(key=lambda x: x[2])

    # adjust z for falling bricks; lowest possible z is 1
    for index, brick in enumerate(bricks):
        new_z = 1
        for before_brick in bricks[:index]:
            if rectangle_overlap(brick, before_brick):
                new_z = max(new_z, before_brick[5] + 1)
        brick[5] = new_z + (brick[5] - brick[2])
        brick[2] = new_z
    # sort to get new order(bricks can have move out of position)
    # cause not all of them overlap
    bricks.sort(key=lambda x: x[2])

    brick_supports = {i: set() for i in range(len(bricks))}
    brick_suported_by = {i: set() for i in range(len(bricks))}
    for i in range(len(bricks)-1):
        brick_down = bricks[i]
        for j in range(i+1, len(bricks)):
            brick_up = bricks[j]
            if brick_up[2] == brick_down[5] + 1 and rectangle_overlap(brick_up, brick_down):
                brick_supports[i].add(j)
                brick_suported_by[j].add(i)

    total = 0
    # number of bricks that can be removed without collapsing
    # every brick can only be removed as standalone brick
    # for each brick check if supported bricks are supported by more than 1 brick
    for i in range(len(bricks)):
        stable_support = True
        for j in brick_supports[i]:
            if len(brick_suported_by[j]) < 2:
                stable_support = False
                break
        if stable_support:
            total += 1
    return total


# Testing
test1 = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9"""
ans1 = 5
assert disintegrated_bricks(test1.splitlines()) == ans1

# Read input
with open("day22.txt") as f:
    input = f.read().splitlines()
    print(disintegrated_bricks(input))
