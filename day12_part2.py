from functools import cache


@cache
def count_possible_solutions(line, nums):
    if not line:
        # if line and nums are both empty, we have a solution
        # else we don't (it's not valid one)
        return 1 if not nums else 0
    if not nums:
        # if we used all numbers but line has more "#",
        # we don't have a valid solution, else we have
        return 0 if "#" in line else 1
    result = 0
    if line[0] in "#?":
        # if line[0] is "#" or "?", we can look at it as "#"
        if nums[0] <= len(line) and "." not in line[:nums[0]]:
            # line[nums[0]] contains only "#" and "?" so we can use first num here
            if nums[0] == len(line):
                # end of the line so we do not need "." for spacing
                result += count_possible_solutions(line[nums[0]:], nums[1:])
            elif line[nums[0]] != "#":
                # we need "." for spacing so at that place we need "." or "?"
                result += count_possible_solutions(
                    line[nums[0] + 1:], nums[1:])

    if line[0] in ".?":
        # if line[0] is "." or "?", we can look at it as "."
        # we cannot use any num here, so we just skip it
        result += count_possible_solutions(line[1:], nums)
    return result


def solver_v2(lines):
    result = 0
    for line in lines:
        characters, nums = line.split(" ")
        new_characters = characters
        for i in range(4):
            new_characters += "?"
            new_characters += characters
        nums = tuple(map(int, nums.split(",")))
        new_nums = nums * 5
        result += count_possible_solutions(new_characters, new_nums)
    return result


# Testing
test1 = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""
ans1 = 525152
assert solver_v2(test1.splitlines()) == ans1

# Read input
with open("day12.txt") as f:
    lines = f.read().splitlines()
    print(solver_v2(lines))
