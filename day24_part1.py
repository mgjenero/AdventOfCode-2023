def total_hailstone_intersections(lines):
    hailstones = []
    for line in lines:
        line = line.replace(" @ ", ",  ").strip()
        x, y, _, vx, vy, _ = line.split(", ")
        hailstones.append([int(x), int(y), int(vx), int(vy)])
    total = 0
    for i in range(len(hailstones) - 1):
        # equations will be transformed to y = ax + b
        hailstone1 = hailstones[i]
        x1, y1, vx1, vy1 = hailstone1
        a1 = vy1/vx1
        b1 = y1 - vy1/vx1 * x1
        for j in range(i+1, len(hailstones)):
            hailstone2 = hailstones[j]
            x2, y2, vx2, vy2 = hailstone2
            a2 = vy2/vx2
            b2 = y2 - vy2/vx2 * x2
            # check if intersection exist or are they parallel
            if a1 != a2:
                # they have intersection
                # a1x + b1 = a2x + b2
                # x(a1 - a2) = b2 - b1
                # x = (b2 - b1) / (a1 - a2)
                intersection_x = (b2 - b1) / (a1 - a2)
                intersection_y = a1 * intersection_x + b1
                # find time when each hailstone reaches intersection
                # x1 + vx1 * t = intersection_x
                # t = (intersection_x - x1) / vx1
                # we only need to chcek for x or y of every hailstone
                time1 = (intersection_x - x1) / vx1
                time2 = (intersection_x - x2) / vx2
                if time1 >= 0 and time2 >= 0:
                    if 200000000000000 <= intersection_x <= 400000000000000 and 200000000000000 <= intersection_y <= 400000000000000:
                        total += 1
    return total


# Read input
with open("day24.txt") as f:
    input = f.read().splitlines()
    print(total_hailstone_intersections(input))
