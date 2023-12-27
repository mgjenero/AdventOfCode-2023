def hash(line):
    res = 0
    for char in line:
        res += ord(char)
        res *= 17
        res = res % 256
    return res


def hash_sum(input):
    ans = 0
    for chars in input.split(","):
        ans += hash(chars)
    return ans


# Testing
test1 = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
ans1 = 1320
assert hash_sum(test1) == ans1

# Read input
with open("day15.txt") as f:
    input = f.read()
    print(hash_sum(input))
