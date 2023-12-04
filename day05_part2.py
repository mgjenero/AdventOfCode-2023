def parse_input(whole_input):
    lines = whole_input.split("\n\n")
    seeds, mappings = lines[0], lines[1:]
    seeds = list(map(int, lines[0].split(":")[1].split()))
    # seeds will be converted as tuples representing intervals
    temp = []
    for i in range(0, len(seeds), 2):
        temp.append((seeds[i], seeds[i] + seeds[i+1]))
    seeds = temp
    maps = []
    for one_map in mappings:
        mapping = []
        for line in one_map.splitlines()[1:]:
            mapping.append(list(map(int, line.split())))
        maps.append(mapping)
    return seeds, maps


def update_intervals(intervals, mapping):
    new_intervals = []

    while intervals:
        start, end = intervals.pop()
        found_overlap = False
        for dest_start, source_start, length in mapping:
            new_start = max(start, source_start)
            new_end = min(end, source_start + length)
            if new_start < new_end:
                # overlapping interval stored in new_intervals after mapping
                # non-overlapping intervals(if they exist) will be stored in intervals
                new_intervals.append(
                    (new_start + (dest_start - source_start), new_end + (dest_start - source_start)))
                found_overlap = True
                if new_end < end:
                    intervals.append((new_end, end))
                if start < new_start:
                    intervals.append((start, new_start))
                # break the loop to update current interval with some not mapped interval
                break
        # if no overlapping interval found, just append the current interval
        if not found_overlap:
            new_intervals.append((start, end))
    intervals = merge_intervals(new_intervals)
    return intervals


def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    curr = intervals[0]
    for start, end in intervals[1:]:
        if start <= curr[1]:
            curr = (curr[0], max(curr[1], end))
        else:
            merged.append(curr)
            curr = (start, end)
    merged.append(curr)
    return merged


def find_lowest_location_number(whole_input):
    seeds, mappings = parse_input(whole_input)
    intervals = seeds
    for mapping in mappings:
        intervals = update_intervals(intervals, mapping)
    # intervals are already sorted when merging is done
    return intervals[0][0]

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
ans1 = 46

assert find_lowest_location_number(test1) == ans1


# Read input
with open("day5.txt", "r") as f:
    lines = f.read()
    print(find_lowest_location_number(lines))
