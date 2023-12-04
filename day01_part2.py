class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.number = None


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word, number) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.number = number


calibration_values = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

trie = Trie()
# Insert all words/nums into trie
for word, number in calibration_values.items():
    trie.insert(word, number)

reverse_trie = Trie()
# Insert all reversed words/(actual) nums into trie
for word, number in calibration_values.items():
    word = reversed(word)
    reverse_trie.insert(word, number)


def better_calibration_value(s: str) -> int:
    # search from start of string
    for i in range(len(s)):
        char = s[i].lower()
        if char.isdigit():
            first = int(char)
            break

        node = trie.root
        found = False
        while i < len(s):
            char = s[i].lower()
            if char not in node.children:
                break
            node = node.children[char]
            if node.is_end_of_word:
                first = node.number
                found = True
                break
            i = i + 1
        if found:
            break

    # search from end of string
    for i in range(len(s)-1, -1, -1):
        char = s[i].lower()
        if char.isdigit():
            last = int(char)
            break

        node = reverse_trie.root
        found = False
        while i > -1:
            char = s[i].lower()
            if char not in node.children:
                break
            node = node.children[char]
            if node.is_end_of_word:
                last = node.number
                found = True
                break
            i = i - 1
        if found:
            break

    return first * 10 + last


def better_sum_calibration_values(lines: list[str]) -> int:
    total = 0
    for line in lines:
        num = better_calibration_value(line)
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
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen"]
ans2 = 281

# Test case 3: Test case with some digits spelled out
test3 = [
    "onetwothree",
    "fourfivesix",
    "seveneightnine"]
ans3 = 138
assert (better_sum_calibration_values(test1) == ans1)
assert (better_sum_calibration_values(test2) == ans2)
assert (better_sum_calibration_values(test3) == ans3)

# Read input
with open("day1.txt", "r") as f:
    lines = f.readlines()
    print(better_sum_calibration_values(lines))

# Runtime = O(n * m), searching trie can be ignored since it is constant time
# Space O(1), we use only constant space(trie always has same size)
#
# where n = number of characters in longest string
# where m is number of strings in list
