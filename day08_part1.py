def calculate_path(input):
    path, maps = input.split("\n\n")

    map_dict = dict()
    for line in maps.splitlines():
        key, value = line.split(" = ")
        # remove parenthesis
        value = value[1:-1].split(", ")
        map_dict[key] = (value[0], value[1])

    curr = "AAA"
    total = 0
    while curr != "ZZZ":
        for p in path:
            curr = map_dict[curr][0] if p == "L" else map_dict[curr][1]
            total += 1
    return total

# Testing

test1="""RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""
ans1 = 2
assert calculate_path(test1) == ans1

# Read input
with open("day8.txt", "r") as f:
    lines = f.read()
    print(calculate_path(lines))



