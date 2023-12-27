def block_vertical(block):
    for l in range(len(block[0])-1):
        r = l + 1
        length = min(l+1, len(block[0])-(l+1))
        miss = 0
        for row in block:
            lr = row[l+1-length:l+1]
            lr.reverse()
            rr = row[r:r+length]
            diff = sum([1 if lr[i] != rr[i] else 0 for i in range(len(lr))])
            if diff > 0:
                miss += diff
                if miss > 1:
                    break
        if miss == 1:
            return l+1
    return 0


def block_horizontal(block):
    for l in range(len(block)-1):
        org_l = l
        r = l + 1
        miss = 0
        while l >= 0 and r < len(block):
            diff = sum([1 if block[l][i] != block[r][i]
                       else 0 for i in range(len(block[l]))])
            if diff > 0:
                miss += diff
                if miss > 1:
                    break
            l -= 1
            r += 1
        if miss == 1:
            return (org_l+1) * 100
    return 0


def summarize_notes_v2(input):
    blocks = input.split("\n\n")
    horizontal = 0
    vertical = 0
    for block in blocks:
        block = [[l for l in line] for line in block.splitlines()]
        vertical += block_vertical(block)
        horizontal += block_horizontal(block)
    return vertical + horizontal


# Testing
test1 = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""
ans1 = 400
assert summarize_notes_v2(test1) == ans1

# Read input
with open("day13.txt") as f:
    input = f.read()
    print(summarize_notes_v2(input))
