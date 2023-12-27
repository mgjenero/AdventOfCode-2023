def block_vertical(block):
    for l in range(len(block[0])-1):
        r = l + 1
        good = True
        length = min(l+1, len(block[0])-(l+1))
        for row in block:
            lr = row[l+1-length:l+1]
            lr.reverse()
            rr = row[r:r+length]
            if lr != rr:
                good = False
                break
        if good:
            return l+1
    return 0


def block_horizontal(block):
    for l in range(len(block)-1):
        org_l = l
        r = l + 1
        good = True
        while l >= 0 and r < len(block):
            if block[l] != block[r]:
                good = False
                break
            l -= 1
            r += 1
        if good:
            return (org_l+1) * 100
    return 0


def summarize_notes(input):
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
ans1 = 405
assert summarize_notes(test1) == ans1

# Read input
with open("day13.txt") as f:
    input = f.read()
    print(summarize_notes(input))
