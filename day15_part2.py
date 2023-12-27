def hash(line):
    res = 0
    for char in line:
        res += ord(char)
        res *= 17
        res = res % 256
    return res


def focusing_power(input):
    ans = 0
    boxes = [{} for i in range(256)]
    for chars in input.split(","):
        if "-" in chars:
            label = chars.split("-")[0]
            hash_val = hash(label)
            if label in boxes[hash_val]:
                del boxes[hash_val][label]
        if "=" in chars:
            label = chars.split("=")[0]
            hash_val = hash(label)
            boxes[hash_val][label] = int(chars.split("=")[1])
    for i, box in enumerate(boxes):
        for j, label in enumerate(box):

            box_num = i+1
            slot = j+1
            focal_len = box[label]
            ans += box_num * slot * focal_len
    return ans


# Testing
test1 = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
ans1 = 145
assert focusing_power(test1) == ans1

# Read input
with open("day15.txt") as f:
    input = f.read()
    print(focusing_power(input))
