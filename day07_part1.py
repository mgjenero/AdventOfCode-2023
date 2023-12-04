from collections import Counter


def get_strength(cards):
    count = Counter(cards)
    vals = list(count.values())
    max_val = max(vals)
    # Five of a kind
    if max_val == 5:
        return 7
    # Four of a kind
    if max_val == 4:
        return 6
    # Full house
    if 3 in vals and 2 in vals:
        return 5
    # Three of a kind
    if max_val == 3:
        return 4
    # Two pair
    if vals.count(2) == 2:
        return 3
    # Pair
    if max_val == 2:
        return 2
    # All distinct cards
    else:
        return 1


def calculate_winnings(lines):
    order = "23456789TJQKA"
    processed = []
    for line in lines:
        cards, bid = line.split()
        cards = [order.index(card) for card in cards]
        bid = int(bid)
        strength = get_strength(cards)
        processed.append(([strength, *cards, line.split()[0]], bid))
    processed.sort()
    total = 0
    for i, (_, bid) in enumerate(processed):
        total += bid * (i+1)
    return total


test1 = [
    "32T3K 765",
    "T55J5 684",
    "KK677 28",
    "KTJJT 220",
    "QQQJA 483"]
ans1 = 6440

assert calculate_winnings(test1) == ans1

# Read input
with open("day7.txt", "r") as f:
    lines = f.readlines()
    print(calculate_winnings(lines))

#  Runtime O(nlogn)
#  Space O(n)
#  where n is the number of lines in the input file
