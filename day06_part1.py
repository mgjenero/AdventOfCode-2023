def parse_lines(lines):
    times = list(map(int, lines[0].split(":")[1].split()))
    records = list(map(int, lines[1].split(":")[1].split()))
    return times, records


def calculate_possible_ways(input):
    times, records = parse_lines(input)
    ans = 1

    for time, record in zip(times, records):
        total = 0
        for speed in range(time):
            reamaining_time = time - speed
            distance = speed * reamaining_time
            if distance > record:
                total += 1
            elif total > 0:
                # once distance start decreasing and is less than record, we can stop
                break
        ans *= total
    return ans


# Testing
test1 = ["Time:      7  15   30",
         "Distance:  9  40  200"]
ans1 = 288

assert calculate_possible_ways(test1) == ans1

# Read input
with open('day6.txt') as f:
    lines = f.readlines()
    print(calculate_possible_ways(lines))

# Runtime  = O(n*m)
# Space  = O(m)
# where n is time
# where m is number of elements(time and record pairs) needed to process
