def is_accepted(item, work, work_name="in"):
    if work_name == "R":
        return False
    if work_name == "A":
        return True
    rules, default = work[work_name]
    for key, comparator, value, next in rules:
        if comparator == "<":
            if item[key] < value:
                return is_accepted(item, work, next)
        elif comparator == ">":
            if item[key] > value:
                return is_accepted(item, work, next)

    return is_accepted(item, work, default)


def sum_rating_numbers(input):
    rules_block, query = input.split("\n\n")
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
    total = 0
    for line in query.splitlines():
        item = dict()
        for vals in line[1:-1].split(","):
            var, val = vals.split("=")
            item[var] = int(val)
        if is_accepted(item, work, "in"):
            total += sum(item.values())
    return total


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
ans1 = 19114
assert sum_rating_numbers(test1) == ans1

# Read input
with open("day19.txt", "r") as f:
    input = f.read()
    print(sum_rating_numbers(input))
