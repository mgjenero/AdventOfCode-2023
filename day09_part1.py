def sum_extrapolated_right(lines):
    total = 0
    for line in lines:
        nums = list(map(int, line.split()))
        diffs = [nums]
        while not all([x == 0 for x in diffs[-1]]):
            curr = []
            for i in range(len(diffs[-1]) - 1):
                curr.append(diffs[-1][i + 1] - diffs[-1][i])
            diffs.append(curr)
        last = 0
        # skip last line cause it's all 0s, go up to 0th line
        for i in range(len(diffs) - 2, -1, -1):
            last = diffs[i][-1] + last
        total += last
    return total


# Testing
test1 = ["0 3 6 9 12 15",
         "1 3 6 10 15 21",
         "10 13 16 21 30 45"]
ans1 = 114

assert sum_extrapolated_right(test1) == ans1

# Read input
with open("day9.txt", "r") as f:
    lines = f.readlines()
    print(sum_extrapolated_right(lines))
