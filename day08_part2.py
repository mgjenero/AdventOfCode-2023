from math import lcm


def calculate_path_2(input):
    path, maps = input.split("\n\n")

    map_dict = dict()
    for line in maps.splitlines():
        key, value = line.split(" = ")
        # remove parenthesis
        value = value[1:-1].split(", ")
        map_dict[key] = (value[0], value[1])

    ends = []
    for node in map_dict.keys():
        # find start nodes
        if node[-1] == "A":
            # for each of them find part to end
            # IMPORTANT: this is not most general solution since there may be
            # multiple ends available for each start but here thats not the case
            # even though it is not stated in the problem
            curr = node
            total = 0
            while curr[-1] != "Z":
                for p in path:
                    curr = map_dict[curr][0] if p == "L" else map_dict[curr][1]
                    total += 1
            ends.append(total)
    return lcm(*ends)


# Testing

test1 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""
ans1 = 6

assert calculate_path_2(test1) == ans1

# Read input
with open("day8.txt", "r") as f:
    lines = f.read()
    print(calculate_path_2(lines))
