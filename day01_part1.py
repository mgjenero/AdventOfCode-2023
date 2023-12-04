def calibration_value(s: str) -> int:
    for i in s:
        if i.isdigit():
            first = int(i)
            break

    for i in reversed(s):
        if i.isdigit():
            last = int(i)
            break
    return first * 10 + last


def sum_calibration_values(lines: list[str]) -> int:
    total = 0
    for line in lines:
        num = calibration_value(line)
        total += num
    return total


# Testing
test1 = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet"]
ans1 = 142
test2 = [
    "a2b3c4",
    "xyz5uvw",
    "def6ghi",
    "jkl7mno"]
ans2 = 222
assert (sum_calibration_values(test1) == ans1)
assert (sum_calibration_values(test2) == ans2)

# Read input
with open("day1.txt", "r") as f:
    lines = f.readlines()
    print(sum_calibration_values(lines))

# Runtime = O(n*m)
# Space O(1)
#
# where n = number of characters in lo-ngest string
# where m is number of strings in list
