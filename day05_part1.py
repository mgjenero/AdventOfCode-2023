def parse_input(whole_input):
    lines = whole_input.split("\n\n")
    seeds, mappings = lines[0], lines[1:]
    seeds = list(map(int, lines[0].split(":")[1].split()))
    maps = []
    for one_map in mappings:
        mapping = []
        for line in one_map.splitlines()[1:]:
            mapping.append(list(map(int, line.split())))
        maps.append(mapping)
    return seeds, maps


def mapping_conversion(value, mapping):
    for dest_start, source_start, length in mapping:
        if value >= source_start and value < source_start + length:
            return dest_start + (value - source_start)
    return value


def find_lowest_location_number(whole_input):
    seeds, mappings = parse_input(whole_input)
    lowest_location = None
    for seed in seeds:
        val = seed
        for mapping in mappings:
            val = mapping_conversion(val, mapping)
        if lowest_location is None or val < lowest_location:
            lowest_location = val
    return lowest_location


# Testing
test1 = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
ans1 = 35

assert find_lowest_location_number(test1) == ans1


# Read input
with open("day5.txt", "r") as f:
    lines = f.read()
    print(find_lowest_location_number(lines))
