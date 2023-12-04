import math


def parse_lines(lines):
    time = int("".join(lines[0].split(":")[1].split()))
    record = int("".join(lines[1].split(":")[1].split()))
    return time, record


def calculate_possible_ways(input):
    time, record = parse_lines(input)
    ans = 0
    # find left boundary, right one is symetric
    # cause when speed is increased by one, distance is decreased by one
    l = 0
    r = time
    while l < r:
        mid = (l + r) // 2
        if mid * (time - mid) > record:
            r = mid
        else:
            l = mid + 1
    # number of possible combinations is time + 1, not time
    # example: time = 3, combinations(holding_button, racing) = (0,3),(1,2),(2,1),(3,0)
    ans = (time + 1) - (2 * l)
    return ans


def calculate_possible_ways_formula(input):
    time, record = parse_lines(input)
    # Solve formula for distance > record
    # where distance = speed * (time - speed) = time * speed - speed^2
    # solve speed^2 - time * speed + record < 0
    numerator1 = time - math.sqrt((-1 * time) ** 2 - 4 * record)
    numerator2 = time + math.sqrt((-1 * time) ** 2 - 4 * record)
    denominator = 2

    l = math.floor(min(numerator1/denominator, numerator2/denominator))
    r = math.floor(max(numerator1/denominator, numerator2/denominator))
    return r-l


# Testing
test1 = ["Time:      7  15   30",
         "Distance:  9  40  200"]
ans1 = 71503

assert calculate_possible_ways(test1) == ans1
assert calculate_possible_ways_formula(test1) == ans1

with open('day6.txt') as f:
    lines = f.readlines()
    print(calculate_possible_ways(lines))
    print(calculate_possible_ways_formula(lines))


# binary_search solution
# Runtime  = O(log(n))
# Space  = O(1)

# quadratic formula solution
# Runtime  = O(1)
# Space  = O(1)
# where n is time
