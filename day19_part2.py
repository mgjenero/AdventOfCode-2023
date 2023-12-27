import math


def count_disctinct(intervals, work, work_name="in"):
    if work_name == "R":
        return 0
    if work_name == "A":
        return math.prod([(M-m+1) for m, M in intervals.values()])

    rules, default = work[work_name]
    total = 0
    use_default = True
    for key, comparator, value, next in rules:
        low, high = intervals[key]
        if comparator == "<":
            passed = (low, value-1)
            failed = (value, high)
        elif comparator == ">":
            passed = (value+1, high)
            failed = (low, value)
        if passed[0] <= passed[1]:
            # passed intervals are send to next workflow
            new_intervals = dict(intervals)
            new_intervals[key] = passed
            total += count_disctinct(new_intervals, work, next)
        if failed[0] <= failed[1]:
            # failed intervals are send to next rule in current workflow
            intervals = dict(intervals)
            intervals[key] = failed
        else:
            # if false is empty, whole interval passed
            use_default = False
            break
    # else:
    if use_default:
        # if for loop is not broken(meaning we have failed intervals not matching any rule)
        # we send them to default workflow
        total += count_disctinct(intervals, work, default)
    return total


def sum_rating_numbers_v2(input):
    rules_block = input.split("\n\n")[0]
    work = dict()
    for line in rules_block.splitlines():
        name, rules = line[:-1].split("{")
        rules = rules.split(",")
        work[name] = ([], rules.pop())
        for rule in rules:
            comparison, next = rule.split(":")
            key = comparison[0]
            comparator = comparison[1]
            value = int(comparison[2:])
            work[name][0].append((key, comparator, value, next))

    values = dict()
    for char in "xmas":
        values[char] = (1, 4000)
    return count_disctinct(values, work, "in")


# Testing
test1 = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""
ans1 = 167409079868000
assert sum_rating_numbers_v2(test1) == ans1

# Read input
with open("day19.txt", "r") as f:
    input = f.read()
    print(sum_rating_numbers_v2(input))
